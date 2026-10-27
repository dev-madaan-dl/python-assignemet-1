from pydantic import BaseModel


class SummaryRequest(BaseModel):
    text: str


class JokeResponse(BaseModel):
    joke: str


class WeatherResponse(BaseModel):
    city: str
    temperature: str
    feels_like: str
    humidity: str
    condition: str


class SummaryResponse(BaseModel):
    summary: str
