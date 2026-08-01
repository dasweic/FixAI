from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


def create_notification(
    db: Session,
    notification: NotificationCreate
):

    new_notification = Notification(
        message=notification.message,
        user_id=notification.user_id
    )

    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)

    return new_notification



def get_user_notifications(
    db: Session,
    user_id: int
):

    return (
        db.query(Notification)
        .filter(Notification.user_id == user_id)
        .order_by(Notification.id.desc())
        .all()
    )



def mark_notification_read(
    db: Session,
    notification_id: int
):

    notification = (
        db.query(Notification)
        .filter(Notification.id == notification_id)
        .first()
    )

    if notification is None:
        return None

    notification.is_read = True

    db.commit()
    db.refresh(notification)

    return notification