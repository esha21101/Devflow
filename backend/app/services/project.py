from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate
from sqlalchemy import select


def create_project(
    db: Session,
    project_data: ProjectCreate,
    current_user: User,
) -> Project:

    project = Project(
        name=project_data.name,
        description=project_data.description,
        owner_id=current_user.id,
    )

    db.add(project)

    db.commit()

    db.refresh(project)

    return project

def get_projects(
    db: Session,
    current_user: User,
):

    projects = db.scalars(
        select(Project).where(
            Project.owner_id == current_user.id
        )
    ).all()

    return projects

def get_project(
    db: Session,
    project_id: str,
    current_user: User,
):

    project = db.scalar(
        select(Project).where(
            Project.id == project_id,
            Project.owner_id == current_user.id,
        )
    )

    return project

def update_project(
    db: Session,
    project: Project,
    project_data: ProjectUpdate,
) -> Project:

    if project_data.name is not None:
        project.name = project_data.name

    if project_data.description is not None:
        project.description = project_data.description

    db.commit()

    db.refresh(project)

    return project