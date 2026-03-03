from pydantic import BaseModel
from datetime import date

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date


class AppointmentResponse(BaseModel):
    id : int
    patient_id: int
    doctor_id: int
    appointment_date: date


    class Config:
        from_attributes = True