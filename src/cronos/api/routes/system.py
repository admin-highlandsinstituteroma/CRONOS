from fastapi import APIRouter

router = APIRouter(tags=["System"])

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/version")
async def version():
    return {
        "service": "CRONOS",
        "version": "0.1.0"
    }
