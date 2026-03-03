# projekt8
PostgreSQL /SQLAlchemy /Alembic /FastAPI/ Docker Compose
Clinic Management API
Project Overview

This project is a REST API for managing:

Patients

Doctors

Appointments

Built with:

FastAPI

PostgreSQL

Docker

Pydantic

Uvicorn

Architecture

FastAPI backend

PostgreSQL database

Docker containerized setup

Separate schema models (Create / Response)

Clean API routing

Database Structure
Patients

id (SERIAL PRIMARY KEY)

first_name (VARCHAR)

last_name (VARCHAR)

birth_date (DATE)

created_at (TIMESTAMP)

Doctors

id

first_name

last_name

specialization

Appointments

id

patient_id (FK)

doctor_id (FK)

appointment_date

How to Run the Project
docker-compose up --build

API available at:

http://localhost:8000

Swagger documentation:

http://localhost:8000/docs
Implemented Endpoints
Patients

POST /patients

GET /patients

GET /patients/id/{id}

GET /patients/lastname/{lastname}

DELETE /patients/{id}

Doctors

CRUD implemented

Appointments

Basic structure implemented

Features

Response validation using Pydantic

Structured API routing

Dockerized environment

Database relations with foreign keys

Error handling with HTTPException

Current Status

MVP completed.
