import pytest

@pytest.fixture
def log_data():
    try:
        with open("sys.log") as file:
            return file.read()
    except FileNotFoundError:
        return None

def test_log(log_data):
    if log_data is None:
        assert False
    else:
        assert "ERROR" not in log_data
