from fastapi import APIRouter

from src.features.character import character_service
from src.features.character.character_models import GetCharactersResponse

character_router = APIRouter(
    prefix="/api/characters"
)

@character_router.get("", response_model=GetCharactersResponse)
def get_characters_endpoint():
    characters = character_service.get_characters()

    return {
        "characters": characters
    }