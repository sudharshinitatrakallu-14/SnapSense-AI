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

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
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

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("# 📷 SnapSense AI")
st.markdown("### Upload • Analyze • Understand")

st.divider()

# --------------------------------------------------
# UPLOAD
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload Screenshot",
    type=["png", "jpg", "jpeg"]
)

# --------------------------------------------------
# PROCESS
# --------------------------------------------------
if uploaded_file is not None:

    st.success("✅ Screenshot uploaded successfully!")

    # Show image
    st.image(uploaded_file, caption="Uploaded Screenshot")

    # ---------------- OCR (CACHED SAFE VERSION) ----------------
    if (
        "ocr_text" not in st.session_state
        or st.session_state.get("file_name") != uploaded_file.name
    ):
        with st.spinner("🔍 Extracting text..."):
            st.session_state.ocr_text = extract_text(uploaded_file)
            st.session_state.file_name = uploaded_file.name

    extracted_text = st.session_state.ocr_text

    # ---------------- ANALYSIS ----------------
    screenshot_type = detect_screenshot_type(extracted_text)

    summary = generate_summary(screenshot_type, extracted_text)

    info = extract_information(extracted_text)

    report = generate_report(
        screenshot_type,
        summary,
        info,
        extracted_text
    )

    # ---------------- DASHBOARD ----------------
    st.divider()
    st.subheader("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Lines", len(extracted_text.splitlines()))
    col2.metric("📧 Emails", len(info["emails"]))
    col3.metric("📞 Phones", len(info["phones"]))
    col4.metric("🌐 Websites", len(info["websites"]))

    # ---------------- ANALYSIS ----------------
    st.subheader("🧠 Screenshot Analysis")
    st.success(f"Detected Type: {screenshot_type}")

    # ---------------- SUMMARY ----------------
    st.subheader("🤖 AI Summary")
    st.info(summary)

    # ---------------- INFO ----------------
    st.subheader("🔍 Extracted Information")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📧 Emails")
        st.write(info["emails"] or "No Email Found")

        st.markdown("### 📞 Phones")
        st.write(info["phones"] or "No Phone Found")

        st.markdown("### 💰 Amounts")
        st.write(info["amounts"] or "No Amount Found")

    with col2:
        st.markdown("### 📅 Dates")
        st.write(info["dates"] or "No Date Found")

        st.markdown("### 🌐 Websites")
        st.write(info["websites"] or "No Website Found")

    # ---------------- OCR TEXT ----------------
    st.divider()
    st.subheader("📄 Extracted Text")

    st.text_area("OCR Output", extracted_text, height=300)

    # ---------------- DOWNLOAD ----------------
    st.divider()
    st.subheader("📥 Download Report")

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="SnapSense_Report.txt",
        mime="text/plain"
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption("🚀 Developed by Sudharshini | SnapSense AI")
