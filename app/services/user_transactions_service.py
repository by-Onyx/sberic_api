from typing import List

from sqlalchemy.orm import Session

from app.db.models.user_transactions import UserTransactions
from app.repositories.user_transactions_repository import UserTransactionsRepository


class UserTransactionsService:

    def __init__(self):
        self.__user_transactions_repository = UserTransactionsRepository()

    def get_user_transactions(self, db: Session, user_id: int, skip: int = 0, limit: int = 1000) -> List[UserTransactions]:
        return self.__user_transactions_repository.get_by_user_id(db, user_id, skip, limit)

    def add_user_transactions(self, db: Session, user_id: int, type: str, transfer_amount: float):
        return self.__user_transactions_repository.add_user_transactions(db, user_id, type, transfer_amount)