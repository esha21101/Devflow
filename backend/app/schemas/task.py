from pydantic import BaseModel
from uuid import UUID


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    project_id: UUID

    class Config:
        from_attributes = True