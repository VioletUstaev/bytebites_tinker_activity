from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class MenuCategory:
    name: str

    def filter_items(self, items: list[MenuItem]) -> list[MenuItem]:
        return [item for item in items if item.category == self]

    def sort_items_by_popularity(self, items: list[MenuItem]) -> list[MenuItem]:
        return sorted(items, key=lambda item: item.popularity_rating, reverse=True)


@dataclass
class MenuItem:
    name: str
    price: Decimal
    category: MenuCategory
    popularity_rating: float


@dataclass
class Transaction:
    items: list[MenuItem] = field(default_factory=list)

    def calculate_total(self) -> Decimal:
        return sum((item.price for item in self.items), start=Decimal("0.00"))

    @property
    def total_cost(self) -> Decimal:
        return self.calculate_total()


@dataclass
class Customer:
    name: str
    purchase_history: list[Transaction] = field(default_factory=list)


# Suggestions and change details: added popularity-descending sorting to MenuCategory to match the updated UML.
