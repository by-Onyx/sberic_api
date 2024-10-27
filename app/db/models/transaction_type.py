from sqlalchemy import Column, Integer, Text

from app.db.database import Base


class TransactionType(Base):
    __tablename__ = 'transaction_type'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False, unique=True)
