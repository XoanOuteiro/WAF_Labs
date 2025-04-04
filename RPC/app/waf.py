import re

# Block common SQLi patterns (case-sensitive)
BLACKLIST_PATTERNS = [
    r"(--|\#)",  # Comments
    r"\bOR\b\s*=?\s*\d*\s*=\s*\d*",  # OR 1=1, AND 1=1 (case-sensitive)
    r"\bAND\b\s*=?\s*\d*\s*=\s*\d*",  # AND 1=1 (case-sensitive)
    r"'(?:\s*=\s*|;\s*|,\s*)",  # Single quote followed by possible equals, semicolon, or comma (common SQLi)
    r"\b(SELECT|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE)\b",  # SQL keywords (case-sensitive)
    r"\bUNION\b.*\bSELECT\b",  # UNION SELECT (case-sensitive)
    r"(\bEXEC\b|\bUNION\b.*\bALL\b)",  # EXEC, UNION ALL (case-sensitive)
    r"(\bFROM\b|\bWHERE\b)",  # FROM, WHERE statements (case-sensitive)
    r"\bSELECT\b.*\bFROM\b",  # Any SELECT query (case-sensitive)
    r"\bOR\b\s*1\s*=\s*1",  # Common 1=1 injection pattern (case-sensitive)
    r"\b'(\d+|\w+)'",  # Looks for strings inside single quotes like 'admin' or '1' (case-sensitive)
    r"(\bDROP\b|\bDELETE\b)",  # DROP, DELETE (case-sensitive)
]

def waf_filter(user_input):
    """Checks if input matches any SQLi patterns."""
    for pattern in BLACKLIST_PATTERNS:
        if re.search(pattern, user_input):
            return True  # Block request
    return False

