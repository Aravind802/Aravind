import asyncio

async def call_gemini(prompt: str) -> str:
    # Simulate async API call
    await asyncio.sleep(1)
    return f"Gemini response to: {prompt}"