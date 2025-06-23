import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_generate_cluster_yaml():
    payload = {
        "cluster_name": "ray-test",
        "cluster_type": "private",
        "num_cpus": 2,
        "num_workers": 1
    }
    response = client.post("/cluster/yaml", json=payload)
    assert response.status_code == 200
    assert "kind: RayCluster" in response.text
    assert "rayVersion: 2.9.0" in response.text


def test_save_cluster_yaml():
    payload = {
        "cluster_name": "ray-save-test",
        "cluster_type": "private",
        "num_cpus": 1,
        "num_workers": 0
    }
    response = client.post("/cluster/yaml/save", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "YAML saved successfully" in data["message"]
    assert data["path"].endswith("ray-save-test.yaml")


def test_generate_cluster_delete_yaml():
    payload = {"cluster_name": "ray-delete"}
    response = client.post("/cluster/yaml/delete", json=payload)
    assert response.status_code == 200
    assert "kind: RayCluster" in response.text
    assert "name: ray-delete" in response.text


def test_save_cluster_delete_yaml():
    payload = {"cluster_name": "ray-delete"}
    response = client.post("/cluster/yaml/delete/save", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "YAML saved successfully" in data["message"]
    assert data["path"].endswith("ray-delete-delete.yaml")
