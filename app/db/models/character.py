from sqlalchemy import Column, Integer, Text, Enum

from app.db.database import Base
from app.db.models.enum.character_enum import CharacterEnum


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
    type = Column(Enum(CharacterEnum, name='character_enum'), nullable=False)
    happiness_percent = Column(Integer, nullable=False)
