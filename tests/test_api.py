
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello from FastAPI!"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert "Aishwarya" in response.json()["students"]
