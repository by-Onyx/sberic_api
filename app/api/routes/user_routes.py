from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.character import Character
from app.schemas.clothes import Clothes
from app.schemas.location import Location
from app.schemas.purpose import Purpose, PurposeCreate, PurposePrice
from app.schemas.user import User, UserBalance
from app.services.user_service import UserService

router = APIRouter(prefix='/user', tags=['user'])

__user_service = UserService()


@router.get('/{user_id}', response_model=User)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = __user_service.get_user_by_id(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.get('/{user_id}/location/', response_model=List[Location])
async def get_locations_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_locations(db=db, user_id=user_id)


@router.get('/{user_id}/location/{location_id}', response_model=Location)
async def get_location_by_user_id(user_id: int, location_id: int, db: Session = Depends(get_db)):
    location = __user_service.get_user_locations(db=db, user_id=user_id)
    if location is None:
        raise HTTPException(status_code=404, detail='User location not found')
    return location


@router.post('/{user_id}/location/{location_id}', response_model=Location)
async def set_active_location(user_id: int, location_id: int, db: Session = Depends(get_db)):
    location = __user_service.set_active_location(db=db, user_id=user_id, location_id=location_id)
    if location is None:
        raise HTTPException(status_code=404, detail='User location not found')
    return location


@router.post('/{user_id}/location/{location_id}/purchase', response_model=float)
async def purchase_location(user_id: int, location_id: int, db: Session = Depends(get_db)):
    balance = __user_service.purchase_location(db=db, user_id=user_id, location_id=location_id)
    if balance is None:
        raise HTTPException(status_code=402, detail='Purchase exception')
    return balance


@router.get('/{user_id}/clothes/', response_model=List[Clothes])
async def get_clothes_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_clothes(db=db, user_id=user_id)


@router.get('/{user_id}/clothes/{clothes_id}', response_model=Clothes)
async def get_clothes_by_user_id(user_id: int, clothes_id: int, db: Session = Depends(get_db)):
    clothes = __user_service.get_user_clothes_by_id(db=db, user_id=user_id, clothes_id=clothes_id)
    if clothes is None:
        raise HTTPException(status_code=404, detail='User clothes not found')
    return clothes


@router.post('/{user_id}/clothes/{clothes_id}/purchase', response_model=float)
async def purchase_clothes(user_id: int, clothes_id: int, db: Session = Depends(get_db)):
    balance = __user_service.purchase_clothes(db=db, user_id=user_id, clothes_id=clothes_id)
    if balance is None:
        raise HTTPException(status_code=402, detail='Purchase exception')
    return balance


@router.get('/{user_id}/character/', response_model=List[Character])
async def get_characters_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_characters(db=db, user_id=user_id)


@router.get('/{user_id}/character/{character_id}', response_model=Character)
async def get_character_by_user_id(user_id: int, character_id: int, db: Session = Depends(get_db)):
    character = __user_service.get_user_character_by_id(db=db, user_id=user_id, character_id=character_id)
    if character is None:
        raise HTTPException(status_code=404, detail='User character not found')
    return character


@router.post('/{user_id}/character/{character_id}', response_model=Character)
async def set_active_character(user_id: int, character_id: int, db: Session = Depends(get_db)):
    character = __user_service.set_active_character(db=db, user_id=user_id, character_id=character_id)
    if character is None:
        raise HTTPException(status_code=404, detail='User character not found')
    return character


@router.get('/{user_id}/character/{character_id}/clothes/', response_model=List[Clothes])
async def get_clothes_by_character_id(user_id: int, character_id: int, db: Session = Depends(get_db)):
    return __user_service.get_user_character_clothes(db=db, user_id=user_id, character_id=character_id)


@router.get('/{user_id}/character/{character_id}/clothes/{clothes_id}', response_model=Clothes)
async def get_clothes_by_character_id(user_id: int, character_id: int, clothes_id: int, db: Session = Depends(get_db)):
    clothes = __user_service.get_user_character_clothes_by_id(db=db, user_id=user_id, character_id=character_id,
                                                              clothes_id=clothes_id)
    if clothes is None:
        raise HTTPException(status_code=404, detail='User character clothes not found')
    return clothes


@router.post('/{user_id}/purpose', response_model=Purpose)
async def create_purpose(user_id: int, purpose: PurposeCreate, db: Session = Depends(get_db)):
    return __user_service.create_purpose(db=db, user_id=user_id, name=purpose.name, price=purpose.price)


@router.put('/{user_id}/purpose/{purpose_id}', response_model=Purpose)
async def add_accumulation(user_id: int, purpose_id: int, purpose: PurposePrice, db: Session = Depends(get_db)):
    return __user_service.add_accumulation(db=db, user_id=user_id, purpose_id=purpose_id, accumulation=purpose.price)


@router.delete('/{user_id}/purpose/{purpose_id}', response_model=Purpose)
async def delete_purpose(user_id: int, purpose_id: int, db: Session = Depends(get_db)):
    return __user_service.delete_purpose(db=db, user_id=user_id, purpose_id=purpose_id)


@router.get('/{user_id}/purpose/incomplete', response_model=List[Purpose])
async def get_user_purpose_incomplete(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_incomplete_purposes(db=db, user_id=user_id)


@router.get('/{user_id}/purpose/complete', response_model=List[Purpose])
async def get_user_purpose_complete(user_id: int, db: Session = Depends(get_db)):
    return __user_service.get_complete_purposes(db=db, user_id=user_id)


@router.post('/{user_id}', response_model=float)
async def add_user_balance(user_id: int, user_balance: UserBalance, db: Session = Depends(get_db)):
    balance = __user_service.add_balance(db=db, user_id=user_id, balance=user_balance.balance)
    if balance is None:
        raise HTTPException(status_code=404, detail='User not found')
    return balance