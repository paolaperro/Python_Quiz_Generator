import os

from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam

from src.features.character import character_service
from src.features.story.story_models import Story

MODEL = os.getenv("OPENAI_MODEL")
SYSTEM_PROMPT = """Sei un autore di storie e devi scrivere una storia.

# Istruzioni
- Scrivi la storia in italiano, di circa 400 parole.
- Il pubblico di riferimento sono i bambini.
- La storia deve avere un inizio, uno sviluppo e una conclusione.
- Segui il tema, i personaggi e gli eventuali dettagli forniti dall'utente.
- La narrazione deve essere coerente e coinvolgente,
con un tono adeguato al tema.
- Tutti i personaggi devono essere inclusi, anche con un ruolo secondario.
"""

USER_PROMPT = """# Tema
{theme}

# Personaggi
{characters}

# Dettagli
{details}
"""

client = OpenAI()

def generate_story(theme: str, character_ids: list[int], details: str | None = None):
    characters_text = ""
    for character_id in character_ids:
        character = character_service.get_character(character_id)

        if not character:
            continue

        characters_text += f"- {character.name} ({character.description})\n"

    if not characters_text:
        characters_text = "Inventa tu i personaggi coerenti con il tema e con i dettagli forniti."

    if not details:
        details = "-"

    user_prompt = USER_PROMPT.replace("{theme}", theme.strip()).replace("{characters}", characters_text.strip()).replace("{details}", details.strip())

    response = client.chat.completions.parse(
        model=MODEL,
        messages=[
            ChatCompletionSystemMessageParam(role="system", content=SYSTEM_PROMPT),
            ChatCompletionUserMessageParam(role="user", content=user_prompt)
        ],
        temperature=1,
        response_format=Story
    )

    data = response.choices[0].message.parsed

    return data


