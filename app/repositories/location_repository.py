from sqlalchemy.orm import Session

from app.db.models.location import Location
from app.repositories.base.base_repository import BaseRepository


class LocationRepository(BaseRepository[Location]):
    pass
