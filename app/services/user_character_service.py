from typing import List

from sqlalchemy.orm import Session

from app.repositories.user_character_repository import UserCharacterRepository


class UserCharacterService:

    def __init__(self):
        self.__user_character_repository = UserCharacterRepository()

    def get_character_ids_by_user_id(self, db: Session, user_id: int) -> List[int]:
        return self.__user_character_repository.get_user_character_ids(db=db, user_id=user_id)

    def is_user_character_exist(self, db: Session, user_id: int, character_id: int) -> bool:
        return self.__user_character_repository.is_user_character_exists(db=db, user_id=user_id, character_id=character_id)
