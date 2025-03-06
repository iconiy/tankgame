import sys


class Tank:

    def __init__(self, health, attack, range, armor, movement):
        self.health = health
        self.attack = attack
        self.range = range
        self.armor = armor
        self.movement = movement

    def death(self):
        death = True
        self.health = 0
        print('Tank has died, Run has ended! ')
        print('Health: ', self.health)
        return death

    def attack(self):
        pass

    def siege(self):
        self.range += 1
        self.attack += 5
        self.movement = 0
        print('The tank has now in siege mode! ')
        print(self.range, self.attack, self.movement)

    def hull_break(self):
        Tank.armor =- 2
        Tank.movement = 0
        print('The tank has a hull breach and is under assault! ')



