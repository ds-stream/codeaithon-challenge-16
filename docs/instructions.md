# codeaithon-challenge-16

An instruction for codeaithon challenge 16 - Task Management Application

## Short Description

In this challenge, you will demonstrate your ability to develop a RESTful API using FastAPI and SQLModel. Your objective is to create a robust backend service that empowers users to efficiently manage tasks and organize them into customizable boards.

Your Mission
Build an API that offers the following core features:

- **Task Management**: Implement CRUD operations (Create, Read, Update, Delete) for tasks, allowing users to manage their to-do items.
- **Board Management**: Enable users to create, view, update, and delete boards, which serve as containers for related tasks.
- **Task Assignment**: Provide functionality for users to assign tasks to specific boards or remove them, helping organize tasks logically.

## Project Structure

- `main.py`: The entry point of your application containing the API endpoints.
- `models.py`: Definitions of SQLModel entities for tasks and boards.
- `schemas.py`: Pydantic schemas for request and response models.
- `database.py`: Database session management and configuration.

## Task Model

Your task model should include the following fields:

- `id`: An auto-incrementing integer that serves as the primary key.
- `title`: A string representing the task's title.
- `description`: An optional string for the task's description.
- `status`: An enumeration with values `not_started`, `in_progress`, `done`, and `closed`.
- `board_id`: An optional integer that references a board's ID.
- `created_at`: A datetime indicating when the task was created.
- `updated_at`: An optional datetime indicating when the task was last updated.

Example JSON schema for a task:

```json
{
  "id": 1,
  "title": "Implement authentication",
  "description": "Add user authentication to the application",
  "status": "in_progress",
  "board_id": null,
  "created_at": "2023-04-01T12:00:00Z",
  "updated_at": "2023-04-02T15:30:00Z"
}
```

## Board Model

Your board model should include the following fields:

- `id`: An auto-incrementing integer that serves as the primary key.
- `name`: A string representing the board's name.
- `description`: An optional string for the board's description.
- `tasks`: A list of tasks associated with the board.

Example JSON schema for a board:

```json
{
  "id": 1,
  "name": "Backend Development",
  "description": "Tasks related to backend development",
  "tasks": [
    {
      "id": 1,
      "title": "Implement authentication",
      "description": "Add user authentication to the application",
      "status": "in_progress",
      "board_id": 1,
      "created_at": "2023-04-01T12:00:00Z",
      "updated_at": "2023-04-02T15:30:00Z"
    }
  ]
}
```

## API Endpoints

You should implement the following endpoints:

- `POST /tasks/`: Create a new task.
- `GET /tasks/`: Retrieve all tasks.
- `GET /tasks/{task_id}`: Retrieve a task by ID.
- `PUT /tasks/{task_id}`: Update a task by ID.
- `DELETE /tasks/{task_id}`: Delete a task by ID.
- `POST /boards/`: Create a new board.
- `GET /boards/`: Retrieve all boards.
- `GET /boards/{board_id}`: Retrieve a board by ID.
- `PUT /boards/{board_id}`: Update a board by ID.
- `DELETE /boards/{board_id}`: Delete a board by ID.

Each endpoint should handle the appropriate HTTP status codes, including but not limited to:

- `200 OK`: The request was successful.
- `201 Created`: A new resource was successfully created.
- `422 Unprocessed Entity`: The server cannot process the request due to data validation.
- `404 Not Found`: The requested resource was not found.

## Running the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```
