from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.schemas import MaterialCreate
from backend.models.material import Material
from backend.services.comparison_service import compare_materials
from backend.services.recommendation_service import best_material
from backend.data.seed import MATERIALS

router = APIRouter(prefix="/materiais", tags=["Materiais"])

@router.post("/")
def create_material(
        material: MaterialCreate,
        db: Session = Depends(get_db)
):
    if db.query(Material).count() == 0:
        for m in MATERIALS:
            db_material = Material(**m)
            db.add(db_material)
        db.commit()

    db_material = Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)

    return db_material

@router.get("/")
def list_materials(
        db: Session = Depends(get_db)
):
    if db.query(Material).count() == 0:
        for m in MATERIALS:
            db_material = Material(**m)
            db.add(db_material)
        db.commit()

    return db.query(Material).all()

@router.post("/compare")
def compare(
        m1_id: int,
        m2_id: int,
        db: Session = Depends(get_db)
):
    if db.query(Material).count() == 0:
        for m in MATERIALS:
            db_material = Material(**m)
            db.add(db_material)
        db.commit()

    m1 = db.query(Material).get(m1_id)
    m2 = db.query(Material).get(m2_id)
    return compare_materials(m1, m2)

@router.get("/recommend")
def recommend(
        db: Session = Depends(get_db)
):
    if db.query(Material).count() == 0:
        for m in MATERIALS:
            db_material = Material(**m)
            db.add(db_material)
        db.commit()

    materials = db.query(Material).all()
    return best_material(materials)

if __name__ == '__main__':
    pass