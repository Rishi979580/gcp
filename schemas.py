from pydantic import BaseModel, EmailStr

class EnrollRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str
    course: str
