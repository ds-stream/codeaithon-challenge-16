from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from .models import TaskStatus  # Make sure to import TaskStatus


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.NOT_STARTED  # Use the TaskStatus enum
    board_id: Optional[int] = (
        None  # Allow setting board_id to None to remove from board
    )


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = Field(None)
    status: TaskStatus = Field(
        ...,
    )
    board_id: Optional[int] = (
        None  # Allow setting board_id to None to remove from board
    )


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
    )
    description: Optional[str] = Field(
        None,
    )
    status: Optional[TaskStatus] = Field(
        None,
    )


class TaskInDBBase(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class Task(TaskInDBBase):
    pass


class TaskInDB(TaskInDBBase):
    pass


class BoardBase(BaseModel):
    name: str
    description: Optional[str] = None


class BoardCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
    )
    description: Optional[str] = Field(
        None,
    )


class BoardUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=1,
    )
    description: Optional[str] = Field(
        None,
    )


class BoardInDBBase(BoardBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True


class Board(BoardInDBBase):
    pass


class BoardInDB(BoardInDBBase):
    pass
