from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from db.base import Base

class ColectedData(Base):
    __tablename__ = 'colected_data'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    value = Column(Text, nullable=False)
    source = Column(String(50), nullable=False)
    reliability = Column(String(50), nullable=False)
