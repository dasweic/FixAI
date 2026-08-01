from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.complaint import Complaint
from app.models.user import User
from app.models.notification import Notification
from app.schemas.complaint import ComplaintCreate


def create_complaint(
    db: Session,
    complaint: ComplaintCreate,
    current_user: User
):

    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        category=complaint.category,
        location=complaint.location,
        department_id=complaint.department_id,
        status="Pending",
        user_id=current_user.id
    )

    # Save complaint
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    # Create notification
    notification = Notification(
        message="Your complaint has been created successfully",
        user_id=current_user.id
    )

    db.add(notification)
    db.commit()

    return new_complaint


def get_my_complaints(
    db: Session,
    current_user: User
):
    return (
        db.query(Complaint)
        .filter(Complaint.user_id == current_user.id)
        .order_by(Complaint.id.desc())
        .all()
    )


def get_all_complaints(
    db: Session
):
    return (
        db.query(Complaint)
        .order_by(Complaint.id.desc())
        .all()
    )


def update_complaint_status(
    db: Session,
    complaint_id: int,
    status: str
):

    complaint = (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )

    if complaint is None:
        return None

    complaint.status = status

    db.commit()
    db.refresh(complaint)

    # Status change notification
    notification = Notification(
        message=f"Your complaint status changed to {status}",
        user_id=complaint.user_id
    )

    db.add(notification)
    db.commit()

    return complaint


def delete_complaint(
    db: Session,
    complaint_id: int
):

    complaint = (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )

    if complaint is None:
        return False

    db.delete(complaint)
    db.commit()

    return True


def search_complaints(
    db: Session,
    keyword: str = "",
    status: str = "",
    category: str = ""
):
    query = db.query(Complaint)

    if keyword:
        query = query.filter(
            or_(
                Complaint.title.ilike(f"%{keyword}%"),
                Complaint.description.ilike(f"%{keyword}%"),
                Complaint.location.ilike(f"%{keyword}%")
            )
        )

    if status:
        query = query.filter(
            Complaint.status == status
        )

    if category:
        query = query.filter(
            Complaint.category == category
        )

    return (
        query.order_by(Complaint.id.desc())
        .all()
    )