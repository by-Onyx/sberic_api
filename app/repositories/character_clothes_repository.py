from typing import List

from sqlalchemy.orm import Session

from app.db.models.character_clothes import CharacterClothes


class CharacterClothesRepository:

    def get_character_clothes_id(self, db: Session, character_id: int)-> List[int]:
        return [clothes.clothes_id for clothes in
                 db.query(CharacterClothes.clothes_id).filter(CharacterClothes.character_id == character_id).all()]

    def is_user_character_exists(self, db: Session, character_id: int, clothes_id: int) -> bool:
        return db.query(CharacterClothes).filter_by(clothes_id=clothes_id, character_id=character_id).first() is not None