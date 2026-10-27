from fastapi import FastAPI
from routers import joke, weather, summary
from exceptions import register_exception_handlers

app = FastAPI()

register_exception_handlers(app)

app.include_router(joke.router)
app.include_router(weather.router)
app.include_router(summary.router)
