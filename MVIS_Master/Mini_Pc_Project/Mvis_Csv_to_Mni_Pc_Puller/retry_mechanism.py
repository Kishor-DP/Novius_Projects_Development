#Copy and paste retry mechanism every where you want to use 

import time
from functools import wraps

def retry(exceptions, tries=31536063734300000, delay=1, backoff=2):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Retrying func2 in {_delay} seconds... ({_tries-1} tries left) due to {e}")
                    time.sleep(_delay)
                    _tries -= 1
                    #_delay *= backoff
            return func(*args, **kwargs)
        return wrapper_retry
    return decorator_retry

@retry(Exception, tries=31536063734300000, delay=1, backoff=0)
def test_function():
    print("Trying to perform an action...")
    # Simulate a failure
    raise Exception("Failed!")

try:
    test_function()
except Exception as e:
    print(f"Operation failed after retries: {e}")
