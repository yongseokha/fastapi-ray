import httpx

RAY_DASHBOARD_API = "http://127.0.0.1:8265/api"


async def get_ray_jobs():
    """
    Ray Dashboard에서 전체 Job 목록 조회
    """
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{RAY_DASHBOARD_API}/jobs")
        resp.raise_for_status()
        return resp.json()
