from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import database
from elonlar import Elonlar
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
)


@app.get('/get')
def elonlarni_korish(db: Session = Depends(database)):
    return db.query(Elonlar).all()


@app.post('/add')
def elon_qoshish(name: str, description: str, price: float, status: bool, created_at: datetime = datetime.now(), db: Session = Depends(database)):
    elon = Elonlar(
        name = name,
        description = description,
        price = price,
        created_at = created_at,
        status = status
    )
    db.add(elon)
    db.commit()
    return {'message': 'Elon muvofaqiyatli qoshildi !'}