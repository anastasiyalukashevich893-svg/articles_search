import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader
from pages.search_page import SearchPage
from pages.home_page import HomePage
from tests.test_data import TestData


@pytest.fixture(scope="session")
def config():
    return ConfigReader()


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)


@pytest.fixture(params = TestData.ARTICLE)
def test_data(request):
    return request.param
