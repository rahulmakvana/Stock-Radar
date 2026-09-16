from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Stock Radar")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "ok": True,
        "service": "Stock Radar",
        "trading_enabled": False
    }

@app.get("/api/scanner/demo")
def scanner():
    return {
        "mode": "DEMO",
        "stocks": [
            {
                "symbol": "TCS",
                "cmp": 3820,
                "fair_value": 4450,
                "upside": 16.5,
                "score": 86
            },
            {
                "symbol": "INFY",
                "cmp": 1510,
                "fair_value": 1760,
                "upside": 16.6,
                "score": 83
            },
            {
                "symbol": "HDFCBANK",
                "cmp": 1695,
                "fair_value": 1950,
                "upside": 15.0,
                "score": 81
            }
        ]
    }
