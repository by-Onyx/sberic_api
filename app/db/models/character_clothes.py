from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from ..database import Base


class Character_Clothes(Base):
    __tablename__ = 'character_clothes'

    character_id = Column(Integer, ForeignKey('character.id', ondelete='CASCADE'), nullable=False)
    clothes_id = Column(Integer, ForeignKey('clothes.id', ondelete='SET NULL'), nullable=True)

    __table_args__ = (PrimaryKeyConstraint('character_id', 'clothes_id'),)
