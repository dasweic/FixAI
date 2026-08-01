from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    message = Column(
        String(255),
        nullable=False
    )

    is_read = Column(
        Boolean,
        default=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    # Relationship with User
    user = relationship(
        "User",
        back_populates="notifications"
    )