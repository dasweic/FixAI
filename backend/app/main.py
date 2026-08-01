from fastapi import FastAPI

from app.database.init_db import create_tables

from app.routers.auth import router as auth_router
from app.routers.user import router as user_router
from app.routers.complaint import router as complaint_router
from app.routers.department import router as department_router
from app.routers.upload import router as upload_router
from app.routers.notification import router as notification_router
from app.routers.dashboard import router as dashboard_router


app = FastAPI(
    title="FixAI Backend",
    description="AI Powered Smart Campus Complaint Management System",
    version="1.0.0"
)


# Routers
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(complaint_router)
app.include_router(department_router)
app.include_router(upload_router)
app.include_router(notification_router)
app.include_router(dashboard_router)


@app.on_event("startup")
def startup():
    create_tables()


@app.get("/")
def root():
    return {
        "message": "Welcome to FixAI Backend"
    }


@app.get("/health")
def health():
    return {
        "status": "Service Running Successfully"
    }