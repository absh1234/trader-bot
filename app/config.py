import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    ADMIN_CHAT_ID: str | None = None
    EXCHANGE: str = os.getenv('EXCHANGE', 'binance')
    BINANCE_APIKEY: str | None = None
    BINANCE_SECRET: str | None = None
    USE_TESTNET: bool = os.getenv(
        'USE_TESTNET', 'true').lower() in ('1', 'true', 'yes')
    DB_URL: str = os.getenv('DB_URL', 'sqlite:///./data.db')
    AUTO_EXECUTE: bool = os.getenv(
        'AUTO_EXECUTE', 'false').lower() in ('1', 'true', 'yes')
    PAPER_TRADING: bool = os.getenv(
        'PAPER_TRADING', 'true').lower() in ('1', 'true', 'yes')
    DEFAULT_RISK_PCT: float = float(os.getenv('DEFAULT_RISK_PCT', 0.01))
    SYMBOLS: str = os.getenv('SYMBOLS', 'BTC/USDT')
    TIMEFRAMES: str = os.getenv('TIMEFRAMES', '15m')
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')


settings = Settings()
