import os
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# App settings
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "15"))