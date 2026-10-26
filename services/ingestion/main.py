from fastapi import FastAPI

app = FastAPI(title="FraudShield Ingestion API")


@app.get("/health")
def health():
    return {"status": "ok"}