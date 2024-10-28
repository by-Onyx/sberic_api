from typing import List

from sqlalchemy.orm import Session

from app.db.models.user_clothes import UserClothes


class UserClothesRepository:

    def get_user_clothes_id(self, db: Session, user_id: int)-> List[int]:
        return [clothes.clothes_id for clothes in
                 db.query(UserClothes.clothes_id).filter(UserClothes.user_id == user_id).all()]

    def is_user_clothes_exists(self, db: Session, user_id: int, clothes_id: int) -> bool:
        return db.query(UserClothes).filter_by(clothes_id=clothes_id, user_id=user_id).first() is not None