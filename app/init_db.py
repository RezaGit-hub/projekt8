from app.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    
    


    cursor.execute(
        """CREATE TABLE IF NOT EXISTS appointments(
        id SERIAL PRIMARY KEY,
        patient_id INTEGER REFERENCES patients(id) ON DELETE CASCADE,
        doctor_id INTEGER REFERENCES doctors(id) ON DELETE SET NULL,
        appointment_date TIMESTAMP NOT NULL,
        reason text,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
    )

    conn.commit()

    

    cursor.close()
    conn.close()
