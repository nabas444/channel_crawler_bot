import re

KEYWORDS = [
    "internship",
    "trainee",
    "fellowship",
    "junior",
    "entry level",
    "scholarship"
]

BLACKLIST = [
    "crypto", "bitcoin", "trading", "investment", "meme", "funny"
]

def is_relevant(text: str) -> bool:
    text = text.lower()

    # strong signals (must exist)
    strong_signals = [
        "internship",
        "trainee",
        "fellowship",
        "graduate",
        "entry level"
    ]

    # weak signals
    weak_signals = [
        "job", "position", "hiring", "opportunity", "apply"
    ]

    # spam signals
    blacklist = [
        "crypto", "bitcoin", "investment", "meme", "funny", "game"
    ]

    if any(bad in text for bad in blacklist):
        return False

    strong_score = sum(1 for s in strong_signals if s in text)
    weak_score = sum(1 for s in weak_signals if s in text)

    # AI-like decision logic
    return strong_score >= 1 and (strong_score + weak_score) >= 2


def extract_fields(text: str):
    text_lower = text.lower()

    job_type = "Not specified"

    if "internship" in text_lower:
        job_type = "Internship"
    elif "trainee" in text_lower:
        job_type = "Trainee"
    elif "graduate" in text_lower:
        job_type = "Graduate Program"
    elif "fellowship" in text_lower:
        job_type = "Fellowship"
    elif "scholarship" in text_lower:
        job_type = "Scholarship"

    location = "Not specified"
    if "addis ababa" in text_lower:
        location = "Addis Ababa"
    elif "ethiopia" in text_lower:
        location = "Ethiopia"
    elif "remote" in text_lower:
        location = "Remote"

    company = "Not specified"

    match = re.search(r"(fca|unicef|google|ethio telecom|world bank|amazon|alx)", text, re.IGNORECASE)
    if match:
        company = match.group(1)

    return {
        "company": company,
        "location": location,
        "job_type": job_type
    }


def clean_text(text: str):
    # remove channel tags like #Opportunity_Alerts
    text = re.sub(r"#\w+", "", text)

    # remove multiple empty spaces
    text = re.sub(r"\n\s*\n", "\n\n", text)

    return text.strip()


SEPARATOR = "━━━━━━━━━━━━━━━━━━"

def format_job(text: str):
    from engine import extract_fields, clean_text
    text = clean_text(text)
    f = extract_fields(text)
    return f"""💼 Type: {f['job_type']}
━━━━━━━━━━━━━━━━━━
📝 Details:{text}
━━━━━━━━━━━━━━━━━━
📌 Telegram Job Aggregator"""