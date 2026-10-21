import unittest
from decimal import Decimal

from models import MenuCategory, MenuItem, Transaction


class ByteBitesTests(unittest.TestCase):
    def test_calculate_total_with_multiple_items(self) -> None:
        # A transaction total should equal the sum of the selected items' prices.
        category = MenuCategory("Meals")
        burger = MenuItem("Burger", Decimal("10.00"), category, 4.5)
        soda = MenuItem("Soda", Decimal("5.00"), category, 4.0)
        transaction = Transaction(items=[burger, soda])

        self.assertEqual(transaction.calculate_total(), Decimal("15.00"))
        self.assertEqual(transaction.total_cost, Decimal("15.00"))

    def test_empty_transaction_total_is_zero(self) -> None:
        # An empty transaction should have a zero total rather than raising an error.
        transaction = Transaction()

        self.assertEqual(transaction.calculate_total(), Decimal("0.00"))

    def test_filter_items_returns_only_matching_category(self) -> None:
        # Filtering a menu by category should return only items in that category.
        meals = MenuCategory("Meals")
        drinks = MenuCategory("Drinks")
        burger = MenuItem("Burger", Decimal("10.00"), meals, 4.5)
        soda = MenuItem("Soda", Decimal("5.00"), drinks, 4.0)

        self.assertEqual(meals.filter_items([burger, soda]), [burger])

    def test_sort_items_by_popularity_descending(self) -> None:
        # Sorting should return items from most to least popular without changing the input.
        meals = MenuCategory("Meals")
        burger = MenuItem("Burger", Decimal("10.00"), meals, 4.5)
        pizza = MenuItem("Pizza", Decimal("12.00"), meals, 4.9)
        salad = MenuItem("Salad", Decimal("8.00"), meals, 3.8)
        menu_items = [burger, pizza, salad]

        self.assertEqual(
            meals.sort_items_by_popularity(menu_items),
            [pizza, burger, salad],
        )
        self.assertEqual(menu_items, [burger, pizza, salad])


if __name__ == "__main__":
    unittest.main()


