from typing import Optional

from pydantic import BaseModel


class Clothes(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]
    file_name: Optional[str]
    clothes_type_id: Optional[int] = None


