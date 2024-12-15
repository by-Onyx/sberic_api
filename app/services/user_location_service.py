from typing import List, Optional

from sqlalchemy.orm import Session
from app.repositories.user_location_repository import UserLocationRepository


class UserLocationService:

    def __init__(self):
        self.__user_location_repository = UserLocationRepository()

    def get_location_ids_by_user_id(self, db: Session, user_id: int) -> List[int]:
        return self.__user_location_repository.get_user_location_ids(db=db, user_id=user_id)

    def is_user_location_exist(self, db: Session, user_id: int, location_id: int) -> bool:
        return self.__user_location_repository.is_user_location_exists(db=db, user_id=user_id, location_id=location_id)

    def get_active_user_location(self, db: Session, user_id: int) -> Optional[int]:
        return self.__user_location_repository.get_active_user_location(db=db, user_id=user_id)

    def set_active_user_location(self, db: Session, user_id: int, location_id: int) -> None:
        self.__user_location_repository.set_active_user_location(db=db, user_id=user_id, location_id=location_id)

    def add_user_location(self, db: Session, user_id: int, location_id: int) -> None:
        self.__user_location_repository.add_user_location(db=db, user_id=user_id, location_id=location_id)

    def add_user_location_active(self, db: Session, user_id: int, location_id: int) -> None:
        self.__user_location_repository.add_user_location_active(db=db, user_id=user_id, location_id=location_id)
