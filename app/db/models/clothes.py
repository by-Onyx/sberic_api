from sqlalchemy import Column, Integer, Text, ForeignKey

from ..database import Base


class Clothes(Base):
    __tablename__ = 'clothes'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    file_name = Column(Text, nullable=False, unique=True)
    clothes_type_id = Column(Integer, ForeignKey('clothes_type.id', ondelete='SET NULL'), nullable=True)
