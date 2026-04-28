import pytest

@pytest.fixture
def api_client():
    print("\n🌐 Creating API client")
    client = {"base_url": "https://api.example.com"}
    return client


def test_endpoint(api_client):
    assert "https" in api_client["base_url"]