import pytest

@pytest.fixture(scope="module")
def setup_data():
    print("\n📦 Setup runs once per module")
    return {"user": "admin", "role": "tester"}


def test_user(setup_data):
    assert setup_data["user"] == "admin"

def test_role(setup_data):
    assert setup_data["role"] == "tester"