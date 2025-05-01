import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Swiggy Recommender 🍔", layout="wide")

st.markdown("<h1 style='text-align: center;'>🍽️ Swiggy Restaurant Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Find your next favorite meal based on your mood, budget & taste!</p>", unsafe_allow_html=True)
st.markdown("---")

# ---- LOAD FILES ----
@st.cache_data
def load_files():
    df_cleaned = pd.read_csv("D:\\Data Science\\Projecct 4 Swiggy\\cleaned_data.csv")
    df_encoded = pd.read_csv("D:\\Data Science\\Projecct 4 Swiggy\\encoded_data.csv")
    with open("D:\\Data Science\\Projecct 4 Swiggy\\model.pkl", "rb") as f:
        encoder = pickle.load(f)
    return df_cleaned, df_encoded, encoder

df, df_encoded, encoder = load_files()

# ---- INPUT SECTION ----
with st.container():
    st.subheader("🔍 Tell us what you're craving...")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        city = st.selectbox("🏙️ City", sorted(df['city'].dropna().unique()))
    with col2:
        cuisine = st.selectbox("🍜 Cuisine", sorted(df['cuisine'].dropna().unique()))
    with col3:
        rating = st.slider("⭐ Minimum Rating", 1.0, 5.0, 4.0)
    with col4:
        cost = st.slider("💰 Max Cost for One (₹)", 50, 1000, 300)

# ---- RECOMMENDATION LOGIC ----
def get_recommendations(city, cuisine, rating, cost):
    try:
        user_input_df = pd.DataFrame([[city, cuisine]], columns=['city', 'cuisine'])
        user_encoded = encoder.transform(user_input_df).toarray()
        user_vector = np.hstack((user_encoded, [[rating, cost]]))
        similarity_scores = cosine_similarity(user_vector, df_encoded.values)
        top_indices = similarity_scores[0].argsort()[-5:][::-1]
        return df.iloc[top_indices]
    except Exception as err:
        st.error(f"Encoding failed: {err}")
        return pd.DataFrame()

# ---- OUTPUT SECTION ----
if st.button("🍴 Show Me Restaurants"):
    results = get_recommendations(city, cuisine, rating, cost)
    if not results.empty:
        st.success("✨ Here are your top picks!")
        for _, row in results.iterrows():
            st.markdown(f"""
                <div style="border:1px solid #ddd; border-radius:10px; padding:15px; margin-bottom:15px;">
                    <h4>{row['name']} 🍽️</h4>
                    <p><b>City:</b> {row['city']} | <b>Cuisine:</b> {row['cuisine']}</p>
                    <p><b>⭐ Rating:</b> {row['rating']} | <b>💵 Cost for One:</b> ₹{int(row['cost'])}</p>
                    <p><b>🏠 Address:</b> {row['address']}</p>
                    <a href="{row['link']}" target="_blank">
                        <button style="background-color:#ff4b4b; color:white; padding:8px 15px; border:none; border-radius:5px; cursor:pointer;">
                            🍴 Order Now
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No recommendations could be found with your criteria.")
