from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from security.scanner import security_check
from classification.classifier import classify_prompt
from scoring.scorer import score_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PromptRequest(BaseModel):
    prompt: str

class ClassificationRequest(BaseModel):
    task_type: str
    reasoning_level: str

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/security-check")
def check_prompt(request: PromptRequest):
    return security_check(request.prompt)

@app.post("/classify")
def classify_prompt_endpoint(request: PromptRequest):
    return classify_prompt(request.prompt)

@app.post("/score-models")
def score_model_profiles(request: ClassificationRequest):
    classification = {
        "task_type": request.task_type,
        "reasoning_level": request.reasoning_level,
    }

    return {
        "scores": score_models(classification),
    }