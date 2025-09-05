import logging
from app.config import settings

logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
                    format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger('trading-bot')
