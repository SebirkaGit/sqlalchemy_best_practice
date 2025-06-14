# app/main.py
from fastapi import FastAPI
from app.db.session import engine
from app.models import contact
from app.db.base import Base

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to Contact Book API!"}
