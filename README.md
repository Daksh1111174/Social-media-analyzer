# Social-media-analyzer
# 📊 Social Media Trend Analyzer

A Streamlit application that analyzes topic-based trends across Facebook, Twitter, and Reddit.

## 🚀 Features
- Three separate tabs: Facebook, Twitter, Reddit
- User-defined topic input
- Fetches ~500 words of text per platform
- Generates WordCloud for trend visualization
- No paid API keys required

## ⚠️ API Note
Due to restrictions on Facebook and Twitter APIs, public news feeds are used to simulate social media text streams for academic purposes.

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
