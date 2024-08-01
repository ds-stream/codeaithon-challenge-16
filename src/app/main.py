from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlmodel import Session, select

from . import database, models, schemas

app = FastAPI()


@app.on_event("startup")
def on_startup():
    database.create_db_and_tables()


@app.post("/tasks/", response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task: schemas.TaskCreate, session: Session = Depends(database.get_session)
):
    db_task = models.Task.from_orm(task)
    if task.board_id:
        board = session.get(models.Board, task.board_id)
        if not board:
            raise HTTPException(status_code=404, detail="Board not found")
        db_task.board_id = task.board_id
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(session: Session = Depends(database.get_session)):
    tasks = session.exec(select(models.Task)).all()
    return tasks


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, session: Session = Depends(database.get_session)):
    task = session.get(models.Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    session: Session = Depends(database.get_session),
):
    task = session.get(models.Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = task_update.dict(exclude_unset=True)

    # Check if board_id is being updated and if it exists
    if "board_id" in task_data:
        board_id = task_data["board_id"]
        if board_id is not None:
            board = session.get(models.Board, board_id)
            if not board:
                raise HTTPException(status_code=404, detail="Board not found")
        task.board_id = board_id  # Assign or unassign the board

    for key, value in task_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.utcnow()
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@app.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, session: Session = Depends(database.get_session)):
    task = session.get(models.Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()
    return task


@app.post("/boards/", response_model=schemas.Board, status_code=status.HTTP_201_CREATED)
def create_board(
    board: schemas.BoardCreate, session: Session = Depends(database.get_session)
):
    db_board = models.Board.from_orm(board)
    session.add(db_board)
    session.commit()
    session.refresh(db_board)
    return db_board


@app.get("/boards/", response_model=List[schemas.Board])
def read_boards(session: Session = Depends(database.get_session)):
    boards = session.exec(select(models.Board)).all()
    return boards


@app.get("/boards/{board_id}", response_model=schemas.Board)
def read_board(board_id: int, session: Session = Depends(database.get_session)):
    board = session.get(models.Board, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    return board


@app.put("/boards/{board_id}", response_model=schemas.Board)
def update_board(
    board_id: int,
    board_update: schemas.BoardUpdate,
    session: Session = Depends(database.get_session),
):
    board = session.get(models.Board, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    board_data = board_update.dict(exclude_unset=True)
    for key, value in board_data.items():
        setattr(board, key, value)
    session.add(board)
    session.commit()
    session.refresh(board)
    return board


@app.delete("/boards/{board_id}", response_model=schemas.Board)
def delete_board(board_id: int, session: Session = Depends(database.get_session)):
    board = session.get(models.Board, board_id)
    if not board:
        raise HTTPException(status_code=404, detail="Board not found")
    session.delete(board)
    session.commit()
    return board
