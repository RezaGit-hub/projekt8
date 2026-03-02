from fastapi import APIRouter, HTTPException
from app.database import get_connection


router = APIRouter()

#CREAT NEW DOKTOR
@router.post("/doctors")
def create_doctors(first_name: str, last_name: str, specialization: str):
    conn = get_connection()
    cursor= conn.cursor()

    cursor.execute(
        """INSERT INTO doctors(first_name, last_name, specialization)
        VALUES(%s, %s, %s) RETURNING id""",
        (first_name, last_name, specialization)
    )

    new_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()
    return {"id": new_id, "message": "doctor erstellt"}

#READ ALL DOCTORS
@router.get("/doctors")
def get_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

#READ ONE DOCTOR WITH ID
@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE id = %s",
                   (doctor_id,)
                   )

    doctor = cursor.fetchall()
    cursor.close()
    conn.close()

    if not doctor:
        raise HTTPException(status_code=404, detail="doctor nicht gefunden")
    return doctor

#READ DOCTOR WITH NAME
@router.get("/doctors/{last_name}")
def get_doctorsname(last_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE last_name = %s",
                   (last_name, )
                   )
    doctorsname = cursor.fetchall()

    cursor.close()
    conn.close()

    return doctorsname

#DELETE ONE DOCTOR
@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM doctors WHERE id = %s RETURNING id",
                   (doctor_id, )
                   )
    deleted = cursor.fetchone()
    
    conn.commit()
    cursor.close()
    conn.close()

    if not deleted:
        raise HTTPException(status_code= 404, detail="doctor nicht gefunden")
    return {"message: ":"doctor gelöscht"}

