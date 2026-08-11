from abc import ABC, abstractmethod
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
    def greet(self):
        print (f'Првиет, я {self.name}, мой уровень {self.level}')
    def rest(self):
        print(f'{self.name} отдыхает')
        self.__health +=1
    @abstractmethod
    def attack(self):
        pass
class Warrior(Hero):
    def attack(self):
        print('Воин атакует мечом')
class Mage(Hero):
    def attack(self):
        print('Маг использует магию')
class Assassin(Hero):
    def attack(self):
        print('Ассасин атакует из-под тишка')

morgan = Warrior("Morgan",8,100,48)
gven = Mage("Gven",45,88,83 )
vivi = Assassin("Vivi", 78,96,58)

morgan.greet()
morgan.attack()
morgan.rest()
print()

gven.greet()
gven.attack()
gven.rest()
print()

vivi.greet()
vivi.attack()
vivi.rest()
print()
