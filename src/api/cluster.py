from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

from src.scheme.cluster.request import ClusterCreateRequest, ClusterDeleteRequest
from src.generator.cluster_yaml import (
    build_cluster_yaml,
    build_cluster_delete_command,
    build_cluster_delete_yaml
)

router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
def generate_cluster_yaml(req: ClusterCreateRequest):
    """
    Cluster 생성용 YAML 반환
    """
    return build_cluster_yaml(req)


@router.post("/delete/command", response_class=PlainTextResponse)
def generate_cluster_delete_command_api(req: ClusterDeleteRequest):
    """
    삭제 명령어 문자열 반환 (kubectl delete raycluster ...)
    """
    return build_cluster_delete_command(req)


@router.post("/delete/yaml", response_class=PlainTextResponse)
def generate_cluster_delete_yaml_api(req: ClusterDeleteRequest):
    """
    RayCluster 삭제용 YAML 반환 (kubectl delete -f this.yaml)
    """
    return build_cluster_delete_yaml(req)
