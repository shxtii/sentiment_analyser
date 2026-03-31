import streamlit as st
import joblib
import string
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Text cleaning
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

# UI
st.title("💬 Sentiment Analysis App")
st.write("Enter a sentence to analyze sentiment")

user_input = st.text_area("Your Text Here")

if st.button("Analyze"):
    if user_input:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 'positive':
            st.success("😊 Positive Sentiment")
        elif prediction == 'negative':
            st.error("😞 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")
    else:
        st.warning("Please enter some text")