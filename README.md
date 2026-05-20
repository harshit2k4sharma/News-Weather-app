# SkyCast & Chronicles AI: Modern News & Weather Dashboard

SkyCast & Chronicles AI is a premium, interactive web application that integrates live weather analytics and real-time news headlines into a cohesive dashboard, powered by an intelligent LangChain AI city assistant.

---

## 🌟 Key Features

### 🤖 **1. AI City Concierge & Assistant**
- An interactive chatbot powered by **Mistral AI (`mistral-small-2506`)**.
- Uses **LangChain Runnable Tools** (`get_weather` and `get_news`) to fetch live API data dynamically when asked about a city.
- Displays step-by-step tool execution logs (thought processes and parameters) right inside the chat window.

### 🌤️ **2. Live Weather Hub**
- Instantly look up live temperature, atmospheric metrics, and forecast updates.
- Premium UI with glassmorphic cards displaying:
  - Current temperature, "feels like" metrics, and weather conditions.
  - Custom emojis dynamically matching the weather state (sunny, rainy, cloudy, misty, etc.).
  - Wind speed, humidity, solar timelines (sunrise/sunset), and atmospheric pressure.

### 📰 **3. Chronicles Global News Feed**
- Enter any city or topic to retrieve real-time world headlines and articles powered by the high-speed **Tavily Search engine**.
- Shows elegant cards featuring publication titles, direct source links, and short summaries.

---

## 🛠️ Technology Stack

- **Frontend UI Framework**: [Streamlit](https://streamlit.io/) (High-performance Python web dashboard)
- **AI Agent Abstraction**: [LangChain](https://www.langchain.com/) (Runnable Chains, Custom Tools Binding)
- **Large Language Model (LLM)**: [Mistral AI API](https://mistral.ai/) (`mistral-small-2506`)
- **News/Web Search**: [Tavily Search API](https://tavily.com/)
- **Live Weather Data**: [OpenWeatherMap API](https://openweathermap.org/)
- **Style & Feel**: Vanilla CSS (Vibrant linear gradients, custom Google fonts, glassmorphism components)

---

## 🚀 Rapid Local Setup

Follow these simple steps to run the application on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/harshit2k4sharma/News-Weather-app.git
cd News-Weather-app
```

### 2. Set Up a Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory (never push this to GitHub!) and fill in your API credentials:
```env
# Mistral AI API Key
MISTRAL_API_KEY="your_mistral_api_key"

# Tavily Search API Key
TAVILY_API_KEY="your_tavily_api_key"

# OpenWeatherMap API Key
OPENWEATHER_API_KEY="your_openweather_api_key"
```

*Note: If you do not have these keys configured in your environment, you can also enter them directly in the Streamlit Sidebar override panel while the app is running!*

### 5. Launch the Application
```bash
streamlit run app.py
```

---

## 🔒 Security Best Practices
To prevent leakage of private keys and ensure project integrity:
- Private environment files (`.env`) and local environments (`.venv/`) are secured and excluded from GitHub using our preconfigured `.gitignore`.
- An environment template (`.env.example`) is provided so contributors can set up the app seamlessly.

---

## 🤝 Contributing
Contributions, feature requests, and bug reports are welcome! Feel free to open an issue or submit a pull request.

*Made with ❤️ by Harshit Sharma*
