import asyncio

async def call_claude(prompt: str) -> str:
    # Simulate async API call
    await asyncio.sleep(1)
    return f"Claude response to: {prompt}"