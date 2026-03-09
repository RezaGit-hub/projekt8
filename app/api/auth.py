from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate , UserLogin
from app.database import get_connection
from app.services.auth_services import hash_password, verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):

    conn = get_connection()
    cursor = conn.cursor()

    password_hash = hash_password(user.password)

    cursor.execute(
        """INSERT INTO users (email, password_hash)
        VALUES (%s,%s)
        RETURNING id, email, role
        """,
        (user.email, password_hash)
    )

    new_user = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "id" : new_user[0],
        "email" : new_user[1],
        "role" : new_user[2]
    }


@router.post("/login")
def login(user: UserLogin):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, email, password_hash, role FROM users WHERE email=%s",
        (user.email,)
    )

    db_user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not verify_password(user.password, db_user[2]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(
        {"user_id": db_user[0], "role": db_user[3]}
    )

    return {"access_token": token}