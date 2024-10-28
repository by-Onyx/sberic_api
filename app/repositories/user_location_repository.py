from typing import List

from sqlalchemy.orm import Session

from app.db.models.user_location import UserLocation


class UserLocationRepository:

    def get_user_location_ids(self, db: Session, user_id: int) -> List[int]:
        return [location.location_id for location in
                db.query(UserLocation.location_id).filter(UserLocation.user_id == user_id).all()]
