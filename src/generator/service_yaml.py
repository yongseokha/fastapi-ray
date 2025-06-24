import yaml
from src.scheme.service.request import ServiceCreateRequest


def build_service_yaml(req: ServiceCreateRequest) -> str:
    """
    Jupyter, VSCode 등의 Service YAML 생성
    """
    image_map = {
        "jupyter": "jupyter/base-notebook",
        "vscode": "codercom/code-server",
        "app": "nginx"
    }

    data = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": req.name,
            "namespace": "default",
            "labels": {
                "app": req.name
            }
        },
        "spec": {
            "containers": [{
                "name": req.name,
                "image": image_map[req.service_type],
                "ports": [{"containerPort": 8888}]
            }]
        }
    }

    return yaml.dump(data, sort_keys=False)


def create_service_yaml(service_name: str, cluster_name: str) -> str:
    """
    간단한 Service YAML 템플릿 생성 예시
    실제로는 각 타입별 상세 스펙이 다를 수 있음
    """
    return f"""
            apiVersion: v1
            kind: Service
            metadata:
              name: {service_name}
              namespace: default
            spec:
              selector:
                rayClusterName: {cluster_name}
              ports:
                - protocol: TCP
                  port: 80
                  targetPort: 8000
              type: ClusterIP
            """
