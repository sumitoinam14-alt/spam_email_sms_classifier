import pickle
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Spam Email/SMS Classifier",
    page_icon="📧",
    layout="centered"
)

# Load model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load vectorizer
with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Title
st.title("📧 Spam Email/SMS Classifier")
st.write("This application predicts whether an email or SMS is **Spam** or **Not Spam** using Machine Learning.")

# Text input
message = st.text_area(
    "Enter your message",
    height=180,
    placeholder="Type or paste your email/SMS here..."
)

# Predict button
if st.button("🔍 Predict", use_container_width=True):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        message_vector = vectorizer.transform([message])
        prediction = model.predict(message_vector)[0]

        st.divider()

        if prediction == 1:
            st.error("🚨 Prediction: SPAM")
        else:
            st.success("✅ Prediction: NOT SPAM")
