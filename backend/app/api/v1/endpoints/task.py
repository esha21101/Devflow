from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models.user import User
from app.schemas.task import TaskCreate, TaskResponse
from app.services.project import get_project
from app.services.task import (
    create_task,
    get_tasks,
)

router = APIRouter(
    prefix="/projects",
    tags=["Tasks"],
)


@router.post(
    "/{project_id}/tasks",
    response_model=TaskResponse,
)
def create_new_task(
    project_id: UUID,
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = get_project(
        db,
        project_id,
        current_user,
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return create_task(
        db,
        task,
        project,
    )
    
@router.get(
    "/{project_id}/tasks",
    response_model=list[TaskResponse],
)
def list_tasks(
    project_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    project = get_project(
        db,
        project_id,
        current_user,
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return get_tasks(
        db,
        project,
    )