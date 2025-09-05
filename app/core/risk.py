from app.config import settings

def position_size(equity, risk_pct, entry, stop):
    risk_amount = equity * risk_pct
    per_unit_risk = abs(entry - stop)
    if per_unit_risk <= 0:
        return 0
    qty = risk_amount / per_unit_risk
    return max(qty, 0)
