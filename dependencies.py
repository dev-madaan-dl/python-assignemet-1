from fastapi import Header, HTTPException
from config import SUMMARY_API_KEY

REVOKED_KEYS = set()  # keys that have been explicitly disabled


async def verify_api_key(x_api_key: str = Header(...)):
    if not x_api_key or not x_api_key.strip():
        raise HTTPException(status_code=400, detail="API key cannot be empty")

    if len(x_api_key) < 10:
        raise HTTPException(status_code=400, detail="API key format is invalid")

    if x_api_key in REVOKED_KEYS:
        raise HTTPException(status_code=403, detail="API key has been revoked")

    if x_api_key != SUMMARY_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
