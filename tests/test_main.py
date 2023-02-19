from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/items/0")
    assert response.status_code == 200