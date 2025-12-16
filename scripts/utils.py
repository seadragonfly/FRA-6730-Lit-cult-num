import pandas as pd
import re, os, dateparser

def clean_text(text):
    if not isinstance(text, str):
        return text
    text = text.replace("\n", " ").lower()
    return text[:1].upper() + text[1:]


def capitalize_after_comma(text):
    if not isinstance(text, str):
        return text

    return re.sub(
        r',\s*([a-z])',
        lambda m: ', ' + m.group(1).upper(),
        text
    )

def make_continuous(text):
    if not isinstance(text, str):
        return text
    return " ".join(text.split())

def time_to_minutes(time_str):
    if not isinstance(time_str, str):
        return None

    parts = time_str.split("h")
    hours = int(parts[0])
    minutes = int(parts[1]) if len(parts) > 1 and parts[1] != "" else 0
    return hours * 60 + minutes


def split_date_range(text, season_start_year=2025):
    if not isinstance(text, str):
        return None, None

    text = text.strip().replace("-", "—")
    if "—" not in text:
        return text, None

    start, end = [p.strip() for p in text.split("—", 1)]

    def has_month(s):
        return any(c.isalpha() for c in s)

    # ensure both sides have a month
    if not has_month(start) and has_month(end):
        start = f"{start} {end.split()[-1]}"
    if not has_month(end) and has_month(start):
        end = f"{end} {start.split()[-1]}"

    def add_year_and_normalize(s):
        # first parse without year
        dt = dateparser.parse(s, languages=["fr"])
        if not dt:
            return s

        # season
        year = season_start_year if dt.month >= 8 else season_start_year + 1

        # re-parse with explicit year
        dt = dateparser.parse(f"{s} {year}", languages=["fr"])
        return dt.strftime("%d %B %Y")

    return add_year_and_normalize(start), add_year_and_normalize(end)



def split_names(text: str) -> list[str]:
    """
    Split a string of names on commas and the conjunction 'et'
    (French 'and'), returning a clean list of individual names.
    """
    if not isinstance(text, str):
        return None

    # Normalize whitespace and line breaks
    s = re.sub(r"\s+", " ", text.strip())

    # Split on commas or standalone 'et'
    parts = re.split(r"\s*,\s*|\s+et\s+", s, flags=re.IGNORECASE)

    # Clean and drop empty fragments
    return [p.strip() for p in parts if p.strip()]
