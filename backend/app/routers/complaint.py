from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.role import admin_required

from app.models.user import User
from app.schemas.complaint import ComplaintCreate

from app.services.complaint_service import (
    create_complaint,
    get_my_complaints,
    get_all_complaints,
    update_complaint_status,
    delete_complaint,
    search_complaints
)

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)


@router.post("/")
def create_new_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_complaint = create_complaint(
        db=db,
        complaint=complaint,
        current_user=current_user
    )

    return {
        "message": "Complaint created successfully",
        "complaint_id": new_complaint.id,
        "status": new_complaint.status
    }


@router.get("/my")
def my_complaints(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_my_complaints(db, current_user)


@router.get("/all")
def all_complaints(
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    return get_all_complaints(db)


@router.get("/search")
def search(
    keyword: str = Query(default=""),
    status: str = Query(default=""),
    category: str = Query(default=""),
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    return search_complaints(
        db=db,
        keyword=keyword,
        status=status,
        category=category
    )


@router.patch("/{complaint_id}")
def update_status(
    complaint_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    complaint = update_complaint_status(
        db,
        complaint_id,
        status
    )

    if complaint is None:
        return {
            "message": "Complaint not found"
        }

    return {
        "message": "Complaint status updated successfully",
        "status": complaint.status
    }


@router.delete("/{complaint_id}")
def delete_existing_complaint(
    complaint_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    deleted = delete_complaint(
        db,
        complaint_id
    )

    if not deleted:
        return {
            "message": "Complaint not found"
        }

    return {
        "message": "Complaint deleted successfully"
    }