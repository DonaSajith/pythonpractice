import pytest

@pytest.fixture
def temp_file():
    filename = "temp.txt"

    with open(filename, "w") as f:
        f.write("Hello pytest")

    yield filename

    import os
    os.remove(filename)


def test_file(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()

    assert content == "Hello pytest"