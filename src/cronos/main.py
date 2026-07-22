from fastapi import FastAPI
from cronos.api.routes.system import router as system_router

app = FastAPI(
    title="CRONOS",
    description="Calendar & Resource Orchestration Network Operating System",
    version="0.1.0"
)

app.include_router(system_router)

@app.get("/")
async def root():
    return {
        "service": "CRONOS",
        "status": "online"
    }
