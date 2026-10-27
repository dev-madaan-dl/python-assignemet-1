from fastapi import APIRouter
import httpx
from schemas import JokeResponse

router = APIRouter()


@router.get("/joke", response_model=JokeResponse)
async def get_joke():
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get("https://v2.jokeapi.dev/joke/Any")
        data = response.json()

    if data["type"] == "single":
        return {"joke": data["joke"]}
    else:
        return {"joke": f"{data['setup']} ... {data['delivery']}"}
