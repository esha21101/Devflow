from uuid import UUID
from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.task import Task
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
)
from sqlalchemy import select
from app.models.user import User
from app.models.enums import (
    TaskStatus,
    TaskPriority,
)


def create_task(
    db: Session,
    task_data: TaskCreate,
    project: Project,
) -> Task:

    task = Task(
    title=task_data.title,
    description=task_data.description,
    status=task_data.status,
    priority=task_data.priority,
    due_date=task_data.due_date,
    project_id=project.id,
)

    db.add(task)

    db.commit()

    db.refresh(task)

    return task

def get_tasks(
    db: Session,
    project: Project,
    status: TaskStatus | None = None,
    priority: TaskPriority | None = None,
    search: str | None = None,
) -> list[Task]:

    query = select(Task).where(
        Task.project_id == project.id
    )

    if status is not None:
        query = query.where(
            Task.status == status
        )

    if priority is not None:
        query = query.where(
            Task.priority == priority
        )

    if search:
        search_pattern = f"%{search}%"

        query = query.where(
            Task.title.ilike(search_pattern)
            | Task.description.ilike(search_pattern)
        )

    tasks = db.scalars(query).all()

    return tasks

def get_task(
    db: Session,
    task_id: UUID,
    current_user: User,
) -> Task | None:

    task = db.scalar(
        select(Task)
        .join(Project)
        .where(
            Task.id == task_id,
            Project.owner_id == current_user.id,
        )
    )

    return task

def update_task(
    db: Session,
    task: Task,
    task_data: TaskUpdate,
) -> Task:

    update_data = task_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            task,
            key,
            value,
        )

    db.commit()

    db.refresh(task)

    return task

def delete_task(
    db: Session,
    task: Task,
) -> None:

    db.delete(task)

    db.commit()