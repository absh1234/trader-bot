from app.services.exchange_ccxt import ExchangeService
from app.db.db import SessionLocal
from app.db.models import Order
from app.utils.logger import logger

exchange = ExchangeService()

def place_market_order(symbol, side, amount):
    session = SessionLocal()
    try:
        raw = exchange.create_order_market(symbol, side, amount)
        price = 0
        if isinstance(raw, dict):
            price = raw.get('price') or raw.get('avgPrice') or 0
        o = Order(symbol=symbol, side=side, amount=amount, price=price, status='filled', raw=raw)
        session.add(o)
        session.commit()
        return o
    except Exception as e:
        logger.exception('place_market_order failed')
        session.rollback()
        raise
    finally:
        session.close()
