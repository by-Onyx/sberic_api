from sqlalchemy import Column, Integer, PrimaryKeyConstraint, ForeignKey, Boolean

from app.db.database import Base


class UserLocation(Base):
    __tablename__ = 'user_location'

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    location_id = Column(Integer, ForeignKey('location.id', ondelete='CASCADE'), nullable=False)
    is_active = Column(Boolean, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('user_id', 'location_id'),)
