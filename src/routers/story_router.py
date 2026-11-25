from fastapi import APIRouter

from src.features.story import story_service
from src.features.story.story_models import PostGenerateStoryResponse, PostGenerateStoryRequest

story_router = APIRouter(
    prefix="/api/stories"
)

@story_router.post("/generate", response_model=PostGenerateStoryResponse)
def post_generate_story_endpoint(body: PostGenerateStoryRequest):
    story = story_service.generate_story(body.theme, body.character_ids, body.details)

    return {
        "story": story
    }

