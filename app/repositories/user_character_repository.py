from typing import List, Optional

from sqlalchemy.orm import Session

from app.db.models.user_character import UserCharacter


class UserCharacterRepository:

    def get_user_character_ids(self, db: Session, user_id: int) -> List[int]:
        return [character.character_id for character in
                db.query(UserCharacter.character_id).filter(UserCharacter.user_id == user_id).all()]

    def create_user_character(self, db: Session, user_id: int, character_id: int) -> None:
        db.add(UserCharacter(character_id=character_id, user_id=user_id, is_active=True))
        db.commit()

    def is_user_character_exists(self, db: Session, user_id: int, character_id: int) -> bool:
        return db.query(UserCharacter).filter_by(character_id=character_id, user_id=user_id).first() is not None

    def get_active_user_character(self, db: Session, user_id: int) -> Optional[int]:
        characters = db.query(UserCharacter.character_id).filter(
            UserCharacter.user_id == user_id and UserCharacter.is_active == True).first()
        return characters.character_id if characters else None

    def set_active_user_character(self, db: Session, user_id: int, character_id: int) -> None:
        characters = db.query(UserCharacter.character_id).filter(
            UserCharacter.user_id == user_id).all()
        for character in characters:
            character.is_active = character.character_id == character_id
