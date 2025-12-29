import os
import time
import logging
import requests
from functools import lru_cache
from dotenv import load_dotenv


# -------------------------------------------------
# 1️⃣ Secure Configuration
# -------------------------------------------------
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

if not API_KEY or not API_URL:
    raise EnvironmentError("API_KEY or API_URL missing")


# -------------------------------------------------
# 2️⃣ Logging Technique
# -------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# -------------------------------------------------
# 3️⃣ Simple Rate Limiting
# -------------------------------------------------
class SimpleRateLimiter:
    def __init__(self, rate_per_sec: float):
        self.interval = 1.0 / rate_per_sec
        self.last_call = 0.0

    def wait(self):
        elapsed = time.monotonic() - self.last_call
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_call = time.monotonic()


rate_limiter = SimpleRateLimiter(rate_per_sec=2)


# -------------------------------------------------
# 4️⃣ Caching Technique
# -------------------------------------------------
@lru_cache(maxsize=128)
def cached_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }


# -------------------------------------------------
# 5️⃣ Retry Technique
# -------------------------------------------------
def retry_request(url, retries=3, timeout=5):
    for attempt in range(1, retries + 1):
        try:
            rate_limiter.wait()
            response = requests.get(
                url,
                headers=cached_headers(),
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            logger.warning(f"Attempt {attempt} failed: {e}")
            time.sleep(attempt)  # exponential backoff

    logger.error("All retry attempts failed")
    return None


# -------------------------------------------------
# 6️⃣ Main Execution
# -------------------------------------------------
if __name__ == "__main__":
    logger.info("Starting secure API call")

    data = retry_request(API_URL)

    if data:
        logger.info("Data fetched successfully")
        print(data)
    else:
        logger.error("Failed to fetch data")