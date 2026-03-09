from app.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS doctors(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        specialization VARCHAR(60),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
    )

    conn.commit()
    
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS patients(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        birth_date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""
    )
    conn.commit()

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

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        email VARCHAR(100) UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,

        role VARCHAR(20) DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """
    )

   
    conn.commit()
    

    cursor.close()
    conn.close()