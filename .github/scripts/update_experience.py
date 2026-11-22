
from datetime import date
from pathlib import Path

README = Path("README.md")
today = date.today()

# Replace with exact employment dates if available.
periods = [
    (date(2023, 1, 1), date(2024, 10, 1)),
    (date(2025, 1, 1), today),
]

# Calculate cumulative employment days.
total_days = sum(
    max(0, (min(end, today) - start).days)
    for start, end in periods
)

years = total_days / 365.2425

experience = (
    f"{years:.1f}+ years of professional experience"
    if years >= 4
    else f"Nearly 4 years of professional experience"
)

content = README.read_text(encoding="utf-8")
marker = "<!-- EXPERIENCE_YEARS -->"

if marker not in content:
    raise ValueError("Experience marker not found.")

import re

content = re.sub(
    r"\*\*Professional Experience:\*\*.*",
    f"**Professional Experience:** {experience} {marker}",
    content,
)

README.write_text(content, encoding="utf-8")

print(f"Experience updated: {experience}")
