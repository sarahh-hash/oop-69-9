import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(self.name, "наносит удар!")
        self.strength -= 1

    def rest(self):
        print(self.name, "отдыхает...")
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(self.name, "атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(self.name, "кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(self.name, "атакует из-под тишка!")


warrior = Warrior("Kitano", 15, 64, 54, 80)
mage = Mage("Marie", 3, 80, 15, 100)
assassin = Assassin("Shadow", 7, 70, 25, 90)

heroes = {
    1: warrior,
    2: mage,
    3: assassin
}

print("Выберите героя:")
print("1 - Warrior")
print("2 - Mage")
print("3 - Assassin")

choice = int(input("Ваш выбор: "))

if choice in heroes:
    player = heroes[choice]

    enemy_number = random.randint(1, 3)

    while enemy_number == choice:
        enemy_number = random.randint(1, 3)

    enemy = heroes[enemy_number]

    print("\nВы выбрали:", player.__class__.__name__)
    print("Противник:", enemy.__class__.__name__)

    player.attack()
    enemy.attack()

    if choice == 1 and enemy_number == 3:
        print("Warrior победил!")
    elif choice == 3 and enemy_number == 2:
        print("Assassin победил!")
    elif choice == 2 and enemy_number == 1:
        print("Mage победил!")
    else:
        print(enemy.__class__.__name__, "победил!")

else:
    print("Такого героя нет!")