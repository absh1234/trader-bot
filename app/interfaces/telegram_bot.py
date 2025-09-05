import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.config import settings
from app.utils.logger import logger
from app.services.signals import generate_signal
from app.services.orders import place_market_order

bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(m: types.Message):
    await m.answer('سلام! من ربات اتوماسیونم. برای وضعیت /status و برای درخواست سیگنال /scan بزن.')

@dp.message(Command('status'))
async def cmd_status(m: types.Message):
    await m.answer('وضعیت: در حال اجرا. Paper trading: {}'.format(settings.PAPER_TRADING))

@dp.message(Command('scan'))
async def cmd_scan(m: types.Message):
    symbol = settings.SYMBOLS.split(',')[0]
    sig = generate_signal(symbol.replace(' ', ''), timeframe=settings.TIMEFRAMES.split(',')[0])
    if not sig:
        await m.answer('سیگنالی یافت نشد.')
        return
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='ورود ✅', callback_data=f'enter|{sig.id}')],
        [InlineKeyboardButton(text='رد ❌', callback_data=f'reject|{sig.id}')]
    ])
    await m.answer(f"سیگنال: {sig.symbol} - {sig.side} at {sig.price}", reply_markup=kb)

@dp.callback_query(lambda c: True)
async def cb_handler(c: types.CallbackQuery):
    data = c.data
    try:
        action, sid = data.split('|')
    except:
        await c.answer('داده نامعتبر')
        return
    if action == 'enter':
        amount = 0.001
        try:
            o = place_market_order('BTC/USDT', 'buy', amount)
            await c.message.edit_text('سفارش اجرا شد ✅')
        except Exception as e:
            await c.message.edit_text('خطا در ثبت سفارش: {}'.format(e))
    else:
        await c.message.edit_text('رد شد ❌')

async def run_bot():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
