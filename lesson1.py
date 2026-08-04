class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name} , мой уровень {self.level}')
    def attack(self):
        print(self.name,'наносит удар!')
        self.strength -= 1
    def rest(self):
        print(self.name, 'отдыхает...')
        self.health += 1

kitano = Hero('Kitano', 15, 64, 54)
marie = Hero("Marie", 3, 80, 15)
kitano.greet()
print (f'{kitano.name} до атаки: {kitano.strength}')
kitano.attack()
print (f'{kitano.name} после атаки: {kitano.strength}')
print (f'{kitano.name} до отдыха {kitano.health}')
kitano.rest()
print (f'{kitano.name} после отдыха {kitano.health}')
print("*"*50)
marie.greet()
print (f'{marie.name} до атаки: {marie.strength}')
marie.attack()
print (f'{marie.name} после атаки: {marie.strength}')
print (f'{marie.name} до отдыха {marie.health}')
marie.rest()
print (f'{marie.name} после отдыха {marie.health}')