import os
import importlib.util
import pytest


def test_submission_files_exist(developer):
    base_path = f"submissions/developer-{developer}"
    folders = ["tests", "results"]

    for folder in folders:
        assert os.path.exists(
            os.path.join(base_path, folder)
        ), f"{folder.capitalize()} directory does not exist"

        files = os.listdir(os.path.join(base_path, folder))
        assert len(files) > 0, f"No {folder} files found"


def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "status": "not_started",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["status"] == "not_started"
    assert "id" in data


def test_read_tasks(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) > 0


def test_read_task(client):
    # Assuming we have a task with id 1
    response = client.get("/tasks/1")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1


def test_update_task(client):
    # Assuming we have a task with id 1
    response = client.put(
        "/tasks/1",
        json={
            "title": "Updated Task",
            "description": "Updated Description",
            "status": "in_progress",
        },
    )
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == "Updated Task"
    assert updated_task["description"] == "Updated Description"
    assert updated_task["status"] == "in_progress"


def test_delete_task(client):
    # Create a new task to delete
    create_response = client.post(
        "/tasks/",
        json={
            "title": "Task to Delete",
            "description": "To be deleted",
            "status": "not_started",
        },
    )
    assert create_response.status_code == 201
    task_to_delete = create_response.json()

    # Delete the task
    delete_response = client.delete(f"/tasks/{task_to_delete['id']}")
    assert delete_response.status_code == 200
    deleted_task = delete_response.json()
    assert deleted_task["id"] == task_to_delete["id"]

    # Try to get the deleted task
    get_response = client.get(f"/tasks/{task_to_delete['id']}")
    assert get_response.status_code == 404


def test_task_not_found(client):
    response = client.get("/tasks/999999")  # Assuming this ID does not exist
    assert response.status_code == 404


def test_create_board(client):
    response = client.post(
        "/boards/", json={"name": "Test Board", "description": "Test Board Description"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Board"
    assert data["description"] == "Test Board Description"
    assert "id" in data


def test_read_boards(client):
    response = client.get("/boards/")
    assert response.status_code == 200
    boards = response.json()
    assert len(boards) >= 1  # Assuming at least one board has been created


def test_read_board(client):
    # Assuming we have a board with id 1
    response = client.get("/boards/1")
    assert response.status_code == 200
    board = response.json()
    assert board["id"] == 1


def test_update_board(client):
    # Assuming we have a board with id 1
    response = client.put(
        "/boards/1",
        json={"name": "Updated Board", "description": "Updated Board Description"},
    )
    assert response.status_code == 200
    updated_board = response.json()
    assert updated_board["name"] == "Updated Board"
    assert updated_board["description"] == "Updated Board Description"


def test_delete_board(client):
    # Create a new board to delete
    create_response = client.post(
        "/boards/", json={"name": "Board to Delete", "description": "To be deleted"}
    )
    assert create_response.status_code == 201
    board_to_delete = create_response.json()

    # Delete the board
    delete_response = client.delete(f"/boards/{board_to_delete['id']}")
    assert delete_response.status_code == 200
    deleted_board = delete_response.json()
    assert deleted_board["id"] == board_to_delete["id"]

    # Try to get the deleted board
    get_response = client.get(f"/boards/{board_to_delete['id']}")
    assert get_response.status_code == 404


def test_board_not_found(client):
    response = client.get("/boards/999999")  # Assuming this ID does not exist
    assert response.status_code == 404


def test_create_task_with_invalid_data(client):
    # Sending incomplete data that should result in a 422 error
    response = client.post("/tasks/", json={"title": ""})
    assert response.status_code == 422


def test_update_task_with_invalid_data(client):
    # Assuming we have a task with id 1
    # Sending invalid status that should result in a 422 error
    response = client.put("/tasks/1", json={"status": "invalid_status"})
    assert response.status_code == 422


def test_create_board_with_invalid_data(client):
    # Sending incomplete data that should result in a 422 error
    response = client.post("/boards/", json={"name": ""})
    assert response.status_code == 422


def test_update_board_with_invalid_data(client):
    # Assuming we have a board with id 1
    # Sending invalid data that should result in a 422 error
    response = client.put("/boards/1", json={"name": ""})
    assert response.status_code == 422
