import streamlit as st
import pandas as pd

# Create the reference DataFrame
foodlist = {
    "Food": [
        "Cabbage", "Onion", "Spring Onion", "Olives", "Carrot", "Beetroot", "Cauliflower", "Broccoli", "Cucumber", 
        "Celery", "French Beans", "Spinach", "Avocado", "Lettuce", "Zuchinni", "Asparagus", "Bok Choy", "Ginger", 
        "Garlic", "Cheddar", "Gouda", "Curd", "Paneer", "Coconut", "Mushroom", "Seasame Seeds", "Flax Seeds", 
        "Blueberry", "Strawberry", "Walnut", "Almonds", "Pistachio", "Pine Nut", "Okra", "Tamarind", "Raw Banana", 
        "Potato", "Capsicum", "Jalapeno", "Tomato", "Eggplant", "Red Chilli", "Green Chilli", "White Rice", 
        "Brown Rice", "Basmati Rice", "Poha", "Puffed Rice", "Bajra", "Jowar", "Ragi", "Oats", "Sabudana", 
        "Butter", "Olive Oil", "Egg White", "Ghee", "Coconut Oil", "Banana", "Fig", "Grapes", "Kiwi", "Orange", 
        "Papaya", "Pomegranate", "Watermelon", "Toor Dal", "Moong Dal", "Urad Dal", "Besan", "White Chana", 
        "Rajma", "Milk", "Almond Milk", "Peanuts", "Cashew", "Egg"
    ],
    "Calories_per_100g": [
        25, 40, 32, 150, 41, 43, 25, 35, 15, 16, 31, 23, 160, 15, 17, 20, 12, 80, 149, 161, 142, 100, 264, 355, 27,
        750, 750, 57, 30, 655, 580, 448, 695, 44, 280, 89, 77, 31, 29, 22, 25, 23, 107, 130, 112, 118, 130, 402, 
        320, 378, 354, 390, 352, 204, 119, 15, 120, 117, 84, 72, 67, 61, 47, 43, 68, 30, 318, 344, 350, 388, 246, 
        127, 61, 16.4, 568, 552, 75
    ]
}

df = pd.DataFrame(foodlist)

# App title
st.title("Food Calorie Calculator - Amura")
st.markdown("Enter the name of a food item (correct capitalisation) and its weight (in grams). I will calculate the total calories based on your reference list.")

# Number of items
num_items = st.number_input("How many items in your meal?", min_value=1, max_value=20, value=3, step=1)

meal_data = []
for i in range(num_items):
    st.markdown(f"#### Item {i+1}")
    col1, col2 = st.columns(2)
    with col1:
        food_input = st.text_input(f"Food name #{i+1}", key=f"food_{i}").strip()
    with col2:
        weight_input = st.number_input(f"Weight in grams #{i+1}", min_value=0.0, step=10.0, key=f"weight_{i}")
    
    # Only calculate if food name is filled
if food_input:
    food_name = food_input.lower()
    match = ref_df[ref_df["Food"].str.lower() == food_name]

    if not match.empty:
        cal_per_100g = match.iloc[0]["Calories_per_100g"]

        # Special case: Egg White → fixed 15 kcal per 26g
        if food_name == "egg white":
            total_calories = 15

        # Special case: Egg → fixed 75 kcal per egg
        elif food_name == "egg":
            total_calories = 75

        # Oils/Ghee measured in tablespoons (1 tbsp = 13.5g)
        elif food_name in ["olive oil", "ghee", "coconut oil"]:
            grams_per_tbsp = 13.5
            total_calories = (weight_input * grams_per_tbsp * cal_per_100g) / 100

        # Default gram-based calculation
        else:
            total_calories = (weight_input * cal_per_100g) / 100

        meal_data.append({
            "Food": food_input.title(),
            "Weight": f"{weight_input} {'tbsp' if food_name in ['olive oil', 'ghee', 'coconut oil'] else 'g'}",
            "Cal/100g": cal_per_100g,
            "Total Calories": round(total_calories, 2)
        })
    else:
        st.error(f"Item {i+1}: '{food_input}' not found in reference list.")


# --- Display Results ---
if meal_data:
    result_df = pd.DataFrame(meal_data)
    st.markdown("### 🧾 Meal Breakdown")
    st.dataframe(result_df, use_container_width=True)

    total_meal_cals = result_df["Total Calories"].sum()
    st.markdown(f"### 🧮 **Total Meal Calories: {total_meal_cals:.2f} kcal**")
