from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models.user_location import UserLocation


class UserLocationRepository:

    def get_user_location_ids(self, db: Session, user_id: int) -> List[int]:
        return [location.location_id for location in
                db.query(UserLocation.location_id).filter(UserLocation.user_id == user_id).all()]

    def is_user_location_exists(self, db: Session, user_id: int, location_id: int) -> bool:
        return db.query(UserLocation).filter_by(location_id=location_id, user_id=user_id).first() is not None

    def get_active_user_location(self, db: Session, user_id: int) -> Optional[int]:
        locations = db.query(UserLocation.location_id).filter_by(user_id=user_id, is_active=True).first()
        return locations.location_id if locations else None

    def set_active_user_location(self, db: Session, user_id: int, location_id: int) -> None:
        locations = db.query(UserLocation).filter(
            UserLocation.user_id == user_id).all()
        for location in locations:
            location.is_active = location.location_id == location_id
        db.commit()

    def add_user_location(self, db: Session, user_id: int, location_id: int) -> None:
        db.add(UserLocation(user_id=user_id, location_id=location_id, is_active=False))
        db.commit()
