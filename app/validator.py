import re

FORBIDDEN_KEYWORDS = [
    "drop",
    "delete",
    "update",
    "insert",
    "alter",
    "truncate",
    "create"
]

FORBIDDEN_PATTERN = re.compile(
    r"\b(" + "|".join(FORBIDDEN_KEYWORDS) + r")\b",
    re.IGNORECASE
)

def validate_sql(sql: str) -> None:
    if not sql.strip().lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed")

    match = FORBIDDEN_PATTERN.search(sql)
    if match:
        raise ValueError(
            f"Forbidden SQL operation detected: {match.group(0).upper()}"
        )
