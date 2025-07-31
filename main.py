from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import database
from elonlar import Elonlar
from datetime import datetime

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"]
)


@app.get('/get')
def elonlarni_korish(name: str = None, db: Session = Depends(database)):
    if name:
        return db.query(Elonlar).filter(Elonlar.name.like(f"%{name}%")).all()
    else:
        return db.query(Elonlar).all()


@app.post('/add')
def elon_qoshish(description: str, status: bool, name: str = Query(min_length=3), price: float = Query(gt=1, lt=1000000), created_at: datetime = datetime.now(), db: Session = Depends(database)):
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