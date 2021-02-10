import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
    )
    parser.addoption(
        "--method",
        default="get",
    )
    parser.addoption(
        "--status_code",
        default=200, type=int
    )

@pytest.fixture
def url_static(request):
    return request.config.getoption("--url")


@pytest.fixture
def g_method(request):
    return getattr(requests, request.config.getoption("--method"))


@pytest.fixture
def st_code(request):
    return request.config.getoption("--status_code")