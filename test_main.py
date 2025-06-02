from fastapi.testclient import TestClient
from main import app, todos

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"name": "Test Todo", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Todo", "completed": False}

def test_get_todos():
    # Ensure the todos list is not empty after creating a todo
    client.post("/todos/", json={"name": "Test Todo 2", "completed": True})
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_todo():
    client.post("/todos/", json={"name": "Test Todo 3", "completed": False})
    response = client.get("/todos/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Todo 3", "completed": False}

def test_get_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

def test_update_todo():
    client.post("/todos/", json={"name": "Test Todo 4", "completed": False})
    response = client.put("/todos/0", json={"name": "Updated Todo", "completed": True})
    assert response.status_code == 200
    assert response.json() == {"name": "Updated Todo", "completed": True}

def test_update_todo_not_found():
    response = client.put("/todos/999", json={"name": "Non-existent Todo", "completed": True})
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

def test_delete_todo():
    client.post("/todos/", json={"name": "Test Todo 5", "completed": False})
    response = client.delete("/todos/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Test Todo 5", "completed": False}

def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}