from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from app.db.database import Base


class UserCharacter(Base):
    __tablename__ = 'user_character'

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id', ondelete='CASCADE'), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('user_id', 'character_id'),)