```mermaid
classDiagram
    class Customer {
        +name: str
        +purchase_history: list~Transaction~
    }

    class MenuItem {
        +name: str
        +price: Decimal
        +category: MenuCategory
        +popularity_rating: float
    }

    class MenuCategory {
        +name: str
        +filter_items(items: list~MenuItem~) list~MenuItem~
    }

    class Transaction {
        +items: list~MenuItem~
        +total_cost: Decimal
        +calculate_total() Decimal
    }

    Customer "1" --> "0..*" Transaction : purchase history
    Transaction "1" --> "1..*" MenuItem : contains
    MenuCategory "1" --> "0..*" MenuItem : categorizes
```

<!-- Suggestions and change details: aligned the diagram with the four classes and feature descriptions, removed unsupported identifiers and transaction details, corrected class references, and included category filtering. -->