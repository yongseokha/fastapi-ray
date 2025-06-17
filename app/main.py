from fastapi import FastAPI
from app.api import admin, user

app = FastAPI(title="Ray 관리 플랫폼")

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(user.router, prefix="/user", tags=["user"])