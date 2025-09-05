from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.config import settings
from app.services.signals import generate_signal
from app.utils.logger import logger

scheduler = AsyncIOScheduler()

def start_scheduler():
    symbols = [s.strip() for s in settings.SYMBOLS.split(',')]
    tf = settings.TIMEFRAMES.split(',')[0]

    for s in symbols:
        scheduler.add_job(generate_signal, 'interval', minutes=15, args=[s, tf], id=f'scan_{s}_{tf}')
    scheduler.start()
    logger.info('Scheduler started')
