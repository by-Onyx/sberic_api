from sqlalchemy import Column, Integer, Text, SMALLINT, Numeric, TIMESTAMP, text

from app.db.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    login = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    age = Column(SMALLINT, nullable=False)
    balance = Column(Numeric(10, 2), nullable=False)
    creation_date = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
