from typing import List

from sqlalchemy.orm import Session

from app.db.models.user_location import UserLocation
from app.repositories.user_location_repository import UserLocationRepository


class UserLocationService:

    def __init__(self):
        self.__user_location_repository = UserLocationRepository()

    def get_location_ids_by_user_id(self, db: Session, user_id: int) -> List[int]:
        return self.__user_location_repository.get_user_location_ids(db=db, user_id=user_id)
