from pydantic import BaseModel, ConfigDict, Field, model_validator


class QuizQuestion(BaseModel):
    text: str
    answer: list[str] = Field(min_length=4, max_length=4)
    correct_answer_index: int = Field(ge=0, le=3)
    spiegazione: str = ""


class Quiz(BaseModel):
    title: str
    quiz_questions: list[QuizQuestion] = Field(min_length=10, max_length=10)


class PostGenerateQuizRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    fonti: str | None = Field(default=None, min_length=30, max_length=50_000)
    argomento: str | None = Field(default=None, min_length=1, max_length=120)

    @model_validator(mode="after")
    def verifica_input(self):
        if (self.fonti is None) == (self.argomento is None):
            raise ValueError("Inserisci un argomento oppure gli appunti.")
        return self


class PostGenerateQuizResponse(BaseModel):
    quiz: Quiz
