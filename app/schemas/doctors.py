from pydantic import BaseModel
from typing import Optional


class DoctorCreate(BaseModel):
    first_name : str
    last_name : str
    specialization :str


class DoctorResponse(BaseModel):
    id : int
    first_name : str
    last_name : str
    specialization : str 

    class Config:
        from_attributes = True

class DoctorUpdate(BaseModel):
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    specialization : Optional[str] = None