from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        description="User prompt to send to all LLMs"
    )