
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from FastAPI!",
        "version": "v1"
    }


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json()["students"] == [
        "Rahul",
        "Priya",
        "Aishwarya",
        "Arun",
        "Sneha"
    ]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
