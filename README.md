
# 🌦️ Weather API Backend (FastAPI)

A lightweight backend for the Weather App using FastAPI. It securely fetches:

- 🌡️ Current weather
- 📈 5-day forecasts
- 🌫️ Air Quality Index (AQI)
- 📍 Coordinates

---

## 🧰 Tech Stack

- Python 🐍
- FastAPI ⚡
- OpenWeatherMap API
- `python-dotenv` for secure API keys

---

## 🚀 Deployment (Recommended: Render)

1. Go to [Render.com](https://render.com)
2. Create a new **Web Service**
3. Connect this GitHub repo
4. Set:

   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port 10000`
   - **Environment variable:**
     ```
     OPENWEATHER_API_KEY = your_actual_key_here
     ```

✅ You’ll get a public API endpoint like:
```
https://your-app-url.onrender.com/weather?location=Delhi&unit=metric
```

---

## 🔐 Local Setup (Optional)

Create a `.env` file with:
```
OPENWEATHER_API_KEY=your_actual_api_key
```

Run locally:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## API Endpoint

`GET /weather?location=<city_or_zip>&unit=metric|imperial`

Example:
```
/weather?location=London&unit=metric
```

---

## 🤝 License

MIT — free to use, customize, and deploy
