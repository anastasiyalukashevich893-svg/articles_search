import pytest
from utils.config_reader import ConfigReader
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)