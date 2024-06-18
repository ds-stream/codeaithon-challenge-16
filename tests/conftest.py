import pytest


def pytest_addoption(parser):
    parser.addoption("--coder", action="store", default="default_value")


@pytest.fixture
def coder(request):
    return request.config.getoption("--coder")


# run pytest --coder=<number>