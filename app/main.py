from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User
from schemas import UserRegister, UserResponse
from auth import hash_password


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="NextMe API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "NextMe API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/auth/register", response_model=UserResponse)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        email=user.email,
        password_hash=hashed_password,
        plan_type="adult",
        role="user",
        status="active"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
