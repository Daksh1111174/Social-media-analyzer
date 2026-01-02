# =====================================
# SOCIAL MEDIA TREND ANALYZER
# 3 TABS: FACEBOOK | TWITTER | REDDIT
# USER TOPIC → 500 WORDS → WORDCLOUD
# =====================================

import streamlit as st
import feedparser
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests

# -------------------------------------
# APP CONFIG
# -------------------------------------
st.set_page_config(page_title="Social Media Trend Analyzer", layout="centered")
st.title("📊 Social Media Trend Analyzer")
st.caption("Facebook | Twitter | Reddit – Topic Based WordCloud")

# -------------------------------------
# HELPER FUNCTIONS
# -------------------------------------

def generate_wordcloud(text):
    wc = WordCloud(
        width=900,
        height=450,
        background_color="white",
        max_words=500
    ).generate(text)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# ---------- REDDIT ----------
def fetch_reddit(topic):
    url = f"https://www.reddit.com/search.rss?q={topic}"
    feed = feedparser.parse(url)
    texts = [entry.title for entry in feed.entries]
    return " ".join(texts)

# ---------- TWITTER (SIMULATED via NEWS SEARCH) ----------
def fetch_twitter(topic):
    # Public news search used as Twitter-like text stream
    url = f"https://api.allorigins.win/raw?url=https://news.google.com/rss/search?q={topic}"
    feed = feedparser.parse(url)
    texts = [entry.title for entry in feed.entries]
    return " ".join(texts)

# ---------- FACEBOOK (SIMULATED via NEWS SEARCH) ----------
def fetch_facebook(topic):
    # Facebook public posts not accessible → simulated via news headlines
    url = f"https://api.allorigins.win/raw?url=https://news.google.com/rss/search?q={topic}+facebook"
    feed = feedparser.parse(url)
    texts = [entry.title for entry in feed.entries]
    return " ".join(texts)

# -------------------------------------
# TABS
# -------------------------------------
tab1, tab2, tab3 = st.tabs(["📘 Facebook", "🐦 Twitter", "👽 Reddit"])

# -------------------------------------
# FACEBOOK TAB
# -------------------------------------
with tab1:
    st.subheader("Facebook Trend Analysis")
    topic = st.text_input("Enter topic for Facebook:")

    if st.button("Generate Facebook WordCloud"):
        if topic:
            text = fetch_facebook(topic)
            generate_wordcloud(text)
        else:
            st.warning("Please enter a topic")

# -------------------------------------
# TWITTER TAB
# -------------------------------------
with tab2:
    st.subheader("Twitter Trend Analysis")
    topic = st.text_input("Enter topic for Twitter:")

    if st.button("Generate Twitter WordCloud"):
        if topic:
            text = fetch_twitter(topic)
            generate_wordcloud(text)
        else:
            st.warning("Please enter a topic")

# -------------------------------------
# REDDIT TAB
# -------------------------------------
with tab3:
    st.subheader("Reddit Trend Analysis")
    topic = st.text_input("Enter topic for Reddit:")

    if st.button("Generate Reddit WordCloud"):
        if topic:
            text = fetch_reddit(topic)
            generate_wordcloud(text)
        else:
            st.warning("Please enter a topic")
