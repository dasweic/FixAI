from app.database.connection import engine
from app.database.base import Base

from app.models.user import User
from app.models.complaint import Complaint
from app.models.department import Department
from app.models.complaint_image import ComplaintImage


def create_tables():
    Base.metadata.create_all(bind=engine)