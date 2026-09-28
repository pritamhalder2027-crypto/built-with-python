class Dog:
    def __init__(self, name, age, tricks):
        self.name = name
        self.age = age
        self.tricks = []

    def old(self):
        print(f"{self.name} is {self.age} years old")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}!")

    def learn_trick(self, tricks):
        print(f"{self.name} is able to do {tricks}!")


dog1 = Dog("Luna", 3, tricks=['to handshake'])
dog1.old()
dog1.birthday()
dog1.old()
dog1.learn_trick(tricks='handshake')

dog2 = Dog("Ruby", 2, tricks=['to handshake'])
dog2.old()
dog2.birthday()
dog2.old()
dog2.learn_trick(tricks='handshake')