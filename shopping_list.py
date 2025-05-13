from typing import Dict


class ShoppingList:
    def __init__(self):
        self._items: Dict[str, int] = {}

    def add_item(self, item: str, count: int):
        self._items[item] = count

    def remove_item(self, item: str):
        self._items[item] = 0

    def __str__(self):
        return "\n".join([f"{item}: {qty}" for item, qty in self._items.items()])
