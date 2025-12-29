import time
import threading


class AdaptiveRateLimiter:
    """
    Dynamically adjusts request rate based on API responses.
    Increases rate on success, decreases on failure (429/5xx).
    """

    def __init__(
        self,
        min_rate: float = 1.0,
        max_rate: float = 10.0,
        increase_factor: float = 1.1,
        decrease_factor: float = 0.5,
    ):
        self.min_rate = min_rate
        self.max_rate = max_rate
        self.rate = min_rate
        self.increase_factor = increase_factor
        self.decrease_factor = decrease_factor
        self.last_request_time = 0.0
        self.lock = threading.Lock()

    def wait(self):
        """Sleep if needed to respect current rate"""
        with self.lock:
            interval = 1.0 / self.rate
            now = time.monotonic()
            elapsed = now - self.last_request_time

            if elapsed < interval:
                time.sleep(interval - elapsed)

            self.last_request_time = time.monotonic()

    def on_success(self):
        """Call when request succeeds"""
        with self.lock:
            self.rate = min(self.rate * self.increase_factor, self.max_rate)

    def on_failure(self):
        """Call when request is rate-limited or fails"""
        with self.lock:
            self.rate = max(self.rate * self.decrease_factor, self.min_rate)

    def get_rate(self):
        return round(self.rate, 2)


# -------------------------------
# Example usage
# -------------------------------
if __name__ == "__main__":
    import random

    limiter = AdaptiveRateLimiter(
        min_rate=1,
        max_rate=5
    )

    for i in range(30):
        limiter.wait()

        # Simulate API response
        success = random.random() > 0.2  # 80% success rate

        if success:
            limiter.on_success()
            print(f"[{i}] ✅ Success | Rate = {limiter.get_rate()} req/s")
        else:
            limiter.on_failure()
            print(f"[{i}] ❌ Rate limited | Rate = {limiter.get_rate()} req/s")