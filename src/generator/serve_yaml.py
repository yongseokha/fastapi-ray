import yaml
from src.scheme.serve.request import ServeAppCreateRequest
from pathlib import Path
from src.config import YAML_OUTPUT_DIR


def build_serve_yaml(req: ServeAppCreateRequest) -> str:
    """
    ServeApplication CRD YAML 생성
    """
    data = {
        "apiVersion": "serve.ray.io/v1",
        "kind": "ServeApplication",
        "metadata": {
            "name": req.app_name
        },
        "spec": {
            "import_path": req.import_path,
            "route_prefix": req.route_prefix,
            "runtime_env": {},
            "deployments": [
                {
                    "name": d.name,
                    "num_replicas": d.num_replicas
                } for d in req.deployments
            ]
        }
    }
    return yaml.dump(data, sort_keys=False)


def save_serve_yaml_to_file(req: ServeAppCreateRequest) -> str:
    """
    Serve YAML 파일 저장
    """
    yaml_str = build_serve_yaml(req)
    file_path = Path(YAML_OUTPUT_DIR) / f"{req.app_name}.yaml"
    file_path.write_text(yaml_str, encoding="utf-8")
    return str(file_path)


def build_serve_delete_yaml(app_name: str) -> str:
    """
    ServeApplication 삭제용 YAML 생성
    """
    data = {
        "apiVersion": "serve.ray.io/v1",
        "kind": "ServeApplication",
        "metadata": {
            "name": app_name,
            "namespace": "default"
        }
    }
    return yaml.dump(data, sort_keys=False)


def save_serve_delete_yaml_to_file(app_name: str) -> str:
    """
    삭제용 Serve YAML 파일 저장
    """
    yaml_str = build_serve_delete_yaml(app_name)
    file_path = Path(YAML_OUTPUT_DIR) / f"{app_name}-delete.yaml"
    file_path.write_text(yaml_str, encoding="utf-8")
    return str(file_path)


def build_serve_delete_yaml(app_name: str) -> str:
    """
    Serve 앱 삭제용 YAML 생성
    """
    data = {
        "apiVersion": "serve.ray.io/v1",
        "kind": "ServeApplication",
        "metadata": {
            "name": app_name,
            "namespace": "default"
        }
    }
    return yaml.dump(data, sort_keys=False)
