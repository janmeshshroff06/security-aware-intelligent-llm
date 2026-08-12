SUSPICIOUS_KEYWORDS = [
    "ignore previous instructions",
    "system prompt",
    "developer message",
    "bypass security",
    "jailbreak",
]


def security_check(prompt: str) -> dict:
    normalized_prompt = prompt.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in normalized_prompt:
            return {
                "allowed": False,
                "risk_level": "high",
                "reason": f"Suspicious prompt pattern detected: {keyword}",
            }

    return {
        "allowed": True,
        "risk_level": "low",
        "reason": "No security concerns detected",
    }