from sqlalchemy import Column, Integer, ForeignKey, Numeric, text, Enum
from sqlalchemy.dialects.postgresql import TIMESTAMP

from app.db.database import Base
from app.db.models.enum.transaction_enum import TransactionEnum


class UserTransactions(Base):
    __tablename__ = 'user_transactions'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'), nullable=True)
    transfer_amount = Column(Numeric(10, 2), nullable=False)
    type = Column(Enum(TransactionEnum, name='transaction_enum'), nullable=False)
    datetime = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
