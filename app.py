import streamlit as st
import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="SkyCast & Chronicles AI",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Theme & Minimal CSS Styling
st.markdown("""
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Inter', sans-serif;
        background-color: #0d0f12 !important;
        color: #e2e8f0 !important;
    }
    
    /* Sidebar Styles */
    [data-testid="stSidebar"] {
        background-color: #12151c !important;
        border-right: 1px solid #1e2430 !important;
    }
    
    /* Headings */
    .app-title {
        color: #ffffff;
        font-weight: 700;
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }
    
    .app-subtitle {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 1.8rem;
    }
    
    /* Tabs Custom Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: #12151c;
        border-radius: 8px 8px 0px 0px;
        color: #94a3b8;
        padding-left: 16px;
        padding-right: 16px;
        border: 1px solid #1e2430;
        border-bottom: none;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #1a1f29 !important;
        color: #ffffff !important;
        border-color: #3b82f6 !important;
        font-weight: 600;
    }
    
    /* Minimalist Dark Cards */
    .dark-card {
        background-color: #12151c;
        border: 1px solid #1e2430;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    .weather-temp {
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff;
        margin: 0.2rem 0;
    }
    
    .weather-desc {
        text-transform: capitalize;
        font-weight: 500;
        color: #94a3b8;
        font-size: 1.1rem;
    }
    
    .metric-value {
        font-size: 1.3rem;
        font-weight: 600;
        color: #ffffff;
    }
    
    .metric-label {
        font-size: 0.8rem;
        color: #64748b;
        font-weight: 500;
    }
    
    .news-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #3b82f6;
        text-decoration: none;
        transition: color 0.15s ease;
    }
    
    .news-title:hover {
        color: #60a5fa;
        text-decoration: underline;
    }
    
    .news-source {
        font-size: 0.75rem;
        background: #1e2430;
        color: #94a3b8;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        font-weight: 500;
        display: inline-block;
        margin-top: 0.4rem;
        border: 1px solid #2e3748;
    }
    
    .news-snippet {
        color: #cbd5e1;
        font-size: 0.9rem;
        margin-top: 0.6rem;
        line-height: 1.45;
    }
    
    /* Sidebar Details Card */
    .sidebar-card {
        background: #1a1f29;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #2e3748;
        margin-bottom: 1rem;
    }
    
    /* High Visibility Chat Message Styling */
    [data-testid="stChatMessage"] {
        background-color: #181d28 !important;
        border: 1px solid #2d3748 !important;
        border-radius: 12px !important;
        padding: 1.2rem !important;
        margin-bottom: 1rem !important;
    }
    
    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] span, 
    [data-testid="stChatMessage"] li, 
    [data-testid="stChatMessage"] div {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 1rem !important;
        line-height: 1.55 !important;
    }

    [data-testid="stChatMessage"] a {
        color: #60a5fa !important;
        font-weight: 600 !important;
        text-decoration: underline !important;
    }

    [data-testid="stChatMessage"] strong {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    [data-testid="stChatMessage"] code {
        background-color: #2e3748 !important;
        color: #f87171 !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 4px !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- CREDENTIALS LOAD -----------------
# API Keys are loaded securely from environment / .env file
# They are never printed, displayed, or editable on the frontend interface
active_mistral = os.getenv("MISTRAL_API_KEY")
active_tavily = os.getenv("TAVILY_API_KEY")
active_weather = os.getenv("OPENWEATHER_API_KEY")


# ----------------- SIDEBAR INTERFACE -----------------
st.sidebar.markdown("<div style='margin-bottom: 1rem; font-size: 2.2rem;'>🌤️🤖</div>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='color: #ffffff; margin-top: 0;'>Settings Panel</h3>", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
st.sidebar.markdown("<span style='color: #94a3b8; font-size: 0.9rem;'><b>Status:</b> Connected to secure background service. API keys are loaded safely from environment files.</span>", unsafe_allow_html=True)
st.sidebar.markdown('</div>', unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
st.sidebar.markdown("<h5 style='color: #ffffff; margin-top:0;'>About Application</h5>", unsafe_allow_html=True)
st.sidebar.markdown("""
<span style='color: #94a3b8; font-size: 0.85rem;'>
<b>SkyCast & Chronicles AI</b> integrates live atmospheric metrics and real-time news search into a fast, dark-themed dashboard.

Built using:
- Streamlit
- LangChain Agents
- Mistral AI
- OpenWeather
- Tavily Search
</span>
""", unsafe_allow_html=True)
st.sidebar.markdown('</div>', unsafe_allow_html=True)


# ----------------- WEATHER HELPER FUNCTIONS -----------------
def get_weather_emoji(desc):
    desc = desc.lower()
    if "clear" in desc:
        return "☀️"
    elif "cloud" in desc:
        return "☁️"
    elif "drizzle" in desc or "rain" in desc:
        return "🌧️"
    elif "thunderstorm" in desc:
        return "⛈️"
    elif "snow" in desc:
        return "❄️"
    elif "mist" in desc or "haze" in desc or "fog" in desc:
        return "🌫️"
    return "🌤️"

def fetch_weather_details(city):
    if not active_weather:
        return {"error": "API key configuration error."}
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={active_weather}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if str(data.get("cod")) != "200":
            # Fallback suffix
            url_in = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={active_weather}&units=metric"
            response = requests.get(url_in)
            data = response.json()
            if str(data.get("cod")) != "200":
                return {"error": "City details not found."}
        
        return {
            "city": data.get("name"),
            "country": data.get("sys", {}).get("country"),
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"],
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%I:%M %p"),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%I:%M %p"),
        }
    except Exception:
        return {"error": "Unable to connect to weather data service."}


# ----------------- NEWS HELPER FUNCTIONS -----------------
def fetch_news_details(query):
    if not active_tavily:
        return {"error": "API key configuration error."}
    
    from tavily import TavilyClient
    try:
        tavily_client = TavilyClient(api_key=active_tavily)
        response = tavily_client.search(
            query=f"latest news {query}",
            search_depth="basic",
            max_results=5
        )
        return response.get("results", [])
    except Exception:
        return {"error": "Unable to fetch chronicles feed."}


# ----------------- AI ASSISTANT AGENT -----------------
def run_ai_assistant_agent(messages_list):
    if not active_mistral:
        return "Unable to start assistant. API key configuration error.", []
    
    from langchain_mistralai import ChatMistralAI
    from langchain.tools import tool
    from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, SystemMessage
    
    @tool
    def get_weather(city: str) -> str:
        """Get current weather of a city"""
        w_data = fetch_weather_details(city)
        if "error" in w_data:
            return f"Could not fetch weather for {city}."
        return f"Weather in {w_data['city']}, {w_data['country']}: {w_data['description']}, Temp: {w_data['temp']}°C, Feels like: {w_data['feels_like']}°C, Humidity: {w_data['humidity']}%, Wind: {w_data['wind_speed']} m/s."

    @tool
    def get_news(city_or_topic: str) -> str:
        """Get latest news about a city or general topic"""
        articles = fetch_news_details(city_or_topic)
        if isinstance(articles, dict) and "error" in articles:
            return "Could not retrieve news headlines."
        if not articles:
            return f"No news articles found for {city_or_topic}."
        
        news_list = []
        for r in articles:
            news_list.append(f"- **{r.get('title')}**\n  URL: {r.get('url')}\n  Summary: {r.get('content')[:120]}...")
        return f"Latest headlines in {city_or_topic}:\n\n" + "\n\n".join(news_list)
    
    tools_map = {
        "get_weather": get_weather,
        "get_news": get_news
    }
    
    llm = ChatMistralAI(model="mistral-small-2506", api_key=active_mistral)
    llm_with_tools = llm.bind_tools([get_weather, get_news])
    
    langchain_messages = [
        SystemMessage(content="You are SkyCast Assistant, a clean, minimal, and highly useful city guide. Answer user queries concisely and directly. If the user asks about weather or news, use the tools and integrate the findings cleanly. Always present source URLs in a neat format if giving news.")
    ]
    
    for m in messages_list:
        if m["role"] == "user":
            langchain_messages.append(HumanMessage(content=m["content"]))
        elif m["role"] == "assistant":
            langchain_messages.append(AIMessage(content=m["content"]))
            
    tool_calls_executed = []
    
    for step in range(5):
        res = llm_with_tools.invoke(langchain_messages)
        langchain_messages.append(res)
        
        if res.tool_calls:
            for tool_call in res.tool_calls:
                name = tool_call["name"]
                args = tool_call["args"]
                tool_calls_executed.append({"name": name, "args": args})
                
                if name in tools_map:
                    tool_output = tools_map[name].invoke(tool_call)
                    langchain_messages.append(tool_output)
                else:
                    langchain_messages.append(ToolMessage(
                        content="Tool not found.",
                        tool_call_id=tool_call["id"]
                    ))
        else:
            return res.content, tool_calls_executed
            
    return langchain_messages[-1].content, tool_calls_executed


# ----------------- MAIN INTERFACE -----------------
st.markdown("<h1 class='app-title'>SkyCast & Chronicles AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Real-time weather analytics and global news feed dashboard.</p>", unsafe_allow_html=True)

# Create tabs
tab_chat, tab_weather, tab_news = st.tabs([
    "🤖 AI Assistant Chatbot", 
    "🌤️ Live Weather Hub", 
    "📰 Chronicles News Feed"
])

# ================= TAB 1: AI ASSISTANT CHATBOT =================
with tab_chat:
    st.markdown("##### Chat Assistant")
    
    # Initialize message log
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello. I can assist you with real-time weather analytics or latest news headlines. Ask me about any city."}
        ]

    # Render previous logs
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("assistant"):
            with st.status("Thinking...", expanded=False) as status:
                ai_response, tool_calls = run_ai_assistant_agent(st.session_state.messages)
                
                if tool_calls:
                    for tc in tool_calls:
                        status.write(f"Executing: `{tc['name']}`")
                
                status.update(label="Complete", state="complete")
                
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})


# ================= TAB 2: LIVE WEATHER HUB =================
with tab_weather:
    st.markdown("##### Live Weather Lookups")
    
    col_input, _ = st.columns([2, 2])
    with col_input:
        weather_city = st.text_input("Enter City Name:", placeholder="e.g. Mumbai, New York...", key="w_input_box")
        weather_search_btn = st.button("Search Weather")

    if weather_search_btn or weather_city:
        if not weather_city:
            st.warning("Please enter a city name.")
        else:
            with st.spinner("Fetching..."):
                w = fetch_weather_details(weather_city)
                
                if "error" in w:
                    st.error(w["error"])
                else:
                    emoji = get_weather_emoji(w["description"])
                    st.markdown(f"**📍 Location: {w['city']}, {w['country']}**")
                    
                    # Columns for widgets
                    c1, c2, c3 = st.columns([1.5, 1.5, 1.5])
                    
                    with c1:
                        st.markdown(f"""
                        <div class="dark-card" style="text-align: center;">
                            <div style="font-size: 3.5rem;">{emoji}</div>
                            <div class="weather-temp">{w['temp']}°C</div>
                            <div class="weather-desc">{w['description']}</div>
                            <div style="margin-top: 0.8rem; color: #64748b; font-size: 0.85rem;">
                                Feels like: {w['feels_like']}°C
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with c2:
                        st.markdown(f"""
                        <div class="dark-card">
                            <div style="font-weight: 600; color: #ffffff; margin-bottom: 0.8rem; font-size: 0.95rem;">Atmospherics</div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 0.8rem;">
                                <div>
                                    <div class="metric-label">Min Temp</div>
                                    <div class="metric-value">{w['temp_min']}°C</div>
                                </div>
                                <div>
                                    <div class="metric-label">Max Temp</div>
                                    <div class="metric-value">{w['temp_max']}°C</div>
                                </div>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <div>
                                    <div class="metric-label">Humidity</div>
                                    <div class="metric-value">{w['humidity']}%</div>
                                </div>
                                <div>
                                    <div class="metric-label">Wind Speed</div>
                                    <div class="metric-value">{w['wind_speed']} m/s</div>
                                </div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with c3:
                        st.markdown(f"""
                        <div class="dark-card">
                            <div style="font-weight: 600; color: #ffffff; margin-bottom: 0.8rem; font-size: 0.95rem;">Daylight & Pressure</div>
                            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between;">
                                <span class="metric-label">🌅 Sunrise</span>
                                <span class="metric-value" style="font-size: 1rem;">{w['sunrise']}</span>
                            </div>
                            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between;">
                                <span class="metric-label">🌇 Sunset</span>
                                <span class="metric-value" style="font-size: 1rem;">{w['sunset']}</span>
                            </div>
                            <div style="display: flex; justify-content: space-between;">
                                <span class="metric-label">🎈 Pressure</span>
                                <span class="metric-value" style="font-size: 1rem;">{w['pressure']} hPa</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)


# ================= TAB 3: CHRONICLES NEWS FEED =================
with tab_news:
    st.markdown("##### Real-Time News Headlines")
    
    col_news, _ = st.columns([2, 2])
    with col_news:
        news_query = st.text_input("Enter Topic or City:", placeholder="e.g. AI technology, London...", key="n_input_box")
        news_search_btn = st.button("Search News")
        
    if news_search_btn or news_query:
        if not news_query:
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Searching..."):
                results = fetch_news_details(news_query)
                
                if isinstance(results, dict) and "error" in results:
                    st.error(results["error"])
                elif not results:
                    st.info("No reports found.")
                else:
                    for r in results:
                        st.markdown(f"""
                        <div class="dark-card">
                            <a class="news-title" href="{r.get('url')}" target="_blank">{r.get('title')}</a>
                            <div>
                                <span class="news-source">{r.get('url').split('//')[-1].split('/')[0]}</span>
                            </div>
                            <div class="news-snippet">{r.get('content')}</div>
                        </div>
                        """, unsafe_allow_html=True)
