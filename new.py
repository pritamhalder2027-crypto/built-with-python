class Character:
    def __init__(self, name, health, attack_power, defense=0):
        self.name = name
        self.max_health = health   # set this first: the setter depends on it
        self._health = health
        self.attack_power = attack_power
        self.defense = defense     # an attribute, not a method

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self.max_health))

    def is_alive(self):
        return self._health > 0

    def take_damage(self, amount):
        reduced = max(0, amount - self.defense)   # defense reduces incoming damage
        self.health -= reduced
        print(f"{self.name} takes {reduced} damage! ({self._health}/{self.max_health} HP left)")

    def attack(self, other):
        print(f"{self.name} attacks {other.name}!")
        other.take_damage(self.attack_power)


def battle(a, b):
    attacker, defender = a, b
    while a.is_alive() and b.is_alive():
        attacker.attack(defender)
        attacker, defender = defender, attacker   # swap turns
    winner = a if a.is_alive() else b
    print(f"\n{winner.name} wins!")

class Warrior(Character):
    def __init__(self, name):
        # super() calls the parent's __init__ so we don't repeat ourselves
        super().__init__(name, health=120, attack_power=14, defense=5)

    def attack(self, other):
        # Override: same method name, different behavior
        print(f"{self.name} swings a heavy sword!")
        other.take_damage(self.attack_power)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=70, attack_power=25, defense=0)
        self.mana = 30

    def attack(self, other):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts a fireball! (mana: {self.mana})")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} is out of mana and falls down!...")
            other.take_damage(3)


battle(Warrior("Tempest"), Mage("Merlin"))