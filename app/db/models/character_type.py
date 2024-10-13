from sqlalchemy import Column, Integer, Text

from ..database import Base


class CharacterType(Base):
    __tablename__ = 'character_type'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
