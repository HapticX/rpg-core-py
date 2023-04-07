from unittest import TestCase, main
from rpg_core import Enemy


class EnemyTestCase(TestCase):
    def setUp(self) -> None:
        self.enemy1 = Enemy()
        self.enemy2 = Enemy()

    def test_damage(self):
        self.enemy2.hit(self.enemy1)
        print("after hit:", self.enemy1)

    def test_event(self):
        @self.enemy1.on_hit
        def on_hit(dmg: int):
            print(f'{self.enemy1} hit other enemy with damage {dmg}')
        self.enemy1.hit(self.enemy2)
        print(self.enemy2)

    def test_stringify(self):
        print(self.enemy1)


if __name__ == '__main__':
    main(verbosity=2)
