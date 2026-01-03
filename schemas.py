from pydantic import BaseModel, EmailStr

class EnrollRequest(BaseModel):
    name: str
    email: EmailStr
    workshop: str
