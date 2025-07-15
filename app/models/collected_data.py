from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from db.base import Base

class CollectedData(Base):
    __tablename__ = 'collected_data'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    value = Column(Text, nullable=False)
    source = Column(String(50), nullable=False)
    reliability = Column(String(50), nullable=False)
    target = relationship("Target", back_populates="collected_data")
