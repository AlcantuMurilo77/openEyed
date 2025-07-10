from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from db.base import Base


class DataSource:
    __tablename__ = 'data_source'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    base_url = Column(String(100), nullable=False)

    name: str
    type: str
    base_url: str