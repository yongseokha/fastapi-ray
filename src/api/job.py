from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse, JSONResponse, FileResponse
from src.generator.job.job_yaml import build_job_yaml, save_job_yaml_to_file, build_job_delete_yaml
from src.scheme.job.request import RayJobCreateRequest
from pathlib import Path
from src.config import YAML_OUTPUT_DIR
from src.utils.ray_api import get_ray_jobs

router = APIRouter()


@router.post("/yaml", response_class=PlainTextResponse)
async def generate_job_yaml(req: RayJobCreateRequest):
    """
    RayJob YAML 생성 API
    """
    yaml_text = build_job_yaml(req)
    return yaml_text


@router.post("/yaml/save")
async def save_job_yaml(req: RayJobCreateRequest):
    """
    Ray Job YAML 파일을 서버에 저장합니다.
    저장된 파일 경로를 반환합니다.
    """
    file_path = save_job_yaml_to_file(req)
    return JSONResponse(content={"message": "YAML saved successfully", "path": file_path})


@router.get("/yaml/download/{job_name}", response_class=FileResponse)
async def download_job_yaml(job_name: str):
    """
    생성된 Ray Job YAML 파일을 다운로드합니다.
    """
    file_path = Path(YAML_OUTPUT_DIR) / f"{job_name}.yaml"

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="YAML file not found")

    return FileResponse(
        path=file_path,
        filename=f"{job_name}.yaml",
        media_type="application/x-yaml"
    )


@router.get("/status/{job_name}")
async def get_job_status(job_name: str):
    """
    특정 Ray Job 상태 조회
    """
    try:
        jobs = await get_ray_jobs()

        # ✅ jobs가 None이면 {}로 대체
        job_list = (jobs or {}).get("jobs", [])

        # ✅ 이름 기준으로 매칭된 Job 찾기
        matched = next((j for j in job_list if j["metadata"]["name"] == job_name), None)

        # ✅ 매칭 실패 시 404 응답
        if not matched:
            raise HTTPException(status_code=404, detail="Job not found")

        # ✅ 매칭된 Job 반환
        return JSONResponse(content=matched)

    except HTTPException:
        raise  # HTTPException은 그대로 다시 raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")



@router.post("/yaml/delete", response_class=PlainTextResponse)
async def generate_job_delete_yaml(job_name: str):
    """
    RayJob 삭제용 YAML 반환
    """
    return build_job_delete_yaml(job_name)


