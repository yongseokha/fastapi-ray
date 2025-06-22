import yaml
from pathlib import Path
from src.scheme.serve.request import ServeAppCreateRequest
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
    Serve YAML 파일을 저장하고 파일 경로를 반환
    """
    yaml_str = build_serve_yaml(req)
    file_path = Path(YAML_OUTPUT_DIR) / f"{req.app_name}.yaml"
    file_path.write_text(yaml_str, encoding="utf-8")
    return str(file_path)
