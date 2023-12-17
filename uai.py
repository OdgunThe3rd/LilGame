import random
lis = random.randint(0, 2)
class Player:
    def __init__(self):
        self.name = None
        self.health = 100
        self.level = 1
        print("the player works")
    def attack_enemy(self):
        damage = 10
        return damage
    def run_away(self):
        return random.choice([True, False])
    def kill_count(self):
        self.kills = []
    def level_up(self):
        for i in range(1, len(self.kills), 1):
            self.level += 1
class enemies:
    def __init__(self):
        self.amount = 1
        if 1 <= player.level <= 5:
            self.amount = 6
        if 6 <= player.level <= 10:
            self.amount = 7
    def enemy1(self):
        self.health = 50
        self.damage = 10
        self.enemies = ["wolf", "snake", "rogue soldier"]
        self.enemy = self.enemies[lis]
    def enemy2(self):
        self.health = 60
        self.damage = 15
        self.enemies = ["soldier", "guard", "mercenary"]
        self.enemy = self.enemies[lis]
class enemy(enemies):
    def __init__(self):
        enemies.__init__(self)
        if 0 <= player.level <= 5:
            enemy.enemy1(self)
        if 6 <= player.level <= 10:
            enemy.enemy2(self)
    def attack_player(self):
        damage = self.damage
        print(f"The enemy attacks you and deals {damage} damage")
        return damage
    def run_away(self):
        return random.choice([True, False])
player = Player()
enemy = enemy()





