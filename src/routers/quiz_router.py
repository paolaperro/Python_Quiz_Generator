from fastapi import APIRouter, HTTPException, Request
from openai import APITimeoutError, OpenAIError, RateLimitError

from src.features.quiz import quiz_service
from src.features.quiz.quiz_models import PostGenerateQuizRequest, PostGenerateQuizResponse

quiz_router = APIRouter(prefix="/api/quiz", tags=["Quiz"])


@quiz_router.post("/generate", response_model=PostGenerateQuizResponse)
def post_generate_quiz_endpoint(body: PostGenerateQuizRequest, request: Request):
    client = request.app.state.quiz_client
    if client is None:
        raise HTTPException(503, "Configura OPENAI_API_KEY e OPENAI_MODEL nel file .env e riavvia il server.")

    try:
        quiz = quiz_service.generate_quiz(body, client)
    except APITimeoutError:
        raise HTTPException(504, "La generazione sta impiegando troppo tempo. Riprova.") from None
    except RateLimitError:
        raise HTTPException(429, "Il servizio AI ha raggiunto un limite di utilizzo. Riprova più tardi.") from None
    except (OpenAIError, ValueError):
        raise HTTPException(502, "Il servizio AI non ha restituito un quiz valido. Riprova.") from None

    return {"quiz": quiz}
