from sqlalchemy import Column, Integer, Text, Numeric, Enum

from app.db.database import Base
from app.db.models.enum.clothes_enum import ClothesEnum


class Clothes(Base):
    __tablename__ = 'clothes'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    file_name = Column(Text, nullable=False, unique=True)
    type = Column(Enum(ClothesEnum, name='clothes_enum'), nullable=False)
    x = Column(Numeric(7, 2), nullable=False)
    y = Column(Numeric(7, 2), nullable=False)
    width = Column(Numeric(7, 2), nullable=False)
    height = Column(Numeric(7, 2), nullable=False)
