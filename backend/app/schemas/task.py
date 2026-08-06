from pydantic import BaseModel
from uuid import UUID
from app.models.enums import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.TODO
    
    
class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    status: TaskStatus
    project_id: UUID

    class Config:
        from_attributes = True