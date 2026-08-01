from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.complaint_image import ComplaintImage
from app.models.complaint import Complaint
from app.services.upload_service import upload_complaint_image


router = APIRouter(
    prefix="/upload",
    tags=["Image Upload"]
)


@router.post("/{complaint_id}")
def upload_image(
    complaint_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    complaint = (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )


    image_url = upload_complaint_image(file)


    new_image = ComplaintImage(
        image_url=image_url,
        complaint_id=complaint_id
    )


    db.add(new_image)
    db.commit()
    db.refresh(new_image)


    return {
        "message": "Image uploaded successfully",
        "image_url": image_url
    }