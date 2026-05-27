#!/usr/bin/env python3
"""Check translation quality and flag low-confidence results."""
import json, sys

def check(data):
    score = data.get("quality_score", 0)
    text_length = len(data.get("text", ""))
    result = {
        "quality": score,
        "acceptable": score >= 0.7,
        "needs_review": score < 0.7,
        "recommendation": "Use as-is" if score >= 0.85 else "Review recommended" if score >= 0.7 else "Human translation needed"
    }
    if text_length < 10 and score < 0.8:
        result["note"] = "Short text — detection/translation less reliable"
    return result

if __name__ == "__main__":
    print(json.dumps(check(json.loads(sys.argv[1])), indent=2))
