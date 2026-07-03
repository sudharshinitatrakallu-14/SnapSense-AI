def detect_screenshot_type(text):

    text = text.lower()

    if "message yourself" in text or "type a message" in text:
        return "💬 WhatsApp Chat"

    elif "subject" in text or "from:" in text or "inbox" in text:
        return "📧 Email"

    elif "invoice" in text or "gst" in text or "total" in text:
        return "🧾 Invoice"

    elif "education" in text or "skills" in text or "experience" in text:
        return "📄 Resume"

    elif "marks" in text or "cgpa" in text or "grade" in text:
        return "🎓 Student Result"

    elif "http" in text or "www" in text:
        return "🌐 Website"

    elif "chapter" in text or "unit" in text:
        return "📝 Notes"

    else:
        return "❓ Unknown Screenshot"