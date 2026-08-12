from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from security.scanner import security_check

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


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/security-check")
def check_prompt(request: PromptRequest):
    return security_check(request.prompt)