# app/schemas/contact.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str]

class ContactOut(ContactCreate):
    id: int

    class Config:
        orm_mode = True
