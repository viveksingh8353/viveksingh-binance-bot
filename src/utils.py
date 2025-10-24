import logging
import sys

def setup_logger():
    logger = logging.getLogger("bot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler("bot.log")
        sh = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(sh)
    return logger

def validate(symbol, side, qty, price=None):
    if not symbol.isupper():
        raise ValueError("Symbol uppercase me likh bhai (BTCUSDT)")
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side galat h — BUY ya SELL likh")
    if float(qty) <= 0:
        raise ValueError("Quantity 0 se zyada honi chahiye")
    if price is not None and float(price) <= 0:
        raise ValueError("Price 0 se zyada honi chahiye")
