"""
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, SmallInteger, DateTime

Base = declarative_base()


class User(Base):
    __tablename__ = 'mtt_uw_users'

    user_no         = Column(Integer, primary_key=True)
    user_id         = Column(String(50), nullable=False, unique=True)
    partner_id      = Column(String(50), nullable=False)
    user_status     = Column(SmallInteger, nullable=False)
    user_type       = Column(SmallInteger, nullable=False)
    user_level      = Column(SmallInteger, nullable=False)
    first_name      = Column(String(50), nullable=False)
    last_name       = Column(String(50), nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, user_id, partner_id, user_status, user_type, user_level, first_name, last_name):
        self.user_id = user_id
        self.partner_id = partner_id
        self.user_status = user_status
        self.user_type = user_type
        self.user_level = user_level
        self.first_name = first_name
        self.last_name = last_name

