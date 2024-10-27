from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint

from app.db.database import Base


class CharacterClothes(Base):
    __tablename__ = 'character_clothes'

    character_id = Column(Integer, ForeignKey('character.id', ondelete='CASCADE'), nullable=False)
    clothes_id = Column(Integer, ForeignKey('clothes.id', ondelete='CASCADE'), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('character_id', 'clothes_id'),)
