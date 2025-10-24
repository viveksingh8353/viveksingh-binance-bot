import time
from client import FuturesClient
from utils import setup_logger

logger = setup_logger()

def twap(symbol, side, total_qty, parts, delay):
    client = FuturesClient()
    per_order = float(total_qty) / int(parts)
    for i in range(parts):
        res = client.place_order(symbol=symbol, side=side, type="MARKET", quantity=per_order)
        logger.info(f"TWAP part {i+1}/{parts}: {res}")
        print(f" Part {i+1}/{parts} done!")
        time.sleep(delay)

if __name__ == "__main__":
    twap("BTCUSDT", "BUY", 0.01, 5, 2)
