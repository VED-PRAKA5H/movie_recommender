import sys
import os
import nltk
import pandas as pd

from src.recommendation import recommend
import streamlit as st
import requests
def fetch_poster(movie_id):
    response = requests.get('


                            
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background: url('https://wallpaperset.com/w/full/2/2/a/521081.jpg') no-repeat center center fixed;
            background-size: cover;
            opacity: 0.7;
        }
        h1 {
            color: #FFAAAA;
        }
        .stSelectbox {
            background: rgba(58, 190, 249, 0.2);
            backdrop-filter: blur(10px);
            padding: 10px;
            border: 1px solid #3572EF;
            border-radius: 5px;
        }
        .stSelectbox:hover {
            background: rgba(58, 190, 249, 0.3);
        }
        .stButton {
            background-color: #3ABEF9;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .stButton:hover {
            background-color: #3572EF;
        }
        .stDataFrame {
            border-collapse: collapse;
            width: 100%;
        }
        .stDataFrame th, .stDataFrame td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .stDataFrame th {
            background-color: #A7E6FF;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title('Movie Recommender System')

# Load data
df = pd.read_csv('./data/processed.csv')

# Select box for movie titles
option = st.selectbox(
    'Which similar movies do you want?',
    df['title']
)

# Display selected option
st.write('You selected:', option)

# Recommendation button
if st.button('Recommend'):
    st.write(f"Here's your top ten similar movies to {option}:")
    recommended_movies = recommend(option)
    for movie in recommended_movies:
        st.write(movie)
