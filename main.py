from fastapi import FastAPI
from app.database import get_connection
from app.init_db import create_table
from app.api.patients import router as patient_router

app = FastAPI()

@app.on_event("startup")
def startup():
    create_table()

app.include_router(patient_router)