from fastapi import APIRouter, HTTPException
from app.database import get_connection
from datetime import date
from app.schemas.patient import PatientCreate, PatientResponse
from typing import List

router = APIRouter()

#Create
@router.post("/patients", response_model=PatientResponse)
def create_patient(patient : PatientCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO patients(first_name, last_name, birth_date)
        VALUES (%s,%s,%s)
        RETURNING id, first_name, last_name, birth_date""",
        (patient.first_name, patient.last_name, patient.birth_date)
    )

    new_patient = cursor.fetchone()
    conn.commit()
    

    return {"id": new_patient[0],
            "first_name": new_patient[1],
            "last_name": new_patient[2],
            "birth_date": new_patient[3]}


#READ ALL
@router.get("/patients",  response_model= List[PatientResponse])
def get_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, first_name, last_name, birth_date FROM patients"
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    patients = []
    for row in rows:
        patients.append({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "birth_date": row[3]
        })

    return patients

#READ ONE PATIENT
@router.get("/patients/id/{patient_id}")
def get_patient(patient_id :int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE id = %s",
                   (patient_id,))
    patient = cursor.fetchall()

    cursor.close()
    conn.close()

    if not patient:
        raise HTTPException(status_code=404, detail="patient nicht gefunden")
    return patient

#READ ONE PATIENT WITH LASTNAME
@router.get("/patients/lastname/{last_name}")
def get_patient_lastname(last_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE last_name = %s", (last_name,))

    patient = cursor.fetchall()
    cursor.close()
    conn.close()
    return patient


#DELET
@router.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM patients WHERE id = %s RETURNING id;",
                   (patient_id,))
    
    deleted = cursor.fetchone()
    conn.commit()

    cursor.close()
    conn.close()

    if not deleted:
        raise HTTPException(status_code=404, detail="patient nicht gefunden")
    return{"message": "patient gelöscht"}