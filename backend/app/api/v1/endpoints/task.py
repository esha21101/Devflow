from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models.user import User
from app.models.enums import (
    TaskStatus,
    TaskPriority,
    TaskSortBy,
    SortOrder,
)
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse,
)
from app.services.project import get_project
from app.services.task import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
)

router = APIRouter(
    prefix="/projects",
    tags=["Tasks"],
)

task_router = APIRouter(
    prefix="/tasks",
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
    status: TaskStatus | None = None,
    priority: TaskPriority | None = None,
    search: str | None = None,
    sort_by: TaskSortBy = TaskSortBy.CREATED_AT,
    sort_order: SortOrder = SortOrder.DESC,
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
        status,
        priority,
        search,
        sort_by,
        sort_order,
    )
    
@task_router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
def get_task_by_id(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    task = get_task(
        db,
        task_id,
        current_user,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task

@task_router.patch(
    "/{task_id}",
    response_model=TaskResponse,
)
def update_task_by_id(
    task_id: UUID,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    task = get_task(
        db,
        task_id,
        current_user,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return update_task(
        db,
        task,
        task_data,
    )
    
@task_router.delete(
    "/{task_id}",
    status_code=204,
)
def delete_task_by_id(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    task = get_task(
        db,
        task_id,
        current_user,
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    delete_task(
        db,
        task,
    )