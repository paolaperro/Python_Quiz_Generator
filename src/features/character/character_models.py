from pydantic import BaseModel

class Character(BaseModel):
    id: int
    name: str
    description: str

class GetCharactersResponse(BaseModel):
    characters: list[Character]