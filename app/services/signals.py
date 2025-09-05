from app.services.data import fetch_ohlcv
from app.core.strategies.ema_rsi import ema_rsi_signal
from app.db.db import SessionLocal
from app.db.models import Signal
from app.utils.logger import logger

def generate_signal(symbol, timeframe='15m'):
    df = fetch_ohlcv(symbol, timeframe=timeframe, limit=200)
    res = ema_rsi_signal(df)
    if res:
        s = Signal(symbol=symbol, timeframe=timeframe, side=res['side'], price=float(df.iloc[-1]['close']))
        session = SessionLocal()
        session.add(s)
        session.commit()
        session.close()
        logger.info('Signal generated: %s %s', symbol, res)
        return s
    return None
