from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    login: Optional[str]
    age: Optional[int]
    game_balance: Optional[float]
    real_balance: Optional[float]


class UserBalance(BaseModel):
    balance: Optional[float]
