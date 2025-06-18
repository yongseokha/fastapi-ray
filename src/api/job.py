from fastapi import APIRouter
from src.scheme.job import JobSubmitRequest
from src.utils.ray_api import ray_post, ray_get

router = APIRouter(prefix="/job", tags=["Job"])

@router.post("/submit")
def submit_job(request: JobSubmitRequest):
    """
    [Ray Job 제출 API]
    - Job 사양(JSON)을 받아 Ray Dashboard API로 전달
    """
    response = ray_post("/api/jobs/", request.dict())
    return response.json()

@router.get("/status/{job_id}")
def job_status(job_id: str):
    """
    [Job 상태 조회 API]
    - Job ID로 실행 상태를 조회
    """
    return ray_get(f"/api/jobs/{job_id}").json()
