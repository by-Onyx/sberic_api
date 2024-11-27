from typing import List
from datetime import datetime

from sqlalchemy.orm import Session

from app.db.models.user_transactions import UserTransactions


class UserTransactionsRepository:
    def add_user_transactions(self, db: Session, user_id: int, type: str, transfer_amount: float):
        transaction = UserTransactions(
            user_id=user_id,
            type=type,
            transfer_amount=transfer_amount,
            datetime = datetime.now()
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)

    def get_by_user_id(self, db: Session, user_id: int, skip: int = 0, limit: int = 1000) -> List[UserTransactions]:
        return db.query(UserTransactions).filter(UserTransactions.user_id == user_id).offset(skip).limit(limit).all()