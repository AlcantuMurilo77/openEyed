from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from db.base import Base

class Target(Base):
    __tablename__ = 'target'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nulable=True)
    email = Column(String(150), nullable=True, unique=False)
    phone = Column(String(20), nullable=True)
    domains = Column(JSON, nullable=True)
    usernames = Column(JSON, nullable=True)
    notes = Column(Text, nullable=True)
    cnpj = Column(String(14), nullable=True)
    cpf = Column(String(11), nullable=True)

    results = relationship("SearchResults", back_populates="targets")