import pytest
from fastapi.testclient import TestClient
from src.server import create_app

app = create_app()


@pytest.fixture
def client():
    return TestClient(app)
