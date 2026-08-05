from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.task import Task
from app.schemas.task import TaskCreate
from sqlalchemy import select


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

def get_tasks(
    db: Session,
    project: Project,
) -> list[Task]:

    tasks = db.scalars(
        select(Task).where(
            Task.project_id == project.id
        )
    ).all()

    return tasks