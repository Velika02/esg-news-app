# real-time/app.py - ESG Real-Time News Monitor (displays ESG news, no risk extraction)

import streamlit as st
import os
import sys

# Add parent path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from news_api import fetch_company_esg_news

st.set_page_config(page_title="ESG Real-Time News Monitor", layout="centered")

st.markdown("[🔙 Back to ESG Main Site](https://velika02.github.io/5105-esg-dashboard/)", unsafe_allow_html=True)

st.title("🌍 ESG Real-Time News Monitor")

st.markdown("""
Retrieve recent ESG-related news based on company name.
""")

# Input
company = st.text_input("Enter company name", "Nestle")
max_articles = st.slider("Maximum number of articles", 1, 20, 5)

if company:
    with st.spinner("🔍 Fetching ESG news..."):

        # Fetch news
        news_list = fetch_company_esg_news(company, max_results=max_articles)

        if not news_list:
            st.warning("❗ No relevant news found. Please check the company name or your network connection.")
        else:
            for article in news_list:
                st.markdown(f"### 📰 {article['title']}")
                st.write(article['content'])
                st.markdown(f"[🔗 Read full article]({article['url']})")

