from pydantic import BaseModel


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