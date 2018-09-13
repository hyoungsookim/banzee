"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'mtt_uw_users'

    user_no         = Column(INTEGER, primary_key=True)
    user_id         = Column(String(50), nullable=False, unique=True)
    partner_id      = Column(String(50), nullable=False)
    user_status     = Column(SMALLINT, nullable=False)
    user_type       = Column(SMALLINT, nullable=False)
    user_level      = Column(SMALLINT, nullable=False)
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

