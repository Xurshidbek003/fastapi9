from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float
from database import Base


class Elonlar(Base):

    __tablename__ = 'elonlar'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(Boolean, nullable=False)










