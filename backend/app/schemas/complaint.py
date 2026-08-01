from pydantic import BaseModel


class ComplaintCreate(BaseModel):
    title: str
    description: str
    category: str
    location: str
    department_id: int | None = None


class ComplaintResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    location: str
    status: str
    user_id: int
    department_id: int | None = None

    class Config:
        from_attributes = True