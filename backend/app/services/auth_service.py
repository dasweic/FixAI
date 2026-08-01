
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password


def create_user(db: Session, user: UserCreate):
    # Email already exists?
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return None

    # Hash password
    hashed_password = hash_password(user.password)

    # Create user object
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password=hashed_password,
        role="Student",
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user