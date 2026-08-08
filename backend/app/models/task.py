from datetime import datetime
from sqlalchemy import (
    String,
    ForeignKey,
    Enum,
    DateTime,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.base import BaseModel
from app.models.enums import (
    TaskStatus,
    TaskPriority,
)



class Task(Base, BaseModel):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )
    
    status: Mapped[TaskStatus] = mapped_column(
    Enum(TaskStatus),
    default=TaskStatus.TODO,
    nullable=False,
    )

    priority: Mapped[TaskPriority] = mapped_column(
    Enum(TaskPriority),
    default=TaskPriority.MEDIUM,
    nullable=False,
    )
    
    due_date: Mapped[datetime | None] = mapped_column(
    DateTime(timezone=True),
    nullable=True,
    )

    project_id: Mapped[str] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    project = relationship(
        "Project",
        back_populates="tasks",
    )