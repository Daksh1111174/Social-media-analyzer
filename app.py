# =====================================
# SOCIAL MEDIA TREND ANALYZER
# NO feedparser | STREAMLIT CLOUD SAFE
# =====================================

import streamlit as st
import requests
import xml.etree.ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# -------------------------------------
# APP CONFIG
# -------------------------------------
st.set_page_config(page_title="Social Media Trend Analyzer", layout="centered")
st.title("📊 Social Media Trend Analyzer")
st.caption("Facebook | Twitter | Reddit – Topic Based WordCloud")

# -------------------------------------
# HELPER FUNCTIONS
# -------------------------------------
def fetch_rss_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    root = ET.fromstring(response.content)

    titles = []
    for item in root.findall(".//item/title"):
        if item.text:
            titles.append(item.text)

    return " ".join(titles)


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

# -------------------------------------
# TABS
# -------------------------------------
tab1, tab2, tab3 = st.tabs(["📘 Facebook", "🐦 Twitter", "👽 Reddit"])

# -------------------------------------
# FACEBOOK TAB (SIMULATED)
# -------------------------------------
with tab1:
    topic = st.text_input("Enter topic for Facebook:")
    if st.button("Generate Facebook WordCloud"):
        if topic:
            url = f"https://news.google.com/rss/search?q={topic}+facebook"
            text = fetch_rss_text(url)
            generate_wordcloud(text)
        else:
            st.warning("Please enter a topic")

# -------------------------------------
# TWITTER TAB (SIMULATED)
# -------------------------------------
with tab2:
    topic = st.text_input("Enter topic for Twitter:")
    if st.button("Generate Twitter WordCloud"):
        if topic:
            url = f"https://news.google.com/rss/search?q={topic}+twitter"
            text = fetch_rss_text(url)
            generate_wordcloud(text)
        else:
            st.warning("Please enter a topic")

# -------------------------------------
# REDDIT TAB (REAL DATA)
# -------------------------------------
with tab3:
    topic = st.text_input("Enter topic for Reddit:")
    if st.button("Generate Reddit WordCloud"):
        if topic:
            url = f"https://www.reddit.com/search.rss?q={topic}"
            text = fetch_rss_text(url)
            generate_wordcloud(text)
        else:
            st.warning("Please enter a topic")

