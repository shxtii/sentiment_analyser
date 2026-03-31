# sentiment_analyser
# 🍽️ Sentiment Analysis of Product Reviews using Machine Learning

## 📌 Overview

This project is a machine learning-based web application that analyzes product reviews and classifies them into **Positive**, **Negative**, or **Neutral** sentiments.

It uses techniques from Natural Language Processing and a simple yet effective classification model to understand user opinions from text data.

---

## 🚀 Features

* Classifies reviews into **positive, negative, and neutral**
* Real-time prediction using a web interface
* Clean and simple UI built with Streamlit
* Lightweight and beginner-friendly implementation
* Uses TF-IDF for feature extraction

---

## 🧠 Technologies Used

* Python
* Pandas
* Scikit-learn
* NLTK
* Streamlit
* Joblib

---

## 📂 Project Structure

```
sentiment-analysis-app/
│── main.py              # Model training script
│── app.py               # Streamlit web app
│── data.csv             # Dataset
│── model.pkl            # Trained model
│── vectorizer.pkl       # TF-IDF vectorizer
│── README.md            # Project documentation
```

---

## 📊 How It Works

1. User enters a review
2. Text is preprocessed (cleaning, stopword removal)
3. Text is converted into numerical form using TF-IDF
4. Model predicts sentiment using Naive Bayes
5. Result is displayed instantly

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model

```bash
python main.py
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 🌐 Usage

* Open the local URL shown in terminal (usually `http://localhost:8501`)
* Enter any product review
* Click **Analyze**
* View the predicted sentiment

---

## 📈 Example

| Review                     | Prediction |
| -------------------------- | ---------- |
| "This product is amazing!" | Positive   |
| "Worst experience ever"    | Negative   |
| "It is okay"               | Neutral    |

---

## ⚠️ Limitations

* Small dataset may affect accuracy
* Cannot fully understand sarcasm
* Basic model (can be improved further)

---

## 🚀 Future Improvements

* Use larger datasets (Amazon/IMDb)
* Implement advanced models (Logistic Regression, Deep Learning)
* Add accuracy metrics and graphs
* Deploy application online

---

## 📌 Conclusion

This project demonstrates how machine learning and NLP can be applied to analyze text data and extract meaningful insights. It serves as a strong foundation for building more advanced AI applications.

---

## 👨‍💻 Author

**Shakti Kumar Chaturvedi**<BR>
**25BCE11229**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
