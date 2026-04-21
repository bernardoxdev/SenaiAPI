from pydantic import BaseModel

class MaterialBase(BaseModel):
    name: str
    density: float
    strength: float
    hardness: float
    malleability: float
    conductivity: float
    permeability: float

class MaterialCreate(MaterialBase):
    pass

class MaterialResponse(MaterialBase):
    id: int

    class Config:
        from_attributes = True