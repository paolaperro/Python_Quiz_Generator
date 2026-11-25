from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.features.quiz import quiz_service
from src.routers.quiz_router import quiz_router

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = quiz_service.create_client()
    app.state.quiz_client = client
    try:
        yield
    finally:
        if client is not None:
            client.close()


app = FastAPI(
    title="Generatore di quiz",
    description="Genera quiz da un argomento o dai tuoi appunti con l'AI",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(quiz_router)
# Il mount va dopo le API, altrimenti intercetta anche le loro richieste.
app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
