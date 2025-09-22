from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, repository
from app.services import agent_service
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.post("/chat/{file_id}")
async def handle_chat(
    file_id: int,
    query: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_file = repository.crud_file.get(db, file_id)
    if not db_file or db_file.owner_id != current_user.id:
        raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다.")
    
    file_path = db_file.file_path

    answer = agent_service.excel_agent(file_path, query)

    return {"answer": answer}