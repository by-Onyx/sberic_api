from typing import List

from sqlalchemy.orm import Session

from app.db.models.user_character import UserCharacter


class UserCharacterRepository:

    def get_user_character_ids(self, db: Session, user_id: int) -> List[int]:
        return [character.character_id for character in
                db.query(UserCharacter.character_id).filter(UserCharacter.user_id == user_id).all()]

    def is_user_character_exists(self, db: Session, user_id: int, character_id: int) -> bool:
        return db.query(UserCharacter).filter_by(character_id=character_id, user_id=user_id).first() is not None
