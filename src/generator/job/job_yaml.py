from typing import Dict, Any
import yaml
from src.scheme.job.request import RayJobCreateRequest
from pathlib import Path
from src.config import YAML_OUTPUT_DIR


def build_job_yaml(req: RayJobCreateRequest) -> str:
    """
    RayJob CRD YAML 문자열을 생성합니다.
    PyYAML을 사용하여 구조적 방식으로 생성하며,
    runtimeEnv는 working_dir, pip_packages가 존재할 경우에만 포함됩니다.
    """

    # 기본 job_spec 정의
    job_spec: Dict[str, Any] = {
        "apiVersion": "ray.io/v1",
        "kind": "RayJob",
        "metadata": {
            "name": req.job_name,
            "namespace": "default"
        },
        "spec": {
            "entrypoint": req.entrypoint,
            "rayClusterConfig": {
                "rayClusterName": req.cluster_name
            }
        }
    }

    # Optional 필드(runtimeEnv)
    runtime_env = {}
    if req.working_dir:
        runtime_env["working_dir"] = req.working_dir
    if req.pip_packages:
        runtime_env["pip"] = req.pip_packages

    if runtime_env:
        job_spec["spec"]["runtimeEnv"] = runtime_env

    # YAML 직렬화 및 반환
    return yaml.dump(job_spec, sort_keys=False)


def save_job_yaml_to_file(req: RayJobCreateRequest) -> str:
    """
    YAML 문자열을 생성하여 지정된 파일로 저장
    반환값은 저장된 파일 경로
    """
    yaml_str = build_job_yaml(req)
    filename = f"{req.job_name}.yaml"
    file_path = Path(YAML_OUTPUT_DIR) / filename

    file_path.write_text(yaml_str, encoding="utf-8")
    return str(file_path)


def build_job_delete_yaml(job_name: str) -> str:
    """
    RayJob 삭제용 YAML 생성
    """
    data = {
        "apiVersion": "ray.io/v1",
        "kind": "RayJob",
        "metadata": {
            "name": job_name,
            "namespace": "default"
        }
    }
    return yaml.dump(data, sort_keys=False)
