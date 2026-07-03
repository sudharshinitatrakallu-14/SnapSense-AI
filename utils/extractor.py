import re


def extract_information(text):

    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

    phones = re.findall(r"\b\d{10}\b", text)

    dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)

    websites = re.findall(r"(https?://\S+|www\.\S+)", text)

    amounts = re.findall(r"(?:₹|Rs\.?|INR)?\s?\d+(?:,\d{3})*(?:\.\d{2})?", text)

    return {
        "emails": emails,
        "phones": phones,
        "dates": dates,
        "websites": websites,
        "amounts": amounts
    }