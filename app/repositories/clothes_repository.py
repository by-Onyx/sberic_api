from typing import Optional

from sqlalchemy.orm import Session

from app.db.models.clothes import Clothes
from app.repositories.base.base_repository import BaseRepository


class ClothesRepository(BaseRepository[Clothes]):

    def get_clothes_price(self, db: Session, clothes_id: int) -> Optional[float]:
        return db.query(Clothes).filter(Clothes.id == clothes_id).first().price
