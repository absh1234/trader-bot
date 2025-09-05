import ccxt
from app.config import settings
from app.utils.logger import logger

class ExchangeService:
    def __init__(self):
        self.ex = ccxt.binance({
            'apiKey': settings.BINANCE_APIKEY or '',
            'secret': settings.BINANCE_SECRET or '',
            'enableRateLimit': True,
        })
        if settings.USE_TESTNET:
            try:
                self.ex.set_sandbox_mode(True)
            except Exception:
                pass

    def create_order_market(self, symbol, side, amount):
        try:
            symbol_ccxt = symbol.replace('/', '')
            if side.lower() in ('buy','long'):
                order = self.ex.create_market_buy_order(symbol_ccxt, amount)
            else:
                order = self.ex.create_market_sell_order(symbol_ccxt, amount)
            return order
        except Exception as e:
            logger.exception('create_order_market error')
            raise
