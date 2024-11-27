from typing import Optional

from sqlalchemy.orm import Session

from app.db.models.location import Location
from app.repositories.base.base_repository import BaseRepository


class LocationRepository(BaseRepository[Location]):

    def get_location_price(self, db: Session, location_id: int) -> Optional[float]:
        return db.query(Location).filter(Location.id == location_id).first().price

