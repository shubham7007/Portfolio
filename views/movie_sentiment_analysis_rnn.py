import streamlit as st
import re
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

#app config
st.set_page_config(
    page_title="Movie Sentiment Analysis",
    layout="centered"
)

#Load Model and word index
@st.cache_resource
def load_rnn_model():
    return load_model("models/RNN/simple_rnn_imdb_V03.h5")

@st.cache_resource
def load_word_index():
    return imdb.get_word_index()

model = load_rnn_model()
word_index = load_word_index()

MAX_LEN = 500


with open("models/RNN/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

#Text Preprocessing
# def preprocess_text(text):
#     # text = text.lower()
#     # words = re.findall(r"\w+", text)
#     # encoded_review = [word_index.get(word, 2) for word in words]
#     # padded_review = sequence.pad_sequences(
#     #     [encoded_review],
#     #     maxlen=MAX_LEN
#     # )
#     seq = tokenizer.texts_to_sequences([text])
#     padded = pad_sequences(seq, maxlen = MAX_LEN)
#     return padded_review

def preprocess_text(text):
    seq = tokenizer.texts_to_sequences([text])
    padded_review = pad_sequences(seq, maxlen=MAX_LEN)
    return padded_review



#Prediction Function
def predict_sentiment(review):
    processed_input = preprocess_text(review)
    prediction = model.predict(processed_input)
    score = float(prediction[0][0])
    sentiment = "Positive" if score >= 0.5 else "Negative"
    return sentiment, score


#UI
st.title("Movie Review Sentiment Analysis")
st.write(
    "Enter a movie below and the RNN model will predict"
    "whether the sentiment is *Positive* or *Negative*."
)

review_text = st.text_area(
    "Enter your review here:",
    height = 150,
    placeholder = "This movie was absolutely amazing! The acting were fantastic"

)

#Prediction Button
if st.button("Predict Sentiment"):
    if review_text.strip() == "":
        st.warning("Enter Movie Review Before Prediction.")
    else:
        with st.spinner("Analyzing sentiment..."):
            sentiment, score = predict_sentiment(review_text)

        st.subheader("Prediction Result")
        st.write(f"Sentiment: {sentiment}")
        st.write(f"**Confidence Score: ** {score:.2f}")

        #visual Confidence bar
        st.progress(min(score, 1.0))

#Footer
st.markdown("---------")
st.caption("Built using RNN (SimpleRNN) + TensorFlow + Streamlit")
