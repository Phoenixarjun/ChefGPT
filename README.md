# 👨‍🍳 ChefGPT

**ChefGPT** is an AI-powered smart cooking assistant that helps you discover recipes, get personalized ingredient lists, and locate nearby grocery shops with real-time details like price, distance, and ratings — all in one elegant interface.

![image](https://github.com/user-attachments/assets/c8a98e1a-12b4-440e-ae59-676950ad725b)


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
