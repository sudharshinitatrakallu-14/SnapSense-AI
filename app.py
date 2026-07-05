import streamlit as st
from utils.ocr import extract_text
from utils.detector import detect_screenshot_type
from utils.summarizer import generate_summary
from utils.extractor import extract_information
from utils.report_generator import generate_report

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="SnapSense AI",
    page_icon="📷",
    layout="wide"
)

st.title("📷 SnapSense AI")
st.subheader("Upload → Analyze → Extract Insights")

st.divider()

# ---------------- UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    # Show image FIRST (prevents flicker)
    st.image(uploaded_file, caption="Uploaded Screenshot")

    # ---------------- OCR ----------------
    if (
        "ocr_text" not in st.session_state
        or st.session_state.get("file_name") != uploaded_file.name
    ):
        with st.spinner("Extracting text..."):
            st.session_state.ocr_text = extract_text(uploaded_file)
            st.session_state.file_name = uploaded_file.name

    extracted_text = st.session_state.ocr_text

    # ---------------- PROCESS ----------------
    screenshot_type = detect_screenshot_type(extracted_text)
    summary = generate_summary(screenshot_type, extracted_text)
    info = extract_information(extracted_text)
    report = generate_report(screenshot_type, summary, info, extracted_text)

    # ---------------- DASHBOARD ----------------
    st.divider()
    st.subheader("📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Lines", len(extracted_text.splitlines()))
    c2.metric("Emails", len(info["emails"]))
    c3.metric("Phones", len(info["phones"]))
    c4.metric("Websites", len(info["websites"]))

    # ---------------- OUTPUT ----------------
    st.subheader("🧠 Analysis")
    st.success(screenshot_type)

    st.subheader("🤖 Summary")
    st.info(summary)

    st.subheader("📄 Extracted Text")
    st.text_area("OCR Output", extracted_text, height=250)

    # ---------------- DOWNLOAD ----------------
    st.download_button(
        "Download Report",
        report,
        file_name="SnapSense_Report.txt",
        mime="text/plain"
    )

st.divider()
st.caption("SnapSense AI | Built by Sudharshini")