from typing import Optional

from pydantic import BaseModel

from app.schemas.character import CharacterWithClothes
from app.schemas.location import Location


class User(BaseModel):
    id: Optional[int]
    login: Optional[str]
    age: Optional[int]
    game_balance: Optional[float]
    real_balance: Optional[float]


class UserBalance(BaseModel):
    balance: Optional[float]


class UserLogin(BaseModel):
    id: Optional[int]
    login: Optional[str]
    age: Optional[int]
    game_balance: Optional[float]
    real_balance: Optional[float]
    location: Optional[Location] = None
    character: Optional[CharacterWithClothes] = None

    model_config = {
        'from_attributes': True
    }
