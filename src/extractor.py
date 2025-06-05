import re

# Define quality attributes and regex patterns
QUALITY_PATTERNS = {
    "security": [
        r"\bsecure\b", r"\bsecurity\b", r"\bprotected\b", r"\baccess control\b"
    ],
    "performance": [
        r"\bfast\b", r"\bquick\b", r"\blatency\b", r"\bperformance\b", r"\bresponse time\b"
    ],
    "usability": [
        r"\beasy\b", r"\busable\b", r"\buser[- ]?friendly\b", r"\baccessible\b", r"\brecognize\b", r"\badapt\b"
    ],
    "maintainability": [
        r"\bmaintain\b", r"\btrack\b", r"\bdebug\b", r"\bupdate\b"
    ],
    "reliability": [
        r"\breliable\b", r"\bfail[- ]?safe\b", r"\bavailable\b"
    ],
    "portability": [
        r"\bmobile\b", r"\bresponsive\b", r"\bportable\b"
    ]
}

def extract_quality_attributes(text):
    matches = []

    for attribute, patterns in QUALITY_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                matches.append(attribute)
                break  # avoid duplicates

    return matches
