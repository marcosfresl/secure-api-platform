from fastapi import FastAPI

app = FastAPI(
    title="Secure API Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Secure API Platform"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }