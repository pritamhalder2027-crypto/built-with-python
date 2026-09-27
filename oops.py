class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self._health = health
        self.attack_power = attack_power
        self.max_health = self.health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max (0, min(value, self.max_health))
        # This is encapsulation in action: we control how health can change

    def is_alive(self):
        return self._health > 0

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! ({self._health}/{self.max_health} HP left")

    def attack(self, other):
        print(f"{self.name} attacks {other.name}!")
        other.take_damage(self.attack_power)

# Creating objects (instances) from the character class
hero = Character("Aria", health=100, attack_power=15)
dragon = Character("Dragon", health=40, attack_power=8)

hero.attack(dragon)
dragon.attack(hero)

print(hero.is_alive(), dragon.is_alive())
