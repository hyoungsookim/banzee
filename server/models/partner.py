"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
#from sqlalchemy.ext.declarative import declarative_base

from server.utils import *
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
        self.created_at = get_current_datetime_str()
        self.updated_at = get_current_datetime_str()


    #def __repr__(self):
    #    return "<{0} partner_id: {1}, partner_status: {2}, partner_name: {3}, created_at: {4}, updated_at:{5}>".\
    #        format(self.__class__.name, self.partner_id, self.partner_status, self.partner_name, str(self.created_at), str(self.updated_at))

    def to_dict(self, output_attrs=None):
        """Returns the model attributes as a dict
        :output_attrs: list that includes attributes to convert
        """
        if output_attrs:
            return {col.name: getattr(self, col.name) 
                        for col in self.__table__.columns 
                            if col.name in output_attrs}

        return {col.name: getattr(self, col.name) 
                    for col in self.__table__.columns}

