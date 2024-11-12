import requests
import time
from functools import wraps

def retry(max_retries: int = 3, backoff_factor: float = 0.3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException:
                    retries += 1
                    time.sleep(backoff_factor * (2 ** retries))
            raise Exception("Max retries exceeded")
        return wrapper
    return decorator