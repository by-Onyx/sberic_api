from typing import Optional, List

from pydantic import BaseModel

from app.schemas.clothes import Clothes


class Character(BaseModel):
    id: Optional[int]
    name: Optional[str]
    type: Optional[str]
    happiness_percent: Optional[int]


class CharacterWithClothes(BaseModel):
    id: Optional[int]
    name: Optional[str]
    type: Optional[str]
    happiness_percent: Optional[int]
    clothes: List[Clothes] = None

    model_config = {
        'from_attributes': True
    }