from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.task import Task
from app.schemas.task import TaskCreate


def create_task(
    db: Session,
    task_data: TaskCreate,
    project: Project,
) -> Task:

    task = Task(
        title=task_data.title,
        description=task_data.description,
        project_id=project.id,
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task