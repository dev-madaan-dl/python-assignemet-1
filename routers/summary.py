from fastapi import APIRouter, Depends
from groq import Groq
from schemas import SummaryRequest, SummaryResponse
from dependencies import verify_api_key
from config import GROQ_API_KEY

router = APIRouter()

groq_client = Groq(api_key=GROQ_API_KEY)


@router.post("/summary", response_model=SummaryResponse, dependencies=[Depends(verify_api_key)])
async def summarize(request: SummaryRequest):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": f"Summarize this text in 2-3 sentences:\n\n{request.text}"}]
    )

    return {"summary": response.choices[0].message.content}
