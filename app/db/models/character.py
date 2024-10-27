from sqlalchemy import Column, Integer, Text, ForeignKey

from app.db.database import Base


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
    character_type_id = Column(Integer, ForeignKey('character_type.id', ondelete='SET NULL'), nullable=True)
    happiness_percent = Column(Integer, nullable=False)
