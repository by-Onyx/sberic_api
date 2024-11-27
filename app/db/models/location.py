from sqlalchemy import Column, Integer, Text, Numeric, Enum

from app.db.database import Base
from app.db.models.enum.location_enum import LocationEnum


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
    description = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    file_name = Column(Text, nullable=False, unique=True)
    type = Column(Enum(LocationEnum, name='location_enum'), nullable=False)
