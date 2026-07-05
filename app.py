import streamlit as st
from utils.ocr import extract_text
from utils.detector import detect_screenshot_type
from utils.summarizer import generate_summary
from utils.extractor import extract_information
from utils.report_generator import generate_report

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="SnapSense AI",
    page_icon="📷",
    layout="wide"
)
with st.sidebar:

    st.title("📷 SnapSense AI")

    st.markdown("---")

    st.success("Modules")

    st.write("✅ OCR")
    st.write("✅ Screenshot Detection")
    st.write("✅ AI Summary")
    st.write("✅ Information Extraction")
    st.write("✅ Report Generation")

    st.markdown("---")

    st.info("Python + EasyOCR + Streamlit")
    #st.image("logo.png", width=120)
# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
# 📷 SnapSense AI

### Upload • Analyze • Understand

Analyze screenshots using OCR and intelligent text extraction.
""")

st.markdown("""
Welcome to **SnapSense AI** 🚀

### Features
- 📄 OCR Text Extraction
- 🧠 Screenshot Type Detection
- 🤖 AI Summary
- 🔍 Information Extraction
- 📊 Dashboard
- 📥 Download Report
""")

st.divider()

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload Screenshot",
    type=["png", "jpg", "jpeg"]
)

# --------------------------------------------------
# PROCESS IMAGE
# --------------------------------------------------
if uploaded_file is not None:

    st.success("✅ Screenshot uploaded successfully!")

    # Show uploaded screenshot
    st.image(
    uploaded_file,
    caption="Uploaded Screenshot",
    width="stretch"
)

    # OCR
   if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = extract_text(uploaded_file)

extracted_text = st.session_state.ocr_text

    # Detect screenshot type
    screenshot_type = detect_screenshot_type(extracted_text)

    # Summary
    summary = generate_summary(
        screenshot_type,
        extracted_text
    )

    # Extract important information
    info = extract_information(extracted_text)

    # Generate report
    report = generate_report(
        screenshot_type,
        summary,
        info,
        extracted_text
    )

    # --------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------
    st.divider()
    st.subheader("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Lines", len(extracted_text.splitlines()))

    with col2:
        st.metric("📧 Emails", len(info["emails"]))

    with col3:
        st.metric("📞 Phones", len(info["phones"]))

    with col4:
        st.metric("🌐 Websites", len(info["websites"]))

    st.divider()

    # --------------------------------------------------
    # SCREENSHOT ANALYSIS
    # --------------------------------------------------
    st.subheader("🧠 Screenshot Analysis")
    st.success(f"Detected Type: {screenshot_type}")

    # --------------------------------------------------
    # SUMMARY
    # --------------------------------------------------
    st.subheader("🤖 AI Summary")
    st.info(summary)

    st.divider()

    # --------------------------------------------------
    # INFORMATION EXTRACTION
    # --------------------------------------------------
    st.subheader("🔍 Important Information")

    left, right = st.columns(2)

    with left:

        st.markdown("### 📧 Emails")
        if info["emails"]:
            for email in info["emails"]:
                st.success(email)
        else:
            st.info("No Email Found")

        st.markdown("### 📞 Phone Numbers")
        if info["phones"]:
            for phone in info["phones"]:
                st.success(phone)
        else:
            st.info("No Phone Number Found")

        st.markdown("### 💰 Amounts")
        if info["amounts"]:
            for amount in info["amounts"]:
                st.success(amount)
        else:
            st.info("No Amount Found")

    with right:

        st.markdown("### 📅 Dates")
        if info["dates"]:
            for date in info["dates"]:
                st.success(date)
        else:
            st.info("No Date Found")

        st.markdown("### 🌐 Websites")
        if info["websites"]:
            for website in info["websites"]:
                st.success(website)
        else:
            st.info("No Website Found")

    st.divider()

    # --------------------------------------------------
    # OCR OUTPUT
    # --------------------------------------------------
    st.subheader("📄 Extracted Text")

    st.text_area(
        "OCR Output",
        extracted_text,
        height=300
    )

    st.divider()

    # --------------------------------------------------
    # DOWNLOAD REPORT
    # --------------------------------------------------
    st.subheader("📥 Download Report")

    st.download_button(
        label="📄 Download Analysis Report",
        data=report,
        file_name="SnapSenseAI_Report.txt",
        mime="text/plain"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption("🚀 Developed by Sudharshini | SnapSense AI")
