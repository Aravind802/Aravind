import os
from openai import AsyncOpenAI

# Create OpenAI async client
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def call_openai(prompt: str) -> str:
    """
    Calls OpenAI asynchronously and returns the response text.
    """
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content