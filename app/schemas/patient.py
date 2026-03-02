from pydantic import BaseModel
from datetime import date

#wird es benutzt, wenn ein neue Patient erstellt wird(request)
class PatientCreate(BaseModel):
    first_name:  str
    last_name: str
    birth_date: date


#wird es benutzt , wenn eine patient zurückgegeben wird(response)
class PatientResponse(BaseModel):
    id : int
    first_name : str
    last_name : str
    birth_date: date

    class Config:
        from_attributes = True