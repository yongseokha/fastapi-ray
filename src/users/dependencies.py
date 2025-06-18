from fastapi import HTTPException, status

# 테스트를 위해 무조건 통과하는 더미 권한 검사 함수
def verify_permission(action: str):
    def checker():
        # 향후 여기서 사용자 권한 체크 로직을 넣을 수 있음
        allowed_actions = ["deploy_cluster", "submit_job"]
        if action not in allowed_actions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"허용되지 않은 작업: {action}"
            )
        return True
    return checker
