from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class ComplaintImage(Base):
    __tablename__ = "complaint_images"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    image_url = Column(
        String(500),
        nullable=False
    )

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id", ondelete="CASCADE"),
        nullable=False
    )

    complaint = relationship(
        "Complaint",
        back_populates="images"
    )