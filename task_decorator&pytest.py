import pytest
@pytest.fixture
import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print("execution_time:", end-start)
        return result
    return wrapper

@timer
def multiply(a, b):
    return a * b

def test_multiplication():
    result = multiply(4, 3)
    assert result == 12