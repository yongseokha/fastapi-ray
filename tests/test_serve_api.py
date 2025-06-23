import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from src.server import create_app

client = TestClient(create_app())


@pytest.fixture
def test_payload():
    return {
        "app_name": "test-serve-app",
        "import_path": "my_app.entrypoint:app",
        "route_prefix": "/test",
        "deployments": [
            {"name": "model-deploy", "num_replicas": 2}
        ]
    }


def test_generate_serve_yaml(test_payload):
    response = client.post("/serve/yaml", json=test_payload)
    assert response.status_code == 200
    assert "apiVersion: serve.ray.io/v1" in response.text
    assert f"name: {test_payload['app_name']}" in response.text


@patch("src.api.serve.save_serve_yaml_to_file")
def test_save_serve_yaml(mock_save, test_payload):
    mock_save.return_value = f"/tmp/{test_payload['app_name']}.yaml"

    response = client.post("/serve/yaml/save", json=test_payload)
    assert response.status_code == 200
    assert response.json()["message"] == "YAML saved successfully"
    assert test_payload["app_name"] in response.json()["path"]


@patch("src.api.serve.Path.exists")
@patch("src.api.serve.FileResponse")
def test_download_serve_yaml_success(mock_file_response, mock_exists):
    mock_exists.return_value = True
    mock_file_response.return_value = "dummy-file-response"

    response = client.get("/serve/yaml/download/test-serve-app")
    assert response.status_code == 200 or response == "dummy-file-response"


@patch("src.api.serve.Path.exists")
def test_download_serve_yaml_not_found(mock_exists):
    mock_exists.return_value = False
    response = client.get("/serve/yaml/download/not-found-app")
    assert response.status_code == 404
    assert response.json()["detail"] == "YAML file not found"


