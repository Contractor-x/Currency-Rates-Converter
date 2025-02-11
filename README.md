# 💰 Currency Converter

A **Python-based Currency Converter** with a **GUI (Tkinter) frontend** and a **separate backend module** for real-time exchange rate fetching. This project allows users to convert between different currencies using live exchange rates from the [ExchangeRate-API](https://www.exchangerate-api.com/).

## ✨ Features
✅ Real-time currency conversion using an API
✅ Simple and user-friendly GUI (Tkinter)
✅ Supports multiple currencies
✅ Error handling for invalid inputs
✅ Modular code (separate frontend and backend)

---

## 🚀 Installation & Setup

### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required packages:
```sh
pip install requests
```

### 2️⃣ Get an API Key
Sign up at [ExchangeRate-API](https://www.exchangerate-api.com/) to get a free API key.

### 3️⃣ Configure API Key
Replace `your_api_key_here` in **currency_backend.py** with your actual API key:
```python
API_KEY = "your_api_key_here"
```

### 4️⃣ Run the Application
Run the GUI script:
```sh
python currency_converter_gui.py
```

---

## 📂 Project Structure
```
📁 Currency Converter Project
│── currency_backend.py   # Backend - Fetches exchange rates & converts currency
│── currency_converter_gui.py  # Frontend - Tkinter GUI for user interaction
│── README.md   # Project Documentation
```

---

## 🛠 Usage
1️⃣ Enter the **amount** you want to convert.  
2️⃣ Specify the **base currency** (e.g., USD).  
3️⃣ Specify the **target currency** (e.g., EUR).  
4️⃣ Click **Convert** to see the result.  

---

## 🎯 Example
```
Amount: 100
From Currency: USD
To Currency: EUR

Output: 100 USD = 92.50 EUR
```

---

## 🏆 Future Improvements
🚀 Improve UI with modern styling (e.g., PyQt, custom Tkinter themes)  
📈 Add currency conversion history and charts  
🔄 Enable offline mode with cached exchange rates  
📊 Support for cryptocurrency conversions  

---

## 🤝 Contribution
Feel free to fork this repository and submit pull requests! Suggestions and improvements are always welcome. 😊

---

## ⚡ Author
👨‍💻 **Your Name**  
🔗 https://github.com/Contractor-x  
📧 dada4ash@gmail.com  

---

## 📜 License
This project is open-source and available under the **MIT License**.

