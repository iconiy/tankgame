import random


class Tank:

    def __init__(self, name):
        self.health = 150
        self.attck = 25
        self.range = 12
        self.armor = 10
        self.movement = 2
        self.ammo = 2
        self.name = name

    def death(self):
        death = True
        self.health = 0
        print('Tank has died, Run has ended! ')
        print('Health: ', self.health)
        return death

    def attack(self):
        print('BOOM!')
        att = (int(self.attck) - int(random.randint(0, self.attck)))
        print(f'You did {att} damage')

    def siege(self):
        self.range += 2
        self.attck += 5
        self.movement = 0
        print('The tank has now in siege mode! ')
        print(self.range, self.attck, self.movement)

    def hull_break(self):
        Tank.armor =- 2
        Tank.movement = 0
        print('The tank has a hull breach and is under assault! ')

    def stats(self):
        print(f'The current stats of {self.name} is {self.health} health, and {self.attck} attack')



