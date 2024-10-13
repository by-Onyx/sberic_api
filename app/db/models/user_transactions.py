from sqlalchemy import Column, Integer, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP

from ..database import Base


class UserTransactions(Base):
    __tablename__ = 'user_transactions'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'), nullable=True)
    user_login = Column(Text, nullable=False, unique=True)
    transfer_amount = Column(Numeric(10, 2), nullable=False)
    transaction_type_id = Column(Integer, ForeignKey('transaction_type.id', ondelete='CASCADE'), nullable=False)
    datetime = Column(TIMESTAMP, nullable=False)
