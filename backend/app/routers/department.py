from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.schemas.department import DepartmentCreate
from app.services.department_service import (
    create_department,
    get_departments
)


router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post("/")
def add_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department(
        db,
        department
    )


@router.get("/")
def list_departments(
    db: Session = Depends(get_db)
):
    return get_departments(db)