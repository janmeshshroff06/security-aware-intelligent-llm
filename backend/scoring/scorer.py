from scoring.models import MODEL_PROFILES


REASONING_WEIGHTS = {
    "low": 0.25,
    "medium": 0.5,
    "high": 0.75,
}


def score_models(classification: dict) -> list[dict]:
    task_type = classification["task_type"]
    reasoning_level = classification["reasoning_level"]

    reasoning_weight = REASONING_WEIGHTS[reasoning_level]
    task_weight = 1 - reasoning_weight

    scores = []

    for model_name, capabilities in MODEL_PROFILES.items():
        task_score = capabilities[task_type]
        reasoning_score = capabilities["reasoning"]

        final_score = (
            task_score * task_weight
            + reasoning_score * reasoning_weight
        )

        scores.append({
            "model": model_name,
            "score": round(final_score, 2),
        })

    return scores