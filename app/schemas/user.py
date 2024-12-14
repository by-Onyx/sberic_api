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


class UserLoginResponse(BaseModel):
    id: Optional[int]
    login: Optional[str]
    age: Optional[int]
    game_balance: Optional[float]
    real_balance: Optional[float]
    location: Optional[Location] = None
    character: Optional[CharacterWithClothes] = None
    access_token: Optional[str] = None

    model_config = {
        'from_attributes': True
    }


class UserRegisterRequest(BaseModel):
    login: Optional[str]
    age: Optional[int]
    password: Optional[str]

class UserLoginRequest(BaseModel):
    login: Optional[str]
    password: Optional[str]