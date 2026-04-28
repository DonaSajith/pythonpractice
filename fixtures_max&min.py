import pytest

@pytest.fixture
def numbers():
    return [10, 20, 30]

def test_max(numbers):
    assert max(numbers) == 30

def test_min(numbers):
    assert min(numbers) == 10