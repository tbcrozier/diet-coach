import streamlit as st
from llm import estimate_nutrition_with_ollama
from bq import insert_meal_to_bq

st.title("🍽️ Diet Coach")

user_id = st.text_input("Your ID (email or name)")
meal = st.text_area("What did you eat?")

if st.button("Log Meal"):
    if not user_id or not meal:
        st.error("Please enter both your name and your meal.")
    else:
        with st.spinner("Analyzing..."):
            nutrition, raw = estimate_nutrition_with_ollama(meal)
            insert_meal_to_bq(user_id, meal, nutrition or {}, raw)

        st.success("✅ Meal logged!")
        st.json(nutrition or {"message": "Could not parse nutrition."})
