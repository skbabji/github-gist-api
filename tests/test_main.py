import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def check_gists_response(response):
    assert response.status_code in (200, 404)
    if response.status_code == 200:
        assert isinstance(response.json(), list)
        for gist in response.json():
            assert "id" in gist
            assert "url" in gist
    else:
        assert response.json()["detail"] == "User not found or no gists."

def test_list_gists_octocat():
    check_gists_response(client.get("/octocat"))

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_list_gists_nonexistent_user():
    check_gists_response(client.get("/thisuserdoesnotexistforsure1234567890"))
