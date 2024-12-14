from typing import Optional

from sqlalchemy.orm import Session

from app.db.models.user import User
from app.repositories.base.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):

    def get_user_game_balance(self, db: Session, user_id: int) -> Optional[float]:
        user = self.get(db=db, id=user_id)
        return user.game_balance

    def set_user_game_balance(self, db: Session, user_id: int, balance: float) -> Optional[float]:
        user = self.update(db=db, id=user_id, game_balance=balance)
        return user.game_balance

    def get_user_real_balance(self, db: Session, user_id: int) -> Optional[float]:
        user = self.get(db=db, id=user_id)
        return user.real_balance

    def set_user_real_balance(self, db: Session, user_id: int, balance: float) -> Optional[float]:
        user = self.update(db=db, id=user_id, real_balance=balance)
        return user.real_balance

    def create_user(self, db: Session, login: str, password: str, age: int) -> User:
        return self.create(db=db, login=login, password=password, age=age, game_balance=0, real_balance=0)

    def get_user_by_login(self, db: Session, login: str) -> Optional[User]:
        return db.query(User).filter(User.login == login).first()