import pytest

@pytest.fixture(autouse=True)
def setup_env():
    print("\nSetting up environment")
    yield
    print("\nCleaning up environment")


def test_one():
    print("Running test one")
    assert True


def test_two():
    print("Running test two")
    assert True