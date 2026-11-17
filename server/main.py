import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from server.api.websocket import router as websocket_router
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

app = FastAPI()
app.include_router(websocket_router)
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
async def hello(request:Request):
    return templates.TemplateResponse(
        "index.html",
        {"request" : request}
        )
if __name__ == "__main__":
    uvicorn.run(app)