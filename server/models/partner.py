"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Partner(Base):
    __tablename__ = 'mtt_md_partners'

    partner_id      = Column(String(50), primary_key=True)
    partner_status  = Column(SMALLINT, nullable=False)
    partner_name    = Column(String(50), nullable=False)
    created_at      = Column(DateTime, nullable=False)
    updated_at      = Column(DateTime, nullable=False)

    def __init__(self, partner_id=None, partner_status=200, partner_name=None):
        self.partner_id = partner_id
        self.partner_status = partner_status
        self.partner_name = partner_name
