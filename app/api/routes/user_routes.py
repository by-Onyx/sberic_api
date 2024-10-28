from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.character import Character
from app.schemas.clothes import Clothes
from app.schemas.location import Location
from app.schemas.user import User
from app.services.user_service import UserService

router = APIRouter(prefix='/user', tags=['user'])

__user_service = UserService()


@router.get('/{user_id}', response_model=User)
async def get_location_by_id(user_id: int, db: Session = Depends(get_db)):
    user = __user_service.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.get('/{user_id}/location/', response_model=List[Location])
async def get_locations_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_locations(db=db, user_id=user_id)


@router.get('/{user_id}/clothes/', response_model=List[Clothes])
async def get_clothes_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_clothes(db=db, user_id=user_id)


@router.get('/{user_id}/clothes/{clothes_id}', response_model=Clothes)
async def get_clothes_by_user_id(user_id: int, clothes_id: int, db: Session = Depends(get_db)):
    clothes = __user_service.get_user_clothes_by_id(db=db, user_id=user_id, clothes_id=clothes_id)
    if clothes is None:
        raise HTTPException(status_code=404, detail='User clothes not found')
    return clothes


@router.get('/{user_id}/character/', response_model=List[Character])
async def get_characters_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_characters(db=db, user_id=user_id)


@router.get('/{user_id}/character/{character_id}', response_model=Character)
async def get_character_by_user_id(user_id: int, character_id: int, db: Session = Depends(get_db)):
    character = __user_service.get_user_character_by_id(db=db, user_id=user_id, character_id=character_id)
    if character is None:
        raise HTTPException(status_code=404, detail='User character not found')
    return character


@router.get('/{user_id}/character/{character_id}/clothes/', response_model=List[Clothes])
async def get_clothes_by_character_id(user_id: int, character_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_character_clothes(db=db, user_id=user_id, character_id=character_id)


@router.get('/{user_id}/character/{character_id}/clothes/{clothes_id}', response_model=Clothes)
async def get_clothes_by_user_id(user_id: int, character_id: int, clothes_id: int, db: Session = Depends(get_db)):
    clothes = __user_service.get_user_character_clothes_by_id(db=db, user_id=user_id, character_id=character_id,
                                                              clothes_id=clothes_id)
    if clothes is None:
        raise HTTPException(status_code=404, detail='User character clothes not found')
    return clothes
