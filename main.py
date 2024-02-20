from dotenv import load_dotenv
import streamlit as st


import llm_helper


load_dotenv()

st.title("Pet Namer")

animal_type = st.sidebar.selectbox("Select animal type", ["dog", "cat", "bird", "fish"])

pet_color = st.sidebar.text_area(f"What is your {animal_type} color?", max_chars=15)

number_of_names = st.sidebar.slider("Number of names", 1, 10, 5)

output = llm_helper.pet_namer(animal_type, number_of_names, pet_color)

st.write(output)
