from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def show_status(self):
        print(f"{self.name}: {self.health}")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage!")

    @abstractmethod
    def attack(self, other):
        pass


class Warrior(Character):
    def __init__(self, name, health, attack_power, shield):
        super().__init__(name, health, attack_power)
        self.shield = shield

    def attack(self, other):
        print(f"{self.name} bashes {other.name} with a shield charged strike!")
        other.take_damage(self.attack_power)


class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, other):
        if self.mana >= 10:
            self.mana -= 10
            print(f"{self.name} casts a spell! (mana left: {self.mana})")
            other.take_damage(self.attack_power)
        else:
            print(f"{self.name} is out of mana and can't attack!")


warrior = Warrior("Eris", 100, 45, 60)
mage = Mage("Laplace", 130, 25, 50)

for i in range(7):
    mage.attack(warrior)
    warrior.show_status()

# Now the real test:
#generic = Character("Blob", 50, 10)