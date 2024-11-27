from typing import Optional

from pydantic import BaseModel


class Clothes(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    file_name: Optional[str]
    type: Optional[str] = None
    x: Optional[float]
    y: Optional[float]
    width: Optional[float]
    height: Optional[float]
