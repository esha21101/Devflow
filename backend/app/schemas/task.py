from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID
from app.models.enums import (
    TaskStatus,
    TaskPriority,
)


class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=255,
    )
    description: str | None = Field(
        default=None,
        max_length=1000,
    )
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: datetime | None = None
    
class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )
    description: str | None = Field(
        default=None,
        max_length=1000,
    )
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status: TaskStatus
    priority: TaskPriority
    project_id: UUID
    due_date: datetime | None

    class Config:
        from_attributes = True