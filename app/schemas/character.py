from typing import Optional

from pydantic import BaseModel


class Character(BaseModel):
    id: Optional[int]
    name: Optional[str]
    happiness_percent: Optional[int]