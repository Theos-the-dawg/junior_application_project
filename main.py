from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for frontend testing (Bonus Task)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input model
class WebhookInput(BaseModel):
    data: str

# Output model
class WebhookOutput(BaseModel):
    word: List[str]

@app.post("/sort-characters", response_model=WebhookOutput)
def sort_characters(payload: WebhookInput):
    if not payload.data:
        raise HTTPException(status_code=400, detail="Field 'data' is required and must not be empty.")

    sorted_array = sorted(list(payload.data))
    return {"word": sorted_array}

