from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    login: Optional[str]
    age: Optional[int]
    balance: Optional[float]