import pytest

def test_deploy_serve(client):
    """
    /serve/deploy API 테스트
    - Serve 애플리케이션을 배포 요청
    """
    deployment = {
        "name": "test-app",
        "import_path": "my_app.module:App",
        "route_prefix": "/test",
        "runtime_env": {
            "pip": ["fastapi"]
        }
    }
    response = client.post("/serve/deploy", json=deployment)
    assert response.status_code in (200, 400)

def test_list_apps(client):
    """
    /serve/apps API 테스트
    - 현재 배포된 앱 목록 조회
    """
    response = client.get("/serve/apps")
    assert response.status_code == 200

def test_delete_app(client):
    """
    /serve/delete/{app_name} API 테스트
    - 테스트 앱 삭제 요청
    """
    response = client.delete("/serve/delete/test-app")
    assert response.status_code in (200, 404)
