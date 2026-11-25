from pydantic import BaseModel

class Story(BaseModel):
    title: str
    content: str

class PostGenerateStoryRequest(BaseModel):
    theme: str
    character_ids: list[int]
    details: str | None

class PostGenerateStoryResponse(BaseModel):
    story: Story