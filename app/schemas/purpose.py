from typing import Optional

from pydantic import BaseModel


class Purpose(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]
    accumulated: Optional[float]

class PurposeCreate(BaseModel):
    name: Optional[str]
    price: Optional[float]

class PurposePrice(BaseModel):
    price: Optional[float]