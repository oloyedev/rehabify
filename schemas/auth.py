from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class PhysioSignUp(BaseModel):
    first_name: str
    last_name: str
    mail: EmailStr
    city_of_practice: str
    year_of_graduation: int  
    password: str
    confirm_password: str
    license_expiring_date: Optional[date] = None  


class PatientSignUp(BaseModel):
    first_name: str
    last_name: str
    mail: EmailStr
    password: str
    confirm_password: str


class PhysioSignIn(BaseModel):
    mail: EmailStr
    password: str


class PatientSignIn(BaseModel):
    mail: EmailStr
    password: str
