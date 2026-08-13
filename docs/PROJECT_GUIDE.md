# Security-Aware Intelligent LLM — Project Guide

## Project Purpose

This project is a security-aware intelligent LLM routing system.

The system analyzes a user's prompt, checks it for security concerns, classifies the task, scores multiple AI models, selects the most suitable model, generates a response, and explains why that model was selected.

The project is also intended to support future research and documentation around intelligent model routing and security-aware AI systems.

---

## V1 Scope

V1 should follow this exact flow:

Prompt  
→ Security Check  
→ Classification  
→ Score 3 Models  
→ Select Model  
→ Generate Response  
→ Explain Selection

Do not add unnecessary features before this flow works end-to-end.

---

## Technology Stack

### Frontend
- React
- TypeScript

### Backend
- Python
- FastAPI

### Database
- None for V1
- PostgreSQL or Supabase may be added later if needed

### Models
- Start with 3 models
- Prefer free, free-tier, or local options during early development

---

## Project Structure

```text
security-aware-intelligent-llm/
├── frontend/
├── backend/
├── docs/
│   └── PROJECT_GUIDE.md
├── .gitignore
├── LICENSE
└── README.md
```

---

## V1 Development Order

1. Create project structure
2. Initialize React + TypeScript frontend
3. Initialize FastAPI backend
4. Add backend health endpoint
5. Connect frontend to backend
6. Implement security check
7. Implement prompt classification
8. Implement model scoring
9. Implement model selection
10. Implement model response generation
11. Explain model selection
12. Test the complete V1 pipeline

---

## Initial Backend Pipeline

```text
POST /api/chat
      ↓
security_check()
      ↓
classify_prompt()
      ↓
score_models()
      ↓
select_model()
      ↓
generate_response()
      ↓
return response + routing explanation
```

---

## Development Rules

- Keep V1 simple.
- Build one component at a time.
- Do not add features unless they are required for the V1 pipeline.
- Use mock model scores and responses before integrating real model APIs.
- Test each component before moving to the next.
- Update this file whenever the architecture, scope, or implementation status changes.
- Never commit API keys, secrets, tokens, or credentials.
- Keep security checks separate from model routing logic where possible.

---

## Recovery Instructions

If development becomes disorganized or another AI/developer continues the project:

1. Read this entire file first.
2. Inspect the current project structure.
3. Check GitHub issues and recent commits.
4. Determine which V1 development step is currently being worked on.
5. Do not redesign the architecture unless there is a clear technical reason.
6. Continue from the last completed milestone.
7. Keep changes small and testable.
8. Update this guide after meaningful changes.

The priority is always to restore the project to the agreed V1 flow rather than introducing new features.

---

## Security Check

The first stage of the V1 pipeline is a rule-based prompt security check.

The security logic is located in:

`backend/security/scanner.py`

The API layer calls this logic through:

`POST /security-check`

### Current V1 Behavior

The security scanner:

- Accepts a user prompt
- Normalizes the prompt for matching
- Checks for suspicious prompt-manipulation patterns
- Returns a structured result containing:
  - `allowed`
  - `risk_level`
  - `reason`

Example safe result:

```json
{
  "allowed": true,
  "risk_level": "low",
  "reason": "No security concerns detected"
}
```

Example blocked result:

```json
{
  "allowed": false,
  "risk_level": "high",
  "reason": "Suspicious prompt pattern detected: ignore previous instructions"
}
```

### V1 Scope

The current security layer is intentionally simple and rule-based.

It does not yet use:

- External moderation APIs
- Machine-learning security classifiers
- Advanced jailbreak detection
- Authentication or user reputation systems

The goal of V1 is to establish a clean security interface before prompt classification and model routing are implemented.

---

## Prompt Classification

The second stage of the V1 pipeline is a rule-based prompt classification system.

The classification logic is located in:

`backend/classification/classifier.py`

The API layer exposes this logic through:

`POST /classify`

### Current V1 Behavior

The classifier accepts a user prompt and returns:

- `task_type`
- `reasoning_level`

Supported V1 task types:

- `coding`
- `math`
- `writing`
- `general`

Supported reasoning levels:

- `low`
- `medium`
- `high`

The classifier currently uses simple keyword-based rules.

Whole-word and phrase matching is used to reduce false positives. For example, the keyword `api` should not match the word `capital`.

### Example

Input:

```text
Help me debug this Python recursion problem
```

Output:

```json
{
  "task_type": "coding",
  "reasoning_level": "high"
}
```

Another example:

Input:

```text
Compare these two options
```

Output:

```json
{
  "task_type": "general",
  "reasoning_level": "medium"
}
```

### V1 Scope

The current classifier is intentionally simple and rule-based.

It does not yet use:

- Machine-learning classification
- Embeddings
- External classification APIs
- Model routing
- Database-backed rules

The purpose of this stage is to produce a predictable structured classification result that can be used by the model-scoring system later in the V1 pipeline.

---

## Model Scoring

The third stage of the V1 pipeline is a rule-based model-scoring system.

The model profiles are located in:

`backend/scoring/models.py`

The scoring logic is located in:

`backend/scoring/scorer.py`

The API layer exposes the scoring system through:

`POST /score-models`

### Current V1 Behavior

The scoring system receives a prompt classification containing:

- `task_type`
- `reasoning_level`

It then evaluates all three V1 model profiles using their predefined capabilities:

- Coding
- Math
- Writing
- General
- Reasoning

Each model receives a numerical score based on its task-specific capability and reasoning capability.

### Reasoning Weights

The current V1 scoring formula adjusts the importance of reasoning based on the classified reasoning level:

- `low` → 75% task capability + 25% reasoning capability
- `medium` → 50% task capability + 50% reasoning capability
- `high` → 25% task capability + 75% reasoning capability

### Example

Classification:

```json
{
  "task_type": "coding",
  "reasoning_level": "high"
}
```

The scorer returns structured scores for all three models:

```json
{
  "scores": [
    {
      "model": "model_a",
      "score": 95.0
    },
    {
      "model": "model_b",
      "score": 80.0
    },
    {
      "model": "model_c",
      "score": 75.0
    }
  ]
}
```

The exact values depend on the current model profiles.

### Model Profile Status

The current model capability scores are V1 placeholder values used to develop and test the routing architecture.

They are not claims about real-world model benchmark performance.

These profiles can later be replaced or adjusted using documented capabilities, benchmark data, or project-specific evaluation results when real models are integrated.

### Separation of Responsibilities

The scoring system only calculates model scores.

It does not:

- Sort models
- Select a model
- Call an LLM
- Generate a response

Model selection is handled by the next stage of the V1 pipeline.

### V1 Scope

The current scoring system is intentionally simple, deterministic, and transparent.

It does not yet use:

- Machine-learning ranking
- Real model API calls
- FreeLLMAPI
- Cost optimization
- Latency measurements
- Dynamic benchmarking

---

## Current Status

```text
Prompt
→ Security Check ✅
→ Classification ✅
→ Score 3 Models ✅
→ Select Model
→ Generate Response
→ Explain Selection
```

### Completed

- [x] Project foundation and development environment
- [x] V1 security check
- [x] V1 prompt classification
- [x] V1 model scoring

### In Progress

- None

### Upcoming

- [ ] Model selection
- [ ] Model integration and response generation
- [ ] Routing explanation
- [ ] V1 end-to-end testing