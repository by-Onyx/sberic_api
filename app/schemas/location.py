from typing import Optional

from pydantic import BaseModel


class Location(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]
    file_name: Optional[str]
    type_id: Optional[int] = None


