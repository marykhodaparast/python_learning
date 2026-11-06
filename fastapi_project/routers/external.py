from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/external", tags=["External"])

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/users"

@router.get("/users")
async def get_external_users():
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(JSONPLACEHOLDER_URL)

        if response.status_code != 200:
            raise HTTPException(
                status_code=502,
                detail=f"External API error: {response.status_code}"
            )

        users = response.json()
        return [{"name": u["name"], "email": u["email"]} for u in users]

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="External API timed out")
    except httpx.RequestError:
        raise HTTPException(status_code=502, detail="Could not reach external API")