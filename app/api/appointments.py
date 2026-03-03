from fastapi import APIRouter, HTTPException
from app.database import get_connection
from datetime import date
from app.schemas.appointments import AppointmentCreate, AppointmentResponse
from typing import List

router = APIRouter()

#CREAT NEW APPINTMENT
@router.post("/appointments", response_model= AppointmentResponse)
def creat_appointments(appointments: AppointmentCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO appointments(patient_id, doctor_id, appointment_date)
        VALUES(%s,%s, %s) RETURNING id, patient_id, doctor_id, appointment_date""",
        (appointments.patient_id, appointments.doctor_id, appointments.appointment_date)
    )

    new_appointment = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()
    return {"id":new_appointment[0],
            "patient_id": new_appointment[1],
            "doctor_id": new_appointment[2],
            "appointment_date": new_appointment[3]}

#READ ALL APPOINTMENTS
@router.get("/appointments", response_model=list[AppointmentResponse])
def get_appointments():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, patient_id, doctor_id, appointment_date FROM appointments")

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    appointments = []
    for row in rows:
        appointments.append({
            "id": row[0],
            "patient_id": row[1],
            "doctor_id": row[2],
            "appointment_date" : row[3]

        })
    
    return appointments

#READ ONE APPOINTMENT WITH PATIENT_ID
@router.get("/appointments/by_patient/{patient_id}")
def get_appointments_patient(patient_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM appointments WHERE patient_id = %s",
                   (patient_id, )
                   )

    appo = cursor.fetchall()
    cursor.close()
    conn.close()
    if not appo:
        raise HTTPException(status_code=404, detail="patient hat keine Termin")
    return appo

#READ APPOINTMNETS WITH DOCTOR_ID 
@router.get("/appointments/by_doctor/{doctor_id}")
def get_appointment_doctor(doctor_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM appointments WHERE doctor_id = %s",
        (doctor_id,)
    )

    appo = cursor.fetchall()
    cursor.close()
    conn.close()
    if not appo:
        raise HTTPException(status_code=404, detail="doctor hat keinen Termin")
    return appo


#DELETE ONE APPOINTMENT
@router.delete("/appointments/{appointmnet_id}")
def delete_appointment(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM appointments WHERE id = %s RETURNING id",
        (appointment_id,)
    )

    deleted = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()

    if not deleted:
        raise HTTPException(status_code=404, detail="es gibt keine Termin")
    return {"message": "Termin gelöscht"}