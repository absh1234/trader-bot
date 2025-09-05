import pandas as pd
from app.services.data import fetch_ohlcv
from app.core.strategies.ema_rsi import ema_rsi_signal

def simple_backtest(symbol='BTC/USDT', timeframe='15m', initial_cash=1000):
    df = fetch_ohlcv(symbol, timeframe=timeframe, limit=1000)
    cash = initial_cash
    position = 0
    entry_price = 0
    equity_curve = []
    for i in range(50, len(df)):
        window = df.iloc[:i+1].copy()
        sig = ema_rsi_signal(window)
        close = float(window.iloc[-1]['close'])
        if sig and sig['side'] == 'long' and position == 0:
            position = cash / close
            entry_price = close
            cash = 0
        elif sig and sig['side'] == 'short' and position > 0:
            cash = position * close
            position = 0
            entry_price = 0
        equity = cash + position * close
        equity_curve.append(equity)
    res = {
        'start_cash': initial_cash,
        'end_equity': equity_curve[-1] if equity_curve else initial_cash,
        'equity_curve': equity_curve
    }
    return res
