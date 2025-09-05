from fastapi import FastAPI
from app.db.db import SessionLocal
from app.db.models import Signal

app = FastAPI()

@app.get('/signals')
def get_signals(limit: int = 50):
    s = SessionLocal()
    rows = s.query(Signal).order_by(Signal.created_at.desc()).limit(limit).all()
    s.close()
    return [{'symbol': r.symbol, 'side': r.side, 'price': r.price, 'ts': r.created_at.isoformat()} for r in rows]
