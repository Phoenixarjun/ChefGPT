# 👨‍🍳 ChefGPT

**ChefGPT** is an AI-powered smart cooking assistant that helps you discover recipes, get personalized ingredient lists, and locate nearby grocery shops with real-time details like price, distance, and ratings — all in one elegant interface.

![ChefGPT Demo](https://images.unsplash.com/photo-1556912990-dac894c1c5f1?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80)

---

## 🧠 Powered By
- **Google Gemini Pro (via LangChain)** – for recipe generation and smart suggestions
- **Streamlit** – for a simple, interactive UI
- **SerpAPI** – for real-time shop data (distance, price, ratings)
- **LangChain Agents** – to reason, retrieve, and generate structured outputs

---

## 🔥 Features

- 🥘 Enter any dish name and preferred cuisine  
- 📋 Get step-by-step recipes and precise ingredient lists  
- 🛒 Select what you already have, and get a **smart shopping list**  
- 📍 Discover nearby shops with:
  - Shop Name  
  - Distance (km)  
  - Rating ⭐  
  - Estimated Price ₹  

---

## 🚀 How to Run

```bash
git clone https://github.com/Phoenixarjun/ChefGPT.git
cd ChefGPT
pip install -r requirements.txt
streamlit run main.py
