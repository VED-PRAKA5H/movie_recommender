import sys
import os
import nltk
import pandas as pd

from src.recommendation import recommend

import streamlit as st

import streamlit as st
import pandas as pd

# Custom CSS for glassmorphism with orange color
st.markdown("""
    <style>
    .glass {
        background: rgba(255, 165, 0, 0.1); /* Orange color with transparency */
        border-radius: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 165, 0, 0.3); /* Orange border */
        padding: 20px;
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
    st.write(pd.DataFrame({
        'movie list': recommend(option)
    }))

# Apply glassmorphism effect
# st.markdown('<div class="glass">', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

