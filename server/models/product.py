"""
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Product(Base):
    __tablename__ = 'mtt_md_products'

    product_no          = Column(INTEGER, primary_key=True)
    product_id          = Column(String(50), nullable=False, unique=True)
    product_status      = Column(SMALLINT, nullable=False)
    product_name        = Column(String(50), nullable=False)
    product_type        = Column(String(20), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    product_description = Column(TEXT, nullable=True)

    def __init__(self, product_id, product_status, product_name, product_type, 
                product_description=None):
        self.product_id = product_id
        self.product_status = product_status
        self.product_name = product_name
        self.product_type = product_type
        self.product_description = product_description
