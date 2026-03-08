from pydantic import BaseModel
from datetime import date
from typing import Optional

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
        
        
#wird benutzt um die Änderung durchführen
class PatientUpdate(BaseModel):
    first_name : Optional[str] = None
    last_name : Optional[str] = None
    birth_date : Optional[date] = None