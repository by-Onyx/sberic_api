from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey

from ..database import Base


class UserClothes(Base):
    __tablename__ = 'user_clothes'

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    clothes_id = Column(Integer, ForeignKey('clothes.id', ondelete='SET NULL'), nullable=True)

    __table_args__ = (PrimaryKeyConstraint('user_id', 'clothes_id'),)
