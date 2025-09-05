def simple_sizing(equity, risk_pct, entry, stop):
    from app.core.risk import position_size
    return position_size(equity, risk_pct, entry, stop)
