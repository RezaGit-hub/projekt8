from fastapi import FastAPI
from app.database import get_connection
from app.init_db import create_table

app = FastAPI()

@app.on_event("startup")
def startup():
    create_table()

@app.get("/")
def root():
    return {"message" : "DB connection erfolgreich"}