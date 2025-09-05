import ccxt
import pandas as pd
from app.config import settings
from app.utils.logger import logger

def fetch_ohlcv(symbol, timeframe='15m', limit=500):
    ex = ccxt.binance({
        'apiKey': settings.BINANCE_APIKEY or '',
        'secret': settings.BINANCE_SECRET or '',
        'enableRateLimit': True,
    })
    if settings.USE_TESTNET:
        try:
            ex.set_sandbox_mode(True)
        except Exception:
            pass
    ohlcv = ex.fetch_ohlcv(symbol.replace('/', ''), timeframe=timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['ts','open','high','low','close','vol'])
    df['ts'] = pd.to_datetime(df['ts'], unit='ms')
    df['open'] = df['open'].astype(float)
    df['high'] = df['high'].astype(float)
    df['low'] = df['low'].astype(float)
    df['close'] = df['close'].astype(float)
    df['vol'] = df['vol'].astype(float)
    return df
