from pages.base_page import BasePage
from utils.enums import SortType


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.filter_sort = page.get_by_test_id("filter-sort")
        self.loader = page.locator("//section[contains(@class, 'results-region') and contains(@class, 'is-loading')]")
        self.titles = page.get_by_test_id("search-result-title")
        self.prices = page.get_by_test_id("search-result-price")
        self.results = page.get_by_test_id("search-results-grid")

    def sort(self, sort_type: SortType):
        self.filter_sort.click()
        self.filter_sort.select_option(sort_type.value)

    def wait_for_result(self):
        self.loader.wait_for(state='detached')

    def get_articles_and_prices(self, count: int):
        self.wait_for_result()
        items = []
        all_titles = self.titles.all_text_contents()
        all_prices = self.prices.all_text_contents()
        for i in range(min(count, len(all_titles), len(all_prices))):
            items.append({
                'title': all_titles[i].strip(),
                'price': all_prices[i].strip()
            })
        return items

    def get_prices(self, count: int):
        items = self.get_articles_and_prices(count)
        prices = []
        for item in items:
            price_str = item['price'].strip()
            try:
                prices.append(float(price_str))
            except ValueError:
                prices.append(0.0)
        return prices
