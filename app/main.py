import asyncio
from app.interfaces.telegram_bot import run_bot
from app.interfaces.scheduler import start_scheduler
from app.db.db import Base, engine
from app.utils.logger import logger

def init_db():
    Base.metadata.create_all(bind=engine)

async def main():
    init_db()
    start_scheduler()
    await run_bot()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info('Shutdown')
