from fastapi import status
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

url = "http://127.0.0.1:8000"


def test_healthcheck():
    response = client.get(url + "/accounts/v1/healthcheck")
    assert response.status_code == status.HTTP_200_OK
