from fastapi import APIRouter, HTTPException, Depends
from app.database import get_connection
from app.schemas.doctors import DoctorCreate, DoctorResponse, DoctorUpdate
from typing import List
from app.services.auth_dependencies import get_current_user

router = APIRouter()

#CREAT NEW DOKTOR
@router.post("/doctors", response_model= DoctorResponse)
def create_doctors(doctors : DoctorCreate, current_user = Depends(get_current_user)):

    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="not authorized")
    
    conn = get_connection()
    cursor= conn.cursor()

    cursor.execute(
        """INSERT INTO doctors(first_name, last_name, specialization)
        VALUES(%s, %s, %s) RETURNING id, first_name, last_name, specialization""",
        (doctors.first_name, doctors.last_name, doctors.specialization)
    )

    new_id = cursor.fetchone()

    conn.commit()
    
    return {"id": new_id[0], 
            "first_name" : new_id[1],
            "last_name": new_id[2],
            "specialization" : new_id[3] 
            }

#READ ALL DOCTORS
@router.get("/doctors", response_model= List[DoctorResponse])
def get_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name , last_name , specialization  FROM doctors")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    doctors = []
    for row in rows:
        doctors.append({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "specialization": row[3]
        })

    return doctors

#READ ONE DOCTOR WITH ID
@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id:int):
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
def get_doctorsname(last_name:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE last_name = %s",
                   (last_name, )
                   )
    doctorsname = cursor.fetchall()

    cursor.close()
    conn.close()

    return doctorsname

#UPDTAE DOCTOR
@router.put("/doctors/{doctor_id}", response_model=DoctorResponse)
def update_doctor(doctor_id :int, doctor: DoctorUpdate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """UPDATE doctors
        SET first_name = COALESCE(%s, first_name),
        last_name = COALESCE(%s, last_name),
        specialization = COALESCE(%s, specialization)
        WHERE id = %s
        RETURNING id , first_name, last_name, specialization""",
        (doctor.first_name, doctor.last_name, doctor.specialization, doctor_id)
    )
    updated= cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    if not updated:
        raise HTTPException(status_code=404, detail="doctor nicht gefunden")

    return{"id" : updated[0],
           "first_name": updated[1],
           "last_name": updated[2],
           "specialization": updated[3]
           } 

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

