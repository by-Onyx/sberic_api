from fastapi import HTTPException
from typing import Optional, List

from sqlalchemy.orm import Session

from app.db.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.character import Character, CharacterWithClothes
from app.schemas.clothes import Clothes
from app.schemas.location import Location
from app.schemas.purpose import Purpose
from app.schemas.user import UserRegisterRequest, UserLoginResponse, UserLoginRequest
from app.services.character_service import CharacterService
from app.services.clothes_service import ClothesService
from app.services.location_service import LocationService
from app.services.purpose_service import PurposeService
from app.services.user_character_service import UserCharacterService
from app.services.user_clothes_service import UserClothesService
from app.services.user_location_service import UserLocationService
from app.services.user_transactions_service import UserTransactionsService

from app.services.help_services.password_service import hash_password, verify_password
from app.services.help_services.jwt_service import create_access_token


class UserService:

    def __init__(self):
        self.__user_repository = UserRepository(User)
        self.__location_service = LocationService()
        self.__character_service = CharacterService()
        self.__clothes_service = ClothesService()
        self.__character_service = CharacterService()
        self.__purpose_service = PurposeService()
        self.__user_location_service = UserLocationService()
        self.__user_character_service = UserCharacterService()
        self.__user_clothes_service = UserClothesService()
        self.__user_transactions_service = UserTransactionsService()

    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return self.__user_repository.get(db=db, id=user_id)

    def get_user_by_login(self, db: Session, login: str) -> Optional[User]:
        return self.__user_repository.get_user_by_login(db=db, login=login)

    def register_user(self, db: Session, user: UserRegisterRequest) -> Optional[UserLoginResponse]:
        user.password = hash_password(user.password)
        new_user = self.__user_repository.create_user(db=db, login=user.login, password=user.password, age=user.age)

        user_response = UserLoginResponse.model_validate(new_user)
        user_response.access_token = create_access_token(user_id=new_user.id, login=new_user.login)

        return user_response


    def login_user(self, db: Session, user_login: UserLoginRequest) -> Optional[UserLoginResponse]:
        user = self.get_user_by_login(db=db, login=user_login.login)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if not verify_password(user_login.password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect password")

        user_response = UserLoginResponse.model_validate(user)
        user_response.access_token = create_access_token(user_id=user.id, login=user.login)
        user_response.location = self.get_active_location(db=db, user_id=user.id)

        character = self.get_active_character(db=db, user_id=user.id)

        if character is not None:
            user_response.character = CharacterWithClothes.model_validate(character)
            user_response.character.clothes = self.get_user_character_clothes(db=db, user_id=user.id,
                                                                                     character_id=character.id)

        return user_response


    def get_user_locations(self, db: Session, user_id: int) -> List[Location]:
        location_ids = self.__user_location_service.get_location_ids_by_user_id(db=db, user_id=user_id)
        return [location for location_id in location_ids if
                (location := self.__location_service.get_location_by_id(db=db, location_id=location_id)) is not None]

    def get_user_location_by_id(self, db: Session, user_id: int, location_id: int) -> Optional[Location]:
        if not self.__user_location_service.is_user_location_exist(db=db, user_id=user_id, location_id=location_id):
            raise HTTPException(status_code=404, detail="User location not found")
        return self.__location_service.get_location_by_id(db=db, location_id=location_id)

    def get_user_characters(self, db: Session, user_id: int) -> List[Character]:
        character_ids = self.__user_character_service.get_character_ids_by_user_id(db=db, user_id=user_id)
        return [character for character_id in character_ids if
                (character := self.__character_service.get_character_by_id(db=db,
                                                                           character_id=character_id)) is not None]

    def get_user_character_by_id(self, db: Session, user_id: int, character_id: int) -> Optional[Character]:
        if not self.__user_character_service.is_user_character_exist(db=db, user_id=user_id, character_id=character_id):
            raise HTTPException(status_code=404, detail="User character not found")
        return self.__character_service.get_character_by_id(db=db, character_id=character_id)

    def get_user_clothes(self, db: Session, user_id: int) -> List[Clothes]:
        clothes_ids = self.__user_clothes_service.get_clothes_ids_by_user_id(db=db, user_id=user_id)
        return [clothes for clothes_id in clothes_ids if
                (clothes := self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id))]

    def get_user_clothes_by_id(self, db: Session, user_id: int, clothes_id: int) -> Optional[Character]:
        if not self.__user_clothes_service.is_user_clothes_exist(db=db, user_id=user_id, clothes_id=clothes_id):
            raise HTTPException(status_code=404, detail="User clothes not found")
        return self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id)

    def get_user_character_clothes(self, db: Session, user_id: int, character_id: int) -> List[Clothes]:
        if not self.__user_character_service.is_user_character_exist(db=db, user_id=user_id, character_id=character_id):
            raise HTTPException(status_code=404, detail="User character not found")
        return self.__character_service.get_character_clothes(db=db, character_id=character_id)

    def get_user_character_clothes_by_id(self, db: Session, user_id: int, character_id: int, clothes_id: int) -> \
            Optional[Character]:
        if not self.__user_character_service.is_user_character_exist(db=db, user_id=user_id, character_id=character_id):
            raise HTTPException(status_code=404, detail="User character not found")
        return self.__character_service.get_character_clothes_by_id(db=db, character_id=character_id,
                                                                    clothes_id=clothes_id)

    def purchase_clothes(self, db: Session, user_id: int, clothes_id: int) -> float:
        balance = self.__user_repository.get_user_game_balance(db=db, user_id=user_id)
        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        if self.__user_clothes_service.is_user_clothes_exist(db=db, user_id=user_id, clothes_id=clothes_id):
            raise HTTPException(status_code=409, detail="Clothes already purchased")

        price = self.__clothes_service.get_clothes_price(db=db, clothes_id=clothes_id)
        if balance < price:
            raise HTTPException(status_code=402, detail="Not enough money")

        try:
            self.__user_clothes_service.add_user_clothes(db=db, user_id=user_id, clothes_id=clothes_id)
            current_balance = float(balance) - float(price)
            self.__user_repository.set_user_game_balance(db=db, user_id=user_id, balance=current_balance)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transaction failed: {str(e)}")

        return current_balance

    def purchase_location(self, db: Session, user_id: int, location_id: int) -> float:
        balance = self.__user_repository.get_user_game_balance(db=db, user_id=user_id)
        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        if self.__user_location_service.is_user_location_exist(db=db, user_id=user_id, location_id=location_id):
            raise HTTPException(status_code=409, detail="Location already purchased")

        price = self.__location_service.get_location_price(db=db, location_id=location_id)
        if balance < price:
            raise HTTPException(status_code=402, detail="Not enough money")

        try:
            self.__user_location_service.add_user_location(db=db, user_id=user_id, location_id=location_id)
            current_balance = float(balance) - float(price)
            self.__user_repository.set_user_game_balance(db=db, user_id=user_id, balance=current_balance)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transaction failed: {str(e)}")

        return current_balance

    def set_active_character(self, db: Session, user_id: int, character_id: int) -> Optional[Character]:
        is_exists = self.__user_character_service.is_user_character_exist(db=db, user_id=user_id,
                                                                          character_id=character_id)

        self.__user_character_service.set_active_user_character(db=db, user_id=user_id, character_id=character_id)

        return self.__character_service.get_character_by_id(db=db, character_id=character_id) if is_exists else None

    def get_active_character(self, db: Session, user_id: int) -> Optional[Character]:
        character_id = self.__user_character_service.get_active_user_character(db=db, user_id=user_id)

        return self.__character_service.get_character_by_id(db=db, character_id=character_id)

    def set_active_location(self, db: Session, user_id: int, location_id: int) -> Optional[Location]:
        is_exists = self.__user_location_service.is_user_location_exist(db=db, user_id=user_id,
                                                                        location_id=location_id)

        self.__user_location_service.set_active_user_location(db=db, user_id=user_id, location_id=location_id)

        return self.__location_service.get_location_by_id(db=db, location_id=location_id) if is_exists else None

    def get_active_location(self, db: Session, user_id: int) -> Optional[Location]:
        location_id = self.__user_location_service.get_active_user_location(db=db, user_id=user_id)

        return self.__location_service.get_location_by_id(db=db, location_id=location_id)

    def get_incomplete_purposes(self, db: Session, user_id: int) -> List[Purpose]:
        return self.__purpose_service.get_incomplete_purposes(db=db, user_id=user_id)

    def get_complete_purposes(self, db: Session, user_id: int) -> List[Purpose]:
        return self.__purpose_service.get_complete_purposes(db=db, user_id=user_id)

    def create_purpose(self, db: Session, user_id: int, name: str, price: float) -> Optional[Purpose]:
        return self.__purpose_service.create_purpose(db=db, user_id=user_id, name=name, price=price)

    def add_accumulation(self, db: Session, user_id, purpose_id: int, accumulation: float) -> Optional[Purpose]:
        balance = self.__user_repository.get_user_real_balance(db=db, user_id=user_id)
        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        purpose = self.__purpose_service.get_purpose_by_id(db=db, purpose_id=purpose_id)
        if purpose is None:
            raise HTTPException(status_code=404, detail="Purpose not found")

        try:
            remains = purpose.price - purpose.accumulated
            if remains > accumulation:
                new_accumulation_remains = float(accumulation) + float(purpose.accumulated)
                purpose = self.__purpose_service.add_accumulation(db=db, purpose_id=purpose_id,
                                                                  accumulation=new_accumulation_remains)
                current_balance = float(balance) - float(accumulation)
                self.__user_repository.set_user_real_balance(db=db, user_id=user_id, balance=current_balance)
            else:
                purpose = self.__purpose_service.complete_purpose(db=db, purpose_id=purpose_id,
                                                                  accumulation=purpose.price)
                current_balance = float(balance) - float(remains)
                self.__user_repository.set_user_real_balance(db=db, user_id=user_id, balance=current_balance)

            return purpose
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transaction failed: {str(e)}")

    def delete_purpose(self, db: Session, user_id: int, purpose_id: int) -> Optional[Purpose]:
        balance = self.__user_repository.get_user_real_balance(db=db, user_id=user_id)
        if balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        try:
            purpose = self.__purpose_service.delete_purpose(db=db, purpose_id=purpose_id)
            if purpose is None:
                raise HTTPException(status_code=404, detail="Purpose not found")

            current_balance = float(balance) + float(purpose.accumulated)
            self.__user_repository.set_user_real_balance(db=db, user_id=user_id, balance=current_balance)
            return purpose
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transaction failed: {str(e)}")

    def add_balance(self, db: Session, user_id: int, balance: float) -> Optional[User]:
        if balance < 0:
            raise HTTPException(status_code=422, detail="Price cannot be negative")

        real_balance = self.__user_repository.get_user_real_balance(db=db, user_id=user_id)
        if real_balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        game_balance = self.__user_repository.get_user_game_balance(db=db, user_id=user_id)
        if game_balance is None:
            raise HTTPException(status_code=404, detail="User not found")

        try:
            self.__user_repository.set_user_game_balance(db=db, user_id=user_id, balance=balance + float(game_balance))
            return self.__user_repository.set_user_real_balance(db=db, user_id=user_id,
                                                                balance=balance + float(real_balance))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Transaction failed: {str(e)}")

    def change_character_clothes(self, db: Session, character_id: int, clothes_id: int) -> Optional[Clothes]:
        return self.__character_service.change_character_clothes(db=db, character_id=character_id,
                                                                 clothes_id=clothes_id)

    def delete_character_clothes(self, db: Session, character_id: int, clothes_id: int) -> bool:
        return self.__character_service.delete_character_clothes(db=db, character_id=character_id,
                                                                 clothes_id=clothes_id)
