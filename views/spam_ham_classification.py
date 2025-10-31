import streamlit as st
import pickle
import gensim
import numpy as np
from nltk.stem import WordNetLemmatizer
import re
from nltk import sent_tokenize
from gensim.utils import simple_preprocess
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from gensim.models import Word2Vec, KeyedVectors
import gensim.downloader as api



#initialize session state

if "model_choice" not in st.session_state:
    st.session_state.model_choice = "Custom"

#button to switch model
col1, col2 = st.columns(2)
with col1:
    if st.button("Use Custom Word2vec"):
        st.session_state.model_choice = "Custom"
with col2:
    if st.button("Use Pretrained Glove/Wiki"):
        st.session_state.model_choice = "Pretrained"

#Load the selected model
if st.session_state.model_choice == "Custom":
    word2vec_model = gensim.models.Word2Vec.load("models/spam_ham_w2v.model")
    st.info("Using Custom Word2Vec (trained on coupus)")
else:
    word2vec_model = gensim.models.Word2Vec.load("models/glove_wiki_small.model")
    # word2vec_model = api.load("glove-wiki-gigaword-100")
    st.info("Using Pretrained Model")


# -----------------------------
# Load pickled models
# -----------------------------
classifier = pickle.load(open("models/spam_ham_model.pkl", "rb"))
# word2vec_model = gensim.models.Word2Vec.load("spam_ham_w2v.model")
lemmatizer = WordNetLemmatizer()

# -----------------------------
# Preprocessing for new messages
# -----------------------------
def preprocess_message(message, lemmatizer, model):
    review = re.sub("[^A-Za-z]", " ", message)
    review = review.lower().split()
    review = [lemmatizer.lemmatize(word) for word in review]
    cleaned_text = " ".join(review)

    words = []
    for sent in sent_tokenize(cleaned_text):
        words.extend(simple_preprocess(sent))

    vecs = [model.wv[word] for word in words if word in model.wv.index_to_key]
    if len(vecs) == 0:
        return np.zeros(model.vector_size)
    return np.mean(vecs, axis=0)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title(" Spam vs Ham Classifier")
st.write("Test your message below to see if it's spam or not.")

user_input = st.text_area("Enter a message:", height=150)

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message first.")
    else:
        vector = preprocess_message(user_input, lemmatizer, word2vec_model)

        # Handle feature mismatch (padding if needed)
        if len(vector) != classifier.n_features_in_:
            vector = np.pad(vector, (0, classifier.n_features_in_ - len(vector)), "constant")

        prediction = classifier.predict([vector])[0]
        label = " Ham (Not Spam)" if prediction == 0 else " Spam"
        st.success(f"Prediction: {label}")




#####Benchmarking Script

#loading data set for benchmarking 
from sklearn.model_selection import train_test_split
import pandas as pd

# Load your dataset
df = pd.read_csv("assets/SMSSpamcollection.txt",sep='\t',names=['label', 'message'])   
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], df['label'], test_size=0.2, random_state=42
)

# Tokenize test messages
X_test_tokens = [simple_preprocess(msg) for msg in X_test]




# Benchmarking function
# -----------------------------


##pad vectot is helping to sort 100 and 101 column mismatch issue in our skleanr classifer we will fix his ASAP
def pad_vector(vec, target_dim):
    """Ensure vector matches classifier input dimension."""
    if len(vec) < target_dim:
        return np.pad(vec, (0, target_dim - len(vec)), 'constant')
    elif len(vec) > target_dim:
        return vec[:target_dim]
    return vec




def vectorize_message(tokens, model):
    if hasattr(model, "wv"):
        vecs = [model.wv[w] for w in tokens if w in model.wv]
    else:
        vecs = [model[w] for w in tokens if w in model]
    return np.mean(vecs, axis=0) if vecs else np.zeros(model.vector_size)



def evaluate_model(model, X_tokens, y_true):
    X_vecs = []
    for tokens in X_tokens:
        vec = vectorize_message(tokens, model)
        vec = pad_vector(vec, classifier.n_features_in_)  # <-- fix applied here
        X_vecs.append(vec)
    X_vecs = np.array(X_vecs)

    y_pred = classifier.predict(X_vecs)
    return {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred),
        "Recall": recall_score(y_true, y_pred),
        "F1": f1_score(y_true, y_pred)
    }


if st.button("Run Benchmark"):
    # NOTE: You need to have X_test_tokens and y_test prepared beforehand
    # Example: X_test_tokens = [["free","win"], ["meeting","schedule"]]
    #          y_test = [1, 0]
    try:
        results_custom = evaluate_model(
            gensim.models.Word2Vec.load("models/spam_ham_w2v.model"),
            X_test_tokens, y_test
        )
        results_glove = evaluate_model(
            KeyedVectors.load("models/glove_wiki.model"),
            X_test_tokens, y_test
        )

        st.subheader("📊 Benchmark Results")
        st.table({
            "Custom Word2Vec": results_custom,
            "Glove Wiki": results_glove
        })
    except NameError:
        st.error("❌ Please define X_test_tokens and y_test before running the benchmark.")


