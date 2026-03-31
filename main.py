import pandas as pd
import string
import nltk
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('stopwords')

# =========================
# LOAD CSV DATASET
# =========================
data = pd.read_csv('data.csv')

# Remove missing values
data = data.dropna()

# =========================
# TEXT CLEANING
# =========================
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in string.punctuation])
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

data['text'] = data['text'].apply(clean_text)

# =========================
# FEATURE EXTRACTION
# =========================
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']

# =========================
# MODEL TRAINING
# =========================
model = MultinomialNB()
model.fit(X, y)

# =========================
# SAVE MODEL
# =========================
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("✅ Model trained successfully!")