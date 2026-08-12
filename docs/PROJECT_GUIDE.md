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

## Current Status

### Completed

- [x] Project purpose defined
- [x] V1 scope frozen
- [x] Architecture selected
- [x] React + TypeScript selected for frontend
- [x] FastAPI selected for backend
- [x] GitHub repository created
- [x] Initial folders created
- [x] PROJECT_GUIDE.md created

### In Progress

- [ ] Initialize React + TypeScript frontend

### Upcoming

- [ ] Initialize FastAPI backend
- [ ] Create `/health` endpoint
- [ ] Connect frontend and backend
- [ ] Implement security check
- [ ] Implement prompt classifier
- [ ] Implement model scoring
- [ ] Implement model selection
- [ ] Integrate 3 models
- [ ] Generate response
- [ ] Explain model selection
- [ ] Complete V1 end-to-end testing
