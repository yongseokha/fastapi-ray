import pytest
from fastapi.testclient import TestClient
from src.server import create_app

@pytest.fixture(scope="module")
def client():
    app = create_app()
    return TestClient(app)
