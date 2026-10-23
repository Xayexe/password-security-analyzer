"""Educational password security analyzer. Does not store or transmit passwords."""

from __future__ import annotations

import getpass
import re
from dataclasses import dataclass

COMMON_PASSWORDS = {
    "password", "password1", "password123", "123456", "12345678",
    "123456789", "1234567890", "qwerty", "qwerty123", "abc123",
    "admin", "admin123", "letmein", "welcome", "iloveyou", "111111",
}
SEQUENCES = ("abcdefghijklmnopqrstuvwxyz", "0123456789", "qwertyuiop", "asdfghjkl", "zxcvbnm")


@dataclass(frozen=True)
class Assessment:
    rating: str
    score: int
    feedback: tuple[str, ...]


def has_sequence(password: str, size: int = 4) -> bool:
    lowered = password.lower()
    for sequence in SEQUENCES:
        for candidate in (sequence, sequence[::-1]):
            if any(candidate[i:i + size] in lowered for i in range(len(candidate) - size + 1)):
                return True
    return False


def analyze_password(password: str) -> Assessment:
    """Provide heuristic feedback; not a measure of actual cracking resistance."""
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if not password:
        return Assessment("Very weak", 0, ("Enter a non-empty test password.",))

    feedback: list[str] = []
    score = 0
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
        feedback.append("Consider 16 or more characters for a stronger passphrase.")
    elif length >= 8:
        score += 1
        feedback.append("Use at least 12–16 characters; longer is generally better.")
    else:
        feedback.append("This password is short. Aim for at least 12–16 characters.")

    categories = (
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() and not c.isspace() for c in password),
    )
    diversity = sum(categories)
    if diversity >= 3:
        score += 1
    else:
        feedback.append("Consider more varied characters or a longer, unpredictable passphrase.")

    lowered = password.lower()
    if lowered in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a widely used password. Choose something unique.")
    else:
        if has_sequence(password):
            score = max(0, score - 1)
            feedback.append("Avoid obvious sequences such as '1234' or 'abcd'.")
        if re.search(r"(.)\1{2,}", lowered):
            score = max(0, score - 1)
            feedback.append("Avoid repeating the same character three or more times.")
        if re.search(r"(?i)(password|qwerty|letmein|admin)", password):
            score = max(0, score - 2)
            feedback.append("Avoid common password words and keyboard patterns.")

    if length < 8:
        score = min(score, 1)
    score = max(0, min(score, 4))
    rating = ("Very weak", "Weak", "Fair", "Good", "Strong")[score]
    if not feedback:
        feedback.append("Good start. Use a unique password and enable multi-factor authentication.")
    return Assessment(rating, score, tuple(feedback))


def main() -> None:
    print("=== Password Security Analyzer ===")
    print("Educational feedback only. Never enter a real password into an untrusted tool.")
    try:
        password = getpass.getpass("Enter a MADE-UP test password (hidden input): ")
    except (EOFError, KeyboardInterrupt):
        print("\nCancelled.")
        return
    result = analyze_password(password)
    print(f"\nAssessment: {result.rating} ({result.score}/4)")
    for item in result.feedback:
        print(f"- {item}")
    print("Reminder: A score cannot prove a password is safe. Prefer unique, randomly generated passwords or long passphrases, stored in a password manager, with MFA enabled.")


if __name__ == "__main__":
    main()
