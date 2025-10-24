import argparse
from client import FuturesClient
from utils import setup_logger, validate
import os

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Place Market Order")
    parser.add_argument("symbol", help="e.g. BTCUSDT")
    parser.add_argument("side", help="BUY or SELL")
    parser.add_argument("qty", help="e.g. 0.01")
    parser.add_argument("--dry", action="store_true", help="run in dry-run/mock mode")
    args = parser.parse_args()

    if args.dry:
        os.environ["DRY_RUN"] = "1"

    try:
        validate(args.symbol, args.side, args.qty)
        client = FuturesClient()
        res = client.place_order(symbol=args.symbol, side=args.side, type="MARKET", quantity=args.qty)
        logger.info(f"Market Order Placed: {res}")
        print("Market Order Done!")
        print(res)
    except Exception as e:
        logger.error(f"Error: {e}")
        print(" Error:", e)

if __name__ == "__main__":
    main()
