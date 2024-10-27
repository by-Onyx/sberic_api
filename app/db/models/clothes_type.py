from sqlalchemy import Column, Integer, Text

from app.db.database import Base


class ClothesType(Base):
    __tablename__ = 'clothes_type'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
