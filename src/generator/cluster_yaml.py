import yaml
from pathlib import Path
from src.scheme.cluster.request import ClusterCreateRequest, ClusterDeleteRequest
from src.config import YAML_OUTPUT_DIR


def build_cluster_yaml(req: ClusterCreateRequest) -> str:
    """
    사용자 요청 기반으로 RayCluster CRD YAML 문자열 생성
    """
    data = {
        "apiVersion": "ray.io/v1",
        "kind": "RayCluster",
        "metadata": {
            "name": req.cluster_name,
            "namespace": "default"
        },
        "spec": {
            "rayVersion": "2.9.0",
            "headGroupSpec": {
                "serviceType": "ClusterIP",
                "replicas": 1,
                "template": {
                    "spec": {
                        "containers": [{
                            "name": "ray-head",
                            "image": "rayproject/ray:2.9.0",
                            "resources": {
                                "limits": {"cpu": str(req.num_cpus)}
                            },
                            "args": ["ray", "start", "--head", "--port=6379"]
                        }]
                    }
                }
            },
            "workerGroupSpecs": [{
                "groupName": "ray-workers",
                "replicas": req.num_workers,
                "template": {
                    "spec": {
                        "containers": [{
                            "name": "ray-worker",
                            "image": "rayproject/ray:2.9.0",
                            "args": ["ray", "start", "--address=$(RAY_HEAD_IP):6379"]
                        }]
                    }
                }
            }]
        }
    }

    return yaml.dump(data, sort_keys=False)


def build_cluster_delete_yaml(req: ClusterDeleteRequest) -> str:
    """
    RayCluster 삭제용 YAML 반환
    이후 kubectl delete -f <this.yaml> 로 사용 가능
    """
    data = {
        "apiVersion": "ray.io/v1",
        "kind": "RayCluster",
        "metadata": {
            "name": req.cluster_name,
            "namespace": "default"
        }
    }

    return yaml.dump(data, sort_keys=False)


def build_cluster_delete_command(req: ClusterDeleteRequest) -> str:
    """
    kubectl delete 명령어 형태의 CLI 문자열 생성
    실제 YAML 삭제 대신 수동 명령어 출력용 (옵션 기능)
    """
    return f"kubectl delete raycluster {req.cluster_name} -n default"


def save_cluster_yaml_to_file(req: ClusterCreateRequest) -> str:
    """
    생성된 RayCluster YAML 파일을 저장하고 파일 경로 반환
    """
    yaml_str = build_cluster_yaml(req)
    file_path = Path(YAML_OUTPUT_DIR) / f"{req.cluster_name}.yaml"
    file_path.write_text(yaml_str, encoding="utf-8")
    return str(file_path)


def save_cluster_delete_yaml_to_file(req: ClusterDeleteRequest) -> str:
    """
    삭제용 RayCluster YAML 파일을 저장하고 파일 경로 반환
    """
    yaml_str = build_cluster_delete_yaml(req)
    file_path = Path(YAML_OUTPUT_DIR) / f"{req.cluster_name}-delete.yaml"
    file_path.write_text(yaml_str, encoding="utf-8")
    return str(file_path)
