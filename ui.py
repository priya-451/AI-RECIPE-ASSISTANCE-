import streamlit as st
from main import generate_recipe
st.title("AI Recipe Assistant")
ingredients = st.text_input("Enter the ingredients you have (comma-separated):")
if ingredients:
    ingredient_list = [ingredient.strip() for ingredient in ingredients.split(',')]
    response = generate_recipe(ingredient_list)
    st.markdown(response)