import pandas as pd

def ema_rsi_signal(df: pd.DataFrame, fast=9, slow=21, rsi_len=14, rsi_floor=45, rsi_ceil=55):
    df = df.copy()
    df['ema_fast'] = df['close'].ewm(span=fast).mean()
    df['ema_slow'] = df['close'].ewm(span=slow).mean()
    delta = df['close'].diff()
    gain = (delta.clip(lower=0)).rolling(rsi_len).mean()
    loss = (-delta.clip(upper=0)).rolling(rsi_len).mean()
    rs = gain / (loss.replace(0, 1e-9))
    df['rsi'] = 100 - (100 / (1 + rs))
    last = df.iloc[-1]

    if last.ema_fast > last.ema_slow and last.rsi > rsi_floor:
        return {'side': 'long'}
    if last.ema_fast < last.ema_slow and last.rsi < rsi_ceil:
        return {'side': 'short'}
    return None
