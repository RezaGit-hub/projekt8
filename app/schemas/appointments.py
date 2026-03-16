from pydantic import BaseModel
from datetime import date
from typing import Optional

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    reason: str


class AppointmentResponse(BaseModel):
    id : int
    patient_id: int
    doctor_id: int
    appointment_date: date
    reason: str


    class Config:
        from_attributes = True

class AppointmentUpdate(BaseModel):
    patient_id : Optional[int] = None
    doctor_id : Optional[int] = None
    appointment_date : Optional[date] = None
    reason : Optional[str] = None