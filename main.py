from fastapi import FastAPI
from app.database import get_connection
from app.init_db import create_table
from app.api.patients import router as patient_router
from app.api.doctors import router as doctor_router
from app.api.appointments import router as appointment_router
from app.api import auth
app = FastAPI()
"""
@app.on_event("startup")
def startup():
    create_table()"""

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(auth.router, prefix="/auth", tags=["auth"])