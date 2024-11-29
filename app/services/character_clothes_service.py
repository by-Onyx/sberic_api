from typing import List

from sqlalchemy.orm import Session

from app.repositories.character_clothes_repository import CharacterClothesRepository


class CharacterClothesService:

    def __init__(self):
        self.__character_clothes_repository = CharacterClothesRepository()

    def get_clothes_ids_by_character_id(self, db: Session, character_id: int) -> List[int]:
        return self.__character_clothes_repository.get_character_clothes_id(db=db, character_id=character_id)

    def set_character_clothes(self, db: Session, character_id: int, clothes_id: int) -> None:
        self.__character_clothes_repository.set_character_clothes(db=db, character_id=character_id, clothes_id=clothes_id)

    def is_character_clothes_exist(self, db: Session, character_id: int, clothes_id: int) -> bool:
        return self.__character_clothes_repository.is_user_character_exists(db=db, character_id=character_id,
                                                                            clothes_id=clothes_id)

    def delete_character_clothes(self, db: Session, character_id: int, clothes_id: int) -> int:
        return self.__character_clothes_repository.delete_character_clothes(db=db, character_id=character_id,
                                                                            clothes_id=clothes_id)
