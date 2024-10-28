from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.location import Location
from app.services.location_service import LocationService

router = APIRouter(prefix='/location', tags=['location'])

__location_service = LocationService()


@router.get('/', response_model=List[Location])
async def get_locations(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    return __location_service.get_all_locations(db=db, skip=skip, limit=limit)

@router.get('/{location_id}', response_model=Location)
async def get_location_by_id(location_id: int, db: Session = Depends(get_db)):
    location = __location_service.get_location_by_id(db=db, location_id=location_id)
    if location is None:
        raise HTTPException(status_code=404, detail='Location not found')
    return location
