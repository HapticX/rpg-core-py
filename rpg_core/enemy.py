"""
Provides Enemy class for interact with objects and other enemies
"""


class Enemy:
    """
    Basic Enemy.
    It can hit other enemies and take damage (or can't).
    """

    def __init__(
            self,
            max_health: int = 10,
            damage: int = 1,
            defence: int = 0,
            can_dmg: bool = True
    ):
        self.current_health = max_health
        self.max_health = max_health
        self.can_dmg = can_dmg
        self.damage = damage
        self.defence = defence
        self._on_take_dmg = None
        self._on_hit = None
        self._on_dead = None
        self._calculate_damage = self._default_calculate_damage

    def hit(self, other: 'Enemy') -> bool:
        """
        Hits other enemy
        :returns: True when other was take damage
        """
        if not other.can_dmg:
            return False
        if (taken_damage := other.take_damage(self.damage)) <= 0:
            return False
        if self._on_hit is not None:
            self._on_hit(taken_damage)
        return True

    def take_damage(self, damage: int) -> int:
        """
        Takes damage and recalculate health
        :returns: taken damage
        """
        damage = self._calculate_damage(damage)
        self.current_health -= damage
        if self._on_take_dmg is not None:
            self._on_take_dmg(damage)
        if self.current_health <= 0 and self._on_dead is not None:
            self._on_dead()
        return damage

    def on_hit(self, func):
        """
        Binds callback function for `hit` method

        :param func: Function with `int` argument.
        """
        self._on_hit = func

    def on_take_damage(self, func):
        """
        Binds callback function when enemy takes any damage

        :param func: Function with `int` argument
        """
        self._on_take_dmg = func

    def on_dead(self, func):
        """
        Binds callback function when enemy is dead

        :param func: Function without arguments
        """
        self._on_dead = func

    def calculate_damage(self, func):
        """
        Binds function for calculating taken damage

        :param func: Function that takes one `int` argument and returns calculated `int` damage
        """
        self._calculate_damage = func

    def _default_calculate_damage(self, damage: int) -> int:
        """
        Calculates damage that can take

        :param damage: damage to calculate
        :returns: calculated damage
        """
        return max(damage - self.defence, 0)

    def __str__(self) -> str:
        return (
            f'<{self.__class__.__name__}>(hp: {self.current_health}/{self.max_health}, '
            f'canDmg: {self.can_dmg}, dmg: {self.damage}, def: {self.defence})'
        )
