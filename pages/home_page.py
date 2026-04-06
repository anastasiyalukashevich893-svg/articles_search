from pages.base_page import BasePage
from pages.search_page import SearchPage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.main_page = page.get_by_test_id("catalog-title")
        self.input_search = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def logo_is_visible(self):
        return self.main_page.wait_for(state='visible')

    def search(self, query: str):
        self.input_search.fill(query)
        self.search_button.click()
        return SearchPage(self.page)
