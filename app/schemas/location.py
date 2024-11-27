from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    file_name: Optional[str]
    type: Optional[str] = None
