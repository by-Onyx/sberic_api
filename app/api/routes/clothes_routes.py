from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.clothes import Clothes
from app.services.clothes_service import ClothesService

router = APIRouter(prefix='/clothes', tags=['clothes'])

__clothes_service = ClothesService()


@router.get('/', response_model=List[Clothes])
async def get_locations(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    return __clothes_service.get_all_clothes(db=db, skip=skip, limit=limit)

@router.get('/{location_id}', response_model=Clothes)
async def get_location_by_id(location_id: int, db: Session = Depends(get_db)):
    clothes = __clothes_service.get_clothes_by_id(db=db, location_id=location_id)
    if clothes is None:
        raise HTTPException(status_code=404, detail='Clothes not found')
    return clothes
