# Assignment 1 API

A FastAPI service that wraps weather and joke APIs and provides authenticated
text summaries using Groq.

## Setup

Requires Python 3.14 or newer. Install the project dependencies:

```powershell
py -m pip install -e .
```

Set these environment variables before starting the service (or put them in a
`.env` file in the project directory):

| Variable | Purpose |
| --- | --- |
| `OPENWEATHER_API_KEY` | OpenWeather API key used by `GET /weather` |
| `GROQ_API_KEY` | Groq API key used by `POST /summary` |
| `SUMMARY_API_KEY` | Client key required in the `X-API-Key` header for `POST /summary` |

Start the development server:

```powershell
py -m uvicorn app:app --reload
```

The interactive API documentation is available at <http://127.0.0.1:8000/docs>.

## Endpoints

- `GET /weather?city=London` returns the city, temperature in Celsius, humidity
  as a percentage value, and the current condition. A missing city returns 404;
  upstream failures return 502.
- `GET /joke` returns a random joke and its category.
- `POST /summary` accepts `{"text": "..."}` and requires the `X-API-Key` header.
  Text must contain non-whitespace characters and be no longer than 10,000
  characters. Groq's `openai/gpt-oss-20b` generates a concise summary, which
  the prompt asks to keep to 2-3 sentences.

Example summary request:

```powershell
Invoke-RestMethod -Method Post `
  -Uri http://127.0.0.1:8000/summary `
  -Headers @{ "X-API-Key" = $env:SUMMARY_API_KEY } `
  -ContentType "application/json" `
  -Body '{"text":"Text to summarize"}'
```
