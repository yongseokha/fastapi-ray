import yaml
from src.scheme.cluster.request import ClusterCreateRequest, ClusterDeleteRequest

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

    # YAML 포맷 문자열로 반환
    return yaml.dump(data, sort_keys=False)

def build_cluster_delete_command(req: ClusterDeleteRequest) -> str:
    """
    주어진 클러스터 이름으로 kubectl delete 명령 생성
    실제로는 kubectl apply --yaml 처럼, 향후 이 명령 실행 또는 API 전송으로 확장 가능
    """
    return f"kubectl delete raycluster {req.cluster_name} -n default"

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
