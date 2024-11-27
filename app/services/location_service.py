from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models.location import Location
from app.repositories.location_repository import LocationRepository


class LocationService:
    def __init__(self):
        self.__location_repository = LocationRepository(Location)

    def get_all_locations(self, db: Session, skip: int = 0, limit: int = 1000) -> List[Location]:
        return self.__location_repository.get_all(db=db, skip=skip, limit=limit)

    def get_location_by_id(self, db: Session, location_id: int) -> Optional[Location]:
        return self.__location_repository.get(db=db, id=location_id)

    def get_location_price(self, db: Session, location_id: int) -> Optional[float]:
        price = self.__location_repository.get_location_price(db=db, location_id=location_id)
        if price is None:
            raise Exception("Location not found")
        return price
