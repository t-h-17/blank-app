import streamlit as st
# NLP Pkgs
from textblob import TextBlob
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import re



def clean_text(text):
    # Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # Removes Whitespaces
    text = re.sub(r"\'s", " ", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)
    return text

# GUI
st.title("Sentiment Analysis")
st.subheader("Enter text")
user_input = st.text_area("Text", height=200)

# Analyze Button
if st.button("Analyze"):
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity
    result = sentiment_score

    if result > 0:
        custom_emoji = ':blush:'
        st.success('Happy : {}'.format(custom_emoji))
    elif result < 0:
        custom_emoji = ':disappointed:'
        st.warning('Sad : {}'.format(custom_emoji))
    else:
        custom_emoji = ':confused:'
        st.info('Confused : {}'.format(custom_emoji))

    st.success("Polarity Score is: {}".format(result))
