import pandas as pd
from app.core.strategies.ema_rsi import ema_rsi_signal

def test_ema_rsi_no_signal():
    df = pd.DataFrame({'close': [1,2,1.5,1.7,1.6]})
    assert ema_rsi_signal(df) is None
