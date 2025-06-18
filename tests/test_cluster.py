def test_deploy_cluster(client):
    """
    클러스터 배포 API 정상 동작 여부 테스트
    """
    response = client.post(
        "/cluster/deploy",
        json={"num_cpus": 2, "num_gpus": 0},
        headers={"x-user": "soyoung"}
    )
    assert response.status_code == 200
    assert "Cluster deployed" in response.json()["message"]


def test_stop_cluster(client):
    """
    클러스터 중지 API 정상 동작 여부 테스트
    """
    response = client.post("/cluster/stop", headers={"x-user": "soyoung"})
    assert response.status_code == 200
    assert "Ray cluster stopped" in response.json()["message"]
