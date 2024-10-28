from typing import Optional, List

from sqlalchemy.orm import Session

from app.api.routes.clothes_routes import __clothes_service
from app.db.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.character import Character
from app.schemas.clothes import Clothes
from app.schemas.location import Location
from app.services.character_service import CharacterService
from app.services.clothes_service import ClothesService
from app.services.location_service import LocationService
from app.services.user_character_service import UserCharacterService
from app.services.user_clothes_service import UserClothesService
from app.services.user_location_service import UserLocationService


class UserService:

    def __init__(self):
        self.__user_repository = UserRepository(User)
        self.__location_service = LocationService()
        self.__character_service = CharacterService()
        self.__clothes_service = ClothesService()
        self.__character_service = CharacterService()
        self.__user_location_service = UserLocationService()
        self.__user_character_service = UserCharacterService()
        self.__user_clothes_service = UserClothesService()

    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        return self.__user_repository.get(db=db, id=user_id)

    def get_user_locations(self, db: Session, user_id: int) -> List[Location]:
        location_ids = self.__user_location_service.get_location_ids_by_user_id(db=db, user_id=user_id)
        return [location for location_id in location_ids if
                (location := self.__location_service.get_location_by_id(db=db, location_id=location_id)) is not None]

    def get_user_characters(self, db: Session, user_id: int) -> List[Character]:
        character_ids = self.__user_character_service.get_character_ids_by_user_id(db=db, user_id=user_id)
        return [character for character_id in character_ids if
                (character := self.__character_service.get_character_by_id(db=db, character_id=character_id)) is not None]

    def get_user_character_by_id(self, db: Session, user_id: int, character_id: int) -> Optional[Character]:
        is_exists = self.__user_character_service.is_user_character_exist(db=db, user_id=user_id, character_id=character_id)
        return self.__character_service.get_character_by_id(db=db, character_id=character_id) if is_exists else None

    def get_user_clothes(self, db: Session, user_id: int) -> List[Clothes]:
        clothes_ids = self.__user_clothes_service.get_clothes_ids_by_user_id(db=db, user_id=user_id)
        return [clothes for clothes_id in clothes_ids if
                (clothes := self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id))]

    def get_user_clothes_by_id(self, db: Session, user_id: int, clothes_id: int) -> Optional[Character]:
        is_exists = self.__user_clothes_service.is_user_clothes_exist(db=db, user_id=user_id, clothes_id=clothes_id)
        return self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id) if is_exists else None

    def get_user_character_clothes(self, db: Session, user_id: int, character_id: int) -> List[Clothes]:
        is_exists = self.__user_character_service.is_user_character_exist(db=db, user_id=user_id, character_id=character_id)
        return self.__character_service.get_character_clothes(db=db, character_id=character_id) if is_exists else None

    def get_user_character_clothes_by_id(self, db: Session, user_id: int, character_id: int, clothes_id: int) -> Optional[Character]:
        is_exists = self.__user_character_service.is_user_character_exist(db=db, user_id=user_id,
                                                                          character_id=character_id)
        return self.__character_service.get_character_clothes_by_id(db=db, character_id=character_id,
                                                                    clothes_id=clothes_id) if is_exists else None
