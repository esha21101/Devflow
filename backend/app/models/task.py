from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.base import BaseModel


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

    project_id: Mapped[str] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    project = relationship(
        "Project",
        back_populates="tasks",
    )