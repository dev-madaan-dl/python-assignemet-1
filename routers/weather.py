from fastapi import APIRouter, HTTPException
import httpx
from schemas import WeatherResponse
from config import OPENWEATHER_API_KEY

router = APIRouter()


@router.get("/weather", response_model=WeatherResponse)
async def get_weather(city: str):
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
        )
        data = response.json()

    if data.get("cod") != 200:
        raise HTTPException(status_code=404, detail=data.get("message", "City not found"))

    return {
        "city": data["name"],
        "temperature": f"{data['main']['temp']}°C",
        "feels_like": f"{data['main']['feels_like']}°C",
        "humidity": f"{data['main']['humidity']}%",
        "condition": data["weather"][0]["description"],
    }
