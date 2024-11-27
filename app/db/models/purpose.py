from sqlalchemy import Column, Integer, Text, Numeric, ForeignKey, Boolean

from app.db.database import Base

class Purpose(Base):
    __tablename__ = 'purpose'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    accumulated = Column(Numeric(10, 2), nullable=False)
    is_complete = Column(Boolean, nullable=False, default=False)
