from typing import List

from sqlalchemy.orm import Session

from app.repositories.user_clothes_repository import UserClothesRepository


class UserClothesService:

    def __init__(self):
        self.__user_clothes_repository = UserClothesRepository()

    def get_clothes_ids_by_user_id(self, db: Session, user_id: int) -> List[int]:
        return self.__user_clothes_repository.get_user_clothes_id(db=db, user_id=user_id)

    def is_user_clothes_exist(self, db: Session, user_id: int, clothes_id: int) -> bool:
        return self.__user_clothes_repository.is_user_clothes_exists(db=db, user_id=user_id, clothes_id=clothes_id)