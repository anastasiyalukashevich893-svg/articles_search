from enum import StrEnum


class SortType(StrEnum):
    LOW_TO_HIGH = "price_asc"
    HIGH_TO_LOW = "price_desc"

    @property
    def display_name(self) -> str:
        return {
            "price_asc": "Price: low to high",
            "price_desc": "Price: high to low",
        }[self.value]
