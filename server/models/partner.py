"""
"""

from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.ext.declarative import declarative_base

from server.app import db

#Base = declarative_base()
#metadata = Base.metadata


class Partner(db.Model):
    __tablename__ = 'mtt_md_partners'

    partner_id      = db.Column(String(50), primary_key=True)
    partner_status  = db.Column(SMALLINT, nullable=False)
    partner_name    = db.Column(String(50), nullable=False)
    created_at      = db.Column(DateTime, nullable=False)
    updated_at      = db.Column(DateTime, nullable=False)

    def __init__(self, partner_id, partner_name, partner_status=200):
        self.partner_id = partner_id
        self.partner_status = partner_status
        self.partner_name = partner_name
        self.created_at = datetime.now
        self.updated_at = datetime.now

    def __repr__(self):
        return self.partner_name

    def to_dict(self):
        pass
        #return (col.name: getattr(self, col.name) for col in self.__table__.columns)

