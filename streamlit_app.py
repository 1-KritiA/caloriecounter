import streamlit as st
import pandas as pd

# Create the reference DataFrame
data = {
    "Food": [
        "Cabbage", "Onion", "Spring Onion", "Olives", "Carrot", "Beetroot", "Cauliflower", "Broccoli", "Cucumber", 
        "Celery", "French Beans", "Spinach", "Avocado", "Lettuce", "Zuchinni", "Asparagus", "Bok Choy", "Ginger", 
        "Garlic", "Cheddar", "Gouda", "Curd", "Paneer", "Coconut", "Mushroom", "Seasame Seeds", "Flax Seeds", 
        "Blueberry", "Strawberry", "Walnut", "Almonds", "Pistachio", "Pine Nut", "Okra", "Tamarind", "Raw Banana", 
        "Potato", "Capsicum", "Jalapeno", "Tomato", "Eggplant", "Red Chilli", "Green Chilli", "White Rice", 
        "Brown Rice", "Basmati Rice", "Poha", "Puffed Rice", "Bajra", "Jowar", "Ragi", "Oats", "Sabudana", 
        "Butter", "Olive Oil"
    ],
    "Calories_per_100g": [
        25, 40, 32, 150, 41, 43, 25, 35, 15, 16, 31, 23, 160, 15, 17, 20, 12, 80, 149, 161, 142, 100, 264, 355, 27,
        750, 750, 57, 30, 655, 580, 448, 695, 44, 280, 89, 77, 31, 29, 22, 25, 23, 107, 130, 112, 118, 130, 402, 
        320, 378, 354, 390, 352, 204, 119
    ]
}

df = pd.DataFrame(data)

# App title
st.title("🥦 Food Calorie Calculator")

st.markdown("Enter the name of a food item and its weight (in grams). The app will calculate the total calories based on your reference list.")

# User input
food_input = st.text_input("Enter food name").strip()
weight_input = st.number_input("Enter weight in grams", min_value=0.0, step=10.0)

# Lookup and compute
if food_input:
    match = df[df["Food"].str.lower() == food_input.lower()]
    if not match.empty:
        cal_per_100g = match.iloc[0]["Calories_per_100g"]
        total_calories = (weight_input * cal_per_100g) / 100
        st.success(f"Calories per 100g of {food_input.title()}: {cal_per_100g} kcal")
        st.write(f"Total calories for {weight_input}g of {food_input.title()}: **{total_calories:.2f} kcal**")
    else:
        st.error("Food item not found in reference list.")
