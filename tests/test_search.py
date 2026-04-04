class TestSearch:
    def test_search(self, home_page, config, test_data):
        query = test_data["name"]
        count = test_data["count"]
        sort_type = test_data["filter_type"]
        home_page.page.goto(config.base_url)
        home_page.logo_is_visible()
        search_page= home_page.search(query)
        search_page.sort(sort_type)
        items = search_page.get_articles_and_prices(count)
        prices=[]
        for item in items:
            price_str=item['price'].strip()
            try:
               prices.append(float(price_str))
            except ValueError:
                prices.append(0.0)
        if sort_type == "Price: low to high":
            expected_prices = sorted(prices)
            assert prices == expected_prices, ( f"Сортировка по возрастанию нарушена!\n"
        f"EXPECTED: {expected_prices[:5]}\n"
        f"ACTUAL: {prices[:5]}")
        else:
            expected_prices = sorted(prices, reverse=True)
            assert prices == expected_prices, (f"Сортировка по убыванию нарушена!\n"
        f"EXPECTED: {expected_prices[:5]}\n"
        f"ACTUAL: {prices[:5]}")
            




