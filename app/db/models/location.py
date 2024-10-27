from sqlalchemy import Column, Integer, Text, ForeignKey, Numeric

from app.db.database import Base


class Location(Base):
    __tablename__ = 'location'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
    price = Column(Numeric(10, 2), nullable=False)
    file_name = Column(Text, nullable=False, unique=True)
    type_id = Column(Integer, ForeignKey('location_type.id', ondelete='SET NULL'), nullable=True)
