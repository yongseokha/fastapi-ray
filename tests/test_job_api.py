import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from src.server import create_app

client = TestClient(create_app())


@pytest.fixture
def mock_job_response():
    return {
        "jobs": [
            {
                "job_id": "abcd1234",
                "status": "SUCCEEDED",
                "metadata": {"name": "train-job"},
                "message": "Job completed",
                "start_time": "2025-06-20T10:00:00Z"
            }
        ]
    }


@patch("src.api.job.get_ray_jobs", new_callable=AsyncMock)
def test_get_job_status_success(mock_get_jobs, mock_job_response):
    mock_get_jobs.return_value = mock_job_response

    response = client.get("/job/status/train-job")
    assert response.status_code == 200
    assert response.json()["status"] == "SUCCEEDED"
    assert response.json()["job_id"] == "abcd1234"


@patch("src.api.job.get_ray_jobs", new_callable=AsyncMock)
def test_get_job_status_not_found(mock_get_jobs):
    mock_get_jobs.return_value = {"jobs": []}

    response = client.get("/job/status/unknown-job")
    assert response.status_code == 404
    assert response.json()["detail"] == "Job not found"


@patch("src.api.job.get_ray_jobs", new_callable=AsyncMock)
def test_get_job_status_server_error(mock_get_jobs):
    mock_get_jobs.side_effect = Exception("Dashboard not reachable")

    response = client.get("/job/status/train-job")
    assert response.status_code == 500
    assert "Dashboard not reachable" in response.json()["detail"]
