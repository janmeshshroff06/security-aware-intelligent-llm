import re

def classify_prompt(prompt: str) -> dict:
    normalized_prompt = prompt.lower()

    def contains_keyword(keywords: list[str]) -> bool:
        return any(
            re.search(rf"\b{re.escape(keyword)}\b", normalized_prompt)
            for keyword in keywords
        )

    coding_keywords = [
        "python",
        "java",
        "javascript",
        "typescript",
        "code",
        "debug",
        "function",
        "class",
        "algorithm",
        "api",
    ]

    math_keywords = [
        "math",
        "equation",
        "calculate",
        "solve",
        "algebra",
        "geometry",
        "probability",
        "statistics",
    ]

    writing_keywords = [
        "write",
        "rewrite",
        "email",
        "essay",
        "paragraph",
        "cover letter",
        "resume",
        "summary",
    ]

    high_reasoning_keywords = [
        "debug",
        "algorithm",
        "prove",
        "analyze",
        "explain why",
        "step by step",
        "complex",
    ]

    medium_reasoning_keywords = [
        "compare",
        "explain",
        "solve",
        "recommend",
    ]

    task_type = "general"
    reasoning_level = "low"

    if contains_keyword(coding_keywords):
        task_type = "coding"
    elif contains_keyword(math_keywords):
        task_type = "math"
    elif contains_keyword(writing_keywords):
        task_type = "writing"

    if contains_keyword(high_reasoning_keywords):
        reasoning_level = "high"
    elif contains_keyword(medium_reasoning_keywords):
        reasoning_level = "medium"

    return {
        "task_type": task_type,
        "reasoning_level": reasoning_level,
    }
