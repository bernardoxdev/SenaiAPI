from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.core.database import get_db
from backend.models.material import Material
from backend.services.ai_service import ask_ai

router = APIRouter(prefix="/ia", tags=["Agente de IA"])

@router.post("/ask")
def ask(question: str, db: Session = Depends(get_db)):
    materials = db.query(Material).all()
    answer = ask_ai(question, materials)
    return {"answer": answer}

if __name__ == '__main__':
    pass