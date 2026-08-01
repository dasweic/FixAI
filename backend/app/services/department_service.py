from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate


def create_department(
    db: Session,
    department: DepartmentCreate
):
    new_department = Department(
        name=department.name,
        description=department.description
    )

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


def get_departments(db: Session):
    return (
        db.query(Department)
        .order_by(Department.id.desc())
        .all()
    )