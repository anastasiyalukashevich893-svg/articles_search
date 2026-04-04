from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)


        self.filter_sort = page.get_by_test_id("filter-sort")
        self.low_to_high = page.get_by_role("option", name="Price: low to high").first
        self.high_to_low = page.get_by_role("option", name="Price: high to low").first
        self.loader = page.locator("//section[contains(@class, 'results-region is-loading')]")
        self.titles = page.locator('[data-testid^="search-result-title-"]')
        self.prices = page.locator('[data-testid^="search-result-price-"]')
        self.results = page.get_by_test_id("search-results-grid")

    def sort (self, sort_type) :
        self.filter_sort.click()
        if sort_type == "Price: low to high":
            self.filter_sort.select_option("price_asc")
        elif sort_type == "Price: high to low":
            self.filter_sort.select_option("price_desc")
        return self


    def wait_for_result(self):
        self.loader.wait_for(state = 'detached')


    def get_articles_and_prices(self, count: int) :
        self.wait_for_result()
        items =[]
        results = self.results.all()[:count]
        all_titles = self.titles.all_text_contents()
        all_prices = self.prices.all_text_contents()
        for i in range(min(count, len(all_titles), len(all_prices))):
            items.append({
                'title': all_titles[i].strip(),
                'price': all_prices[i].strip()
            })
        return items











