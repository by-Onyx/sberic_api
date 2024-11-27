from typing import Optional, List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.db.models.purpose import Purpose
from app.repositories.base.base_repository import BaseRepository


class PurposeRepository(BaseRepository[Purpose]):

    def get_incomplete_purposes(self, db: Session, user_id: int) -> List[Purpose]:
        return db.query(Purpose).filter(Purpose.user_id == user_id).filter(Purpose.is_complete == False).all()

    def get_complete_purposes(self, db: Session, user_id: int) -> List[Purpose]:
        return db.query(Purpose).filter(Purpose.user_id == user_id).filter(Purpose.is_complete == True).all()

    def get_purpose_by_id(self, db: Session, purpose_id: int) -> Optional[Purpose]:
        return self.get(db=db, id=purpose_id)

    def complete_purpose(self, db: Session, purpose_id: int, accumulation: float) -> Optional[Purpose]:
        return self.update(db=db, id=purpose_id, accumulated=accumulation, is_complete=True)

    def create_purpose(self, db: Session, name: str, user_id: int, price: float) -> Optional[Purpose]:
        return self.create(db=db, name=name, user_id=user_id, price=price, accumulated=0, is_complete=False)

    def add_accumulation(self, db: Session, purpose_id: int, accumulation: float) -> Optional[Purpose]:
        return self.update(db=db, id=purpose_id, accumulated=accumulation)

    def delete_purpose(self, db: Session, purpose_id: int) -> Optional[Purpose]:
        return self.delete(db=db, id=purpose_id)
