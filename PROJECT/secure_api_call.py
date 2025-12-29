import os
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_secure_session():
    """
    Creates a secure HTTP session with retries and backoff
    """
    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session


def secure_api_call():
    # Load environment variables
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_url = os.getenv("API_URL")

    if not api_key or not api_url:
        raise EnvironmentError("API_KEY or API_URL missing in .env file")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    session = create_secure_session()

    try:
        response = session.get(
            api_url,
            headers=headers,
            timeout=10  # Prevents hanging requests
        )

        response.raise_for_status()  # Raises error for 4xx/5xx
        return response.json()

    except requests.exceptions.Timeout:
        print("⏱ Request timed out")

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

    return None


if __name__ == "__main__":
    data = secure_api_call()
    if data:
        print("✅ API Response:")
        print(data)