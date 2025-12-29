# ratelimiting.py
import time
import threading


class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        """
        rate: tokens added per second
        capacity: maximum bucket size
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.timestamp = time.monotonic()
        self.lock = threading.Lock()

    def allow(self, tokens: int = 1) -> bool:
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.timestamp
            self.timestamp = now

            # Refill tokens
            self.tokens = min(
                self.capacity,
                self.tokens + elapsed * self.rate
            )

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True

            return False


# Example usage
if __name__ == "__main__":
    limiter = TokenBucket(rate=5, capacity=10)  # 5 req/sec, burst of 10

    for i in range(20):
        if limiter.allow():
            print(f"Request {i}: allowed")
        else:
            print(f"Request {i}: rate limited")
        time.sleep(0.1)
