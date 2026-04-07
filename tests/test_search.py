import pytest
from utils.enums import SortType


class TestSearch:
    @pytest.mark.parametrize("query", ["city", "habits"])
    @pytest.mark.parametrize("count", [10, 15])
    @pytest.mark.parametrize("sort_type", [SortType.LOW_TO_HIGH, SortType.HIGH_TO_LOW])
    def test_search(self, home_page, config, query, count, sort_type):
        home_page.page.goto(config.base_url)
        home_page.logo_is_visible()
        search_page = home_page.search(query)
        search_page.sort(sort_type)
        prices = search_page.get_prices(count)
        if sort_type == SortType.LOW_TO_HIGH:
            expected_prices = sorted(prices)
            assert prices == expected_prices, (f"Сортировка по возрастанию нарушена!\n"
                                               f"EXPECTED: {expected_prices[:5]}\n"
                                               f"ACTUAL: {prices[:5]}")
        else:
            expected_prices = sorted(prices, reverse=True)
            assert prices == expected_prices, (f"Сортировка по убыванию нарушена!\n"
                                               f"EXPECTED: {expected_prices[:5]}\n"
                                               f"ACTUAL: {prices[:5]}")
