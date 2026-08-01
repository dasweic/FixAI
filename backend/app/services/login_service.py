from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.security import verify_password


def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    db_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if db_user is None:
        return None

    if not verify_password(password, db_user.password):
        return None

    return db_user