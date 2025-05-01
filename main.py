import streamlit as st
import chef_helper

st.set_page_config(page_title="ChefGPT", page_icon="👨‍🍳")
st.title("👨‍🍳 ChefGPT: Your AI Sous-Chef for Smart Cooking")

location = st.sidebar.text_input("📍 Enter your location", "Chrompet")
cuisine = st.sidebar.selectbox("🍽️ Select Cuisine", ("Indian", "Italian", "Chinese", "Mexican", "Thai", "Japanese", "French"))
dish = st.sidebar.text_input("🥘 Dish to cook", "")

# Ingredient state
if dish:
    if "ingredients" not in st.session_state:
        st.session_state.ingredients = chef_helper.generate_dish_ingredients_list(cuisine, dish)

    selected_items = []
    with st.sidebar.container():
        st.markdown("### 🧂 Ingredients from Recipe")
        for item in st.session_state.ingredients:
            if st.checkbox(item, value=True, key=f"chk_{item}"):
                selected_items.append(item)

        st.markdown("**🛒 Final Shopping List:**")
        st.write(", ".join(selected_items) if selected_items else "No items selected.")

        if st.button("✅ Confirm Selection & Generate Details"):
            st.session_state.selected_items = selected_items
            st.session_state.show_output = True

# Show results
if "show_output" in st.session_state and st.session_state.show_output:
    recipe, shops = chef_helper.generate_recipe_info_and_other_details(
        dish, st.session_state.selected_items, location
    )

    st.header("👨 Cooking Procedure")
    st.markdown(recipe)

    st.header("🛍️ Shopping Assistance")

    if shops:
        st.write(shops)
    else:
        st.warning("Couldn't fetch detailed shop data.")
