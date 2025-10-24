import os
import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY", "")
API_SECRET = os.getenv("BINANCE_API_SECRET", "")
BASE_URL = os.getenv("BINANCE_API_URL", "https://fapi.binance.com")
DRY_RUN = os.getenv("DRY_RUN", "1")  
class FuturesClient:
    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = (API_SECRET.encode() if API_SECRET else None)
        self.base_url = BASE_URL.rstrip("/")
        self.dry = str(DRY_RUN) not in ("0", "false", "False")

    def _mock_order_response(self, symbol, side, typ, quantity, price):
        
        return {
            "symbol": symbol,
            "orderId": int(time.time() * 1000) % 1000000,
            "status": "FILLED",
            "side": side,
            "type": typ,
            "origQty": str(quantity) if quantity is not None else "0",
            "price": str(price) if price is not None else "0",
            "executedQty": str(quantity) if quantity is not None else "0",
            "mock": True
        }

    def _sign(self, params):
        params["timestamp"] = int(time.time() * 1000)
        query = urlencode(params)
        signature = hmac.new(self.api_secret, query.encode(), hashlib.sha256).hexdigest()
        return query + "&signature=" + signature

    def _send(self, method, path, params=None, signed=False):
        if self.dry:
           
            if path.endswith("/order") and method == "POST":
                return self._mock_order_response(
                    symbol=params.get("symbol"),
                    side=params.get("side"),
                    typ=params.get("type"),
                    quantity=params.get("quantity"),
                    price=params.get("price")
                )
           
            return {"mock": True, "path": path, "params": params}
        
        url = f"{self.base_url}{path}"
        headers = {"X-MBX-APIKEY": self.api_key} if self.api_key else {}
        if signed:
            if not self.api_secret:
                raise RuntimeError("API secret missing for signed request")
            query = self._sign(params or {})
            url = url + "?" + query
            r = requests.request(method, url, headers=headers, timeout=10)
        else:
            r = requests.request(method, url, headers=headers, params=params, timeout=10)
        try:
            return r.json()
        except Exception:
            return {"error": r.text}

    def place_order(self, symbol, side, type="MARKET", quantity=None, price=None):
        data = {"symbol": symbol.upper(), "side": side.upper(), "type": type.upper()}
        if quantity is not None:
            data["quantity"] = quantity
        if price is not None:
            data["price"] = price
            data["timeInForce"] = "GTC"
        return self._send("POST", "/fapi/v1/order", params=data, signed=not self.dry)

    def get_price(self, symbol):
        if self.dry:
            return {"symbol": symbol, "price": "30000.00", "mock": True}
        return self._send("GET", "/fapi/v1/ticker/price", params={"symbol": symbol})
