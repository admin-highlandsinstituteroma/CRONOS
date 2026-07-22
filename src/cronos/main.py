from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="CRONOS",
    version="0.1.0"
)

BASE_DIR = Path(__file__).parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "CRONOS"
        }
    )


@app.get("/health")
async def health():
    return JSONResponse({"status": "ok"})


@app.get("/version")
async def version():
    return JSONResponse({
        "service": "CRONOS",
        "version": "0.1.0"
    })
