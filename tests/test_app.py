import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_get_tasks(client):
    res = client.get("/api/tasks")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_add_task(client):
    res = client.post("/api/tasks",
                      json={"title": "Test Task"},
                      content_type="application/json")
    assert res.status_code == 201
    assert res.get_json()["title"] == "Test Task"