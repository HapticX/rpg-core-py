"""
Provides Item class behavior
"""
from enum import IntEnum


class ItemType(IntEnum):
    GARBAGE = 0
    RECIPE = 1
    CONSUMABLE = 2
    HELMET = 3
    ARMOR = 4
    LEGS = 5
    BOOTS = 6
    HANDS = 7
    SHOULDER_PADS = 8
    SHIELD = 9
    ONE_HANDED_WEAPON = 10
    TWO_HANDED_WEAPON = 11


class Item:
    """
    Basic Item class. Describes basic item data.
    """

    def __init__(
            self,
            name: str,
            description: str = '',
            weight: float = 0.0,
            count: int = 1,
            price: int = 10,
            item_type: ItemType = ItemType.GARBAGE,
            **kwargs
    ):
        self.name = name
        self.description = description
        self.count = count
        self.weight = weight
        self.price = price
        self.item_type = item_type
        self._on_use = None

        match item_type:
            case ItemType.RECIPE:
                self.result: Item = kwargs['result']
            case ItemType.TWO_HANDED_WEAPON | ItemType.ONE_HANDED_WEAPON:
                self.damage: int = kwargs['damage']
            case ItemType.GARBAGE:
                pass
            case ItemType.CONSUMABLE:
                pass
            case _:
                self.defence: int = kwargs['defence']

    def use(self):
        """
        Uses this item if item consumable
        """
        if self.item_type == ItemType.GARBAGE:
            return
        if self._on_use is not None:
            self._on_use()

    def on_use(self, func):
        """
        Binds callback for use function

        :param func: Function without arguments.
        """
        self._on_use = func

    def __str__(self) -> str:
        """
        Stringify item
        :return: String representation
        """
        return (
            f'<Item>(name: "{self.name}", description: "{self.description}", '
            f'type: {self.item_type.name}, weight: {self.weight}, count: {self.count})'
        )
