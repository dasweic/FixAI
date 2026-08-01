from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(500),
        nullable=False
    )

    category = Column(
        String(100),
        nullable=False
    )

    location = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(50),
        default="Pending"
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=True
    )

    # Relationship with User
    user = relationship(
        "User",
        back_populates="complaints"
    )

    # Relationship with Complaint Images
    images = relationship(
        "ComplaintImage",
        back_populates="complaint",
        cascade="all, delete-orphan"
    )