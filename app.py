from fastapi import FastAPI

app = FastAPI(
    title="CRONOS",
    description="Calendar & Resource Orchestration Network Operating System",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "service": "CRONOS",
        "status": "online",
        "version": "0.1.0"
    }

@app.get("/health")
async def health():
    return {
        "status": "ok"
    }
