from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import create_engine
import os

engine = create_engine(os.environ.get('DATABASE_URL'))

Base = declarative_base()

class Tax(Base):
    """
    Tax information imported from CSV files
    
    CSV line example: 2011  0144666-1   Brändö Andelshandel     035 BRÄNDÖ  0   -15,66  5369,7  5385,36 0
    """

    __tablename__ = "tax"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    year = Column(String(4), nullable=False, index=True)
    business_id = Column(String(255), index=True, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    municipality = Column(String(255), nullable=False)
    tax_income = Column(Float)
    tax_total = Column(Float)
    tax_advance = Column(Float)
    tax_return = Column(Float)
    tax_residual = Column(Float)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<Tax information (%r) for %r>" % (self.year, self.name)
    
class Ytj(Base):
    """
    Data fetched from YTJ for specific busienss_id
    """
    __tablename__ = "ytj"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    business_id = Column(String(255), index=True, nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return "<Ytj information for %r>" % self.business_id

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()