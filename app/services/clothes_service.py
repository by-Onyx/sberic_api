from typing import Optional, List

from sqlalchemy.orm import Session

from app.db.models.clothes import Clothes
from app.repositories.clothes_repository import ClothesRepository


class ClothesService:
    def __init__(self):
        self.__clothes_repository = ClothesRepository(Clothes)

    def get_all_clothes(self, db: Session, skip: int = 0, limit: int = 1000) -> List[Clothes]:
        return self.__clothes_repository.get_all(db=db, skip=skip, limit=limit)

    def get_clothes_by_id(self, db: Session, clothes_id: int) -> Optional[Clothes]:
        return self.__clothes_repository.get(db=db, id=clothes_id)

    def get_clothes_price(self, db: Session, clothes_id: int) -> Optional[float]:
        price = self.__clothes_repository.get_clothes_price(db=db, clothes_id=clothes_id)
        if price is None:
            raise Exception('Clothes not found')
        return price
