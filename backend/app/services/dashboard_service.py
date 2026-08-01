from sqlalchemy.orm import Session

from app.models.complaint import Complaint


def get_dashboard_stats(db: Session):
    total = db.query(Complaint).count()

    pending = (
        db.query(Complaint)
        .filter(Complaint.status == "Pending")
        .count()
    )

    resolved = (
        db.query(Complaint)
        .filter(Complaint.status == "Resolved")
        .count()
    )

    in_progress = (
        db.query(Complaint)
        .filter(Complaint.status == "In Progress")
        .count()
    )

    return {
        "total_complaints": total,
        "pending": pending,
        "in_progress": in_progress,
        "resolved": resolved
    }