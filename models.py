from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class MenuCategory:
    name: str

    def filter_items(self, items: list[MenuItem]) -> list[MenuItem]:
        return [item for item in items if item.category == self]


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


# Suggestions and change details: removed the add_transaction method and docstrings because they are not shown in the UML.
