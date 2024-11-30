from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models.character import Character
from app.repositories.character_repository import CharacterRepository
from app.schemas.clothes import Clothes
from app.services.character_clothes_service import CharacterClothesService
from app.services.clothes_service import ClothesService


class CharacterService:

    def __init__(self):
        self.__character_repository = CharacterRepository(Character)
        self.__clothes_service = ClothesService()
        self.__character_clothes_service = CharacterClothesService()

    def get_all_characters(self, db: Session, skip: int = 0, limit: int = 1000) -> List[Character]:
        return self.__character_repository.get_all(db=db, skip=skip, limit=limit)

    def get_character_by_id(self, db: Session, character_id: int) -> Optional[Character]:
        return self.__character_repository.get(db=db, id=character_id)

    def get_character_clothes(self, db: Session, character_id: int) -> List[Clothes]:
        clothes_ids = self.__character_clothes_service.get_clothes_ids_by_character_id(db=db, character_id=character_id)
        return [clothes for clothes_id in clothes_ids if
                (clothes := self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id))]

    def get_character_clothes_by_id(self, db: Session, character_id: int, clothes_id: int) -> Optional[Clothes]:
        is_exists = self.__character_clothes_service.is_character_clothes_exist(db=db, character_id=character_id,
                                                                                clothes_id=clothes_id)
        return self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id) if is_exists else None

    def change_character_clothes(self, db: Session, character_id: int, clothes_id: int) -> Optional[Clothes]:
        new_clothes = self.__clothes_service.get_clothes_by_id(db=db, clothes_id=clothes_id)
        clothes = self.get_character_clothes(db=db, character_id=character_id)

        for clothe in clothes:
            if clothe.type == new_clothes.type:
                self.__character_clothes_service.delete_character_clothes(db=db, character_id=character_id, clothes_id=clothe.id)

        self.__character_clothes_service.set_character_clothes(db=db, character_id=character_id, clothes_id=clothes_id)

        return new_clothes

    def delete_character_clothes(self, db: Session, character_id: int, clothes_id: int) -> bool:
        row_count = self.__character_clothes_service.delete_character_clothes(db=db, character_id=character_id,
                                                                  clothes_id=clothes_id)
        return True if row_count > 0 else False