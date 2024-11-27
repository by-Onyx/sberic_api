from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models.purpose import Purpose
from app.repositories.purpose_repository import PurposeRepository


class PurposeService:
    def __init__(self):
        self.__purpose_repository = PurposeRepository(Purpose)

    def get_incomplete_purposes(self, db: Session, user_id: int) -> List[Purpose]:
        return self.__purpose_repository.get_incomplete_purposes(db=db, user_id=user_id)

    def get_complete_purposes(self, db: Session, user_id: int) -> List[Purpose]:
        return self.__purpose_repository.get_complete_purposes(db=db, user_id=user_id)

    def get_purpose_by_id(self, db: Session, purpose_id: int) -> Optional[Purpose]:
        return self.__purpose_repository.get_purpose_by_id(db=db, purpose_id=purpose_id)

    def create_purpose(self, db: Session, name: str, user_id: int, price: float) -> Optional[Purpose]:
        return self.__purpose_repository.create_purpose(db=db, name=name, user_id=user_id, price=price)

    def add_accumulation(self, db: Session, purpose_id: int, accumulation: float) -> Optional[Purpose]:
        return self.__purpose_repository.add_accumulation(db=db, purpose_id=purpose_id, accumulation=accumulation)

    def complete_purpose(self, db: Session, purpose_id: int, accumulation: float) -> Optional[Purpose]:
        return self.__purpose_repository.complete_purpose(db=db, purpose_id=purpose_id, accumulation=accumulation)

    def delete_purpose(self, db: Session, purpose_id: int) -> Optional[Purpose]:
        return self.__purpose_repository.delete_purpose(db=db, purpose_id=purpose_id)