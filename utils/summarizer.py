def generate_summary(screenshot_type, text):

    text = text.strip()

    if screenshot_type == "💬 WhatsApp Chat":
        return (
            "This screenshot appears to be a WhatsApp chat. "
            "The extracted conversation mainly contains:\n\n"
            + text[:250]
        )

    elif screenshot_type == "📧 Email":
        return (
            "This screenshot appears to be an Email containing communication details."
        )

    elif screenshot_type == "🧾 Invoice":
        return (
            "This screenshot appears to be an Invoice containing billing information."
        )

    elif screenshot_type == "📄 Resume":
        return (
            "This screenshot appears to be a Resume containing education, skills and experience."
        )

    elif screenshot_type == "🎓 Student Result":
        return (
            "This screenshot contains student marks or academic results."
        )

    elif screenshot_type == "🌐 Website":
        return (
            "This screenshot appears to be a Website."
        )

    elif screenshot_type == "📝 Notes":
        return (
            "This screenshot contains study notes."
        )

    else:
        return (
            "Summary could not be generated because the screenshot type is unknown."
        )