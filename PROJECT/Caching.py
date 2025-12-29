import time
from functools import lru_cache
import threading


# -------------------------------------------------
# 1️⃣ Simple LRU Cache (Function-level)
# -------------------------------------------------
@lru_cache(maxsize=128)
def get_square(n: int) -> int:
    """Caches function results automatically"""
    return n * n


# -------------------------------------------------
# 2️⃣ Manual In-Memory Cache (Dictionary)
# -------------------------------------------------
class InMemoryCache:
    def __init__(self):
        self.cache = {}
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            return self.cache.get(key)

    def set(self, key, value):
        with self.lock:
            self.cache[key] = value


memory_cache = InMemoryCache()


# -------------------------------------------------
# 3️⃣ TTL (Time-To-Live) Cache
# -------------------------------------------------
class TTLCache:
    def __init__(self, ttl_seconds: int):
        self.ttl = ttl_seconds
        self.store = {}
        self.lock = threading.Lock()

    def get(self, key):
        with self.lock:
            item = self.store.get(key)
            if not item:
                return None

            value, timestamp = item
            if time.time() - timestamp > self.ttl:
                del self.store[key]
                return None

            return value

    def set(self, key, value):
        with self.lock:
            self.store[key] = (value, time.time())


ttl_cache = TTLCache(ttl_seconds=10)


# -------------------------------------------------
# 4️⃣ Cached API Call Example
# -------------------------------------------------
def fetch_data(api_url):
    cached = ttl_cache.get(api_url)
    if cached:
        print("⚡ Returned from cache")
        return cached

    print("🌐 Fetching from API")
    # Simulate API call
    data = {"data": "sample response"}
    ttl_cache.set(api_url, data)
    return data


# -------------------------------------------------
# 5️⃣ Example Usage
# -------------------------------------------------
if __name__ == "__main__":
    print(get_square(4))
    print(get_square(4))  # Cached

    memory_cache.set("user:1", {"name": "Aravind"})
    print(memory_cache.get("user:1"))

    print(fetch_data("https://api.example.com/data"))
    time.sleep(2)
    print(fetch_data("https://api.example.com/data"))  # Cached