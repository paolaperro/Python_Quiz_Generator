from dotenv import load_dotenv
load_dotenv()

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.routers.character_router import character_router
from src.routers.story_router import story_router

app = FastAPI(
    title="Generatore di storia",
    description="Permette di generare storie utilizzando l'AI",
    version="0.1.0"
)

app.include_router(character_router)
app.include_router(story_router)

app.mount("/", StaticFiles(directory="static"), name="static")

def main():
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000

    )

if __name__ == "__main__":
    main()

