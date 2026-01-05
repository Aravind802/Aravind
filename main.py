import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import PromptRequest
from services.openai_service import call_openai
from services.claude_service import call_claude
from services.gemini_service import call_gemini

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

async def safe_call(func, prompt: str):
    try:
        return await func(prompt)
    except Exception as e:
        return f"Error: {str(e)}"

@app.post("/compare")
async def compare_llms(data: PromptRequest):
    prompt = data.prompt

    openai_res, claude_res, gemini_res = await asyncio.gather(
        safe_call(call_openai, prompt),
        safe_call(call_claude, prompt),
        safe_call(call_gemini, prompt),
    )

    return {
        "openai": openai_res,
        "claude": claude_res,
        "gemini": gemini_res
    }