class Tank:

    def __init__(self, health, attack, range, armor, movement):
        self.health = health
        self.attack = attack
        self.range = range
        self.armor = armor
        self.movement = movement

    def attack(self):
        pass

    def siege(self):
        Tank.range =+ 1
        Tank.attack =+ 5
        Tank.movement = 0
        print('The tank has now in siege mode! ')

    def hull_break(self):
        Tank.armor =- 2
        Tank.movement = 0
        print('The tank has a hull breach and is under assault! ')



