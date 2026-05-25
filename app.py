# loading saved model and vectorizer, building a professional streamlit ui with confidence bar and model info

import streamlit as st
import joblib
import os

st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

st.title("Fake News Detector")
st.write("Paste a news article or headline below and the model will classify it as Real or Fake.")

user_input = st.text_area("Enter news text here:", height=200)

if st.button("Analyze", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        input_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(input_tfidf)[0]
        confidence = model.predict_proba(input_tfidf)[0]

        st.markdown("---")
        st.markdown("### Result")

        if prediction == 0:
            confidence_score = confidence[0]
            st.error("🚨 Fake News Detected")
        else:
            confidence_score = confidence[1]
            st.success("✅ Real News")

        st.markdown(f"**Confidence:** {confidence_score * 100:.2f}%")
        st.progress(float(confidence_score))

st.markdown("---")

st.markdown(
    "**About the Model:** This detector uses Logistic Regression trained on TF-IDF features (10,000 words) "
    "across 116,993 news articles from two datasets — WELFake and Fake and Real News Dataset. "
    "The model achieves 95.4% accuracy on the test set."
)

st.caption(
    "⚠️ **Disclaimer:** This model is trained on US political news from 2015–2018. "
    "It may misclassify articles from other regions, languages, or time periods. "
    "The model detects writing patterns — it does not fact-check. "
    "Use results as a reference only."
)

st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://github.com/naveedamar/Bahria-University-Labs/tree/main/artificial-intelligence/fake-news-detector' target='_blank'>"
    "<button style='background-color: #24292e; color: white; padding: 8px 20px; border: none; border-radius: 6px; cursor: pointer; font-size: 14px;'>"
    "📂 View on GitHub</button></a></div>",
    unsafe_allow_html=True
)