from fastapi import FastAPI

app = FastAPI(
    title="NextMe API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "NextMe API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
