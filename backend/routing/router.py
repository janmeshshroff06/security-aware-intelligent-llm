def select_model(scores: list[dict]) -> dict:
    if not scores:
        raise ValueError("Model scores cannot be empty")

    selected = max(scores, key=lambda item: item["score"])

    return {
        "selected_model": selected["model"],
        "score": selected["score"],
    }