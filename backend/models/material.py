from sqlalchemy import Column, Integer, String, Float
from backend.core.database import Base

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    density = Column(Float)
    strength = Column(Float)
    hardness = Column(Float)
    malleability = Column(Float)
    conductivity = Column(Float)
    permeability = Column(Float)