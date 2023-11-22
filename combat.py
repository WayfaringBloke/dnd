from dataclasses import dataclass, field
from pprint import pprint
import random
from time import sleep


def droll(n: int) -> int:
    with open('output.txt', 'a') as f:
        r = 0 if n == 0 else random.randint(1, n)
        print(f"Rolling d{n}", end="")
        print(f"Rolling d{n}", end="", file=f, flush=True)
        dots = random.randint(3, 5)
        for _ in range(dots):
            print(".", end="")
            print(".", end="", file=f, flush=True)
            sleep(float(random.randint(3, 8)) / 50)

        print(f"{' ' * (6 - dots)} got {r}!")
        print(f"{' ' * (6 - dots)} got {r}!", file=f, flush=True)
    
def roll(n: int) -> int:
    r = 0 if n == 0 else random.randint(1, n)
    print(f"Rolled d{n} got {r}")
    return r

def who_acts():
    if roll(2) == 1:
        print(f"Enemies act first")
    else:
        print(f"Players act first")

@dataclass
class Armor:
    resist: int
    is_flat: bool

    def blk(self):
        return self.resist if self.is_flat else roll(self.resist)

@dataclass
class Weapon:
    damage: int
    is_auto: bool
    is_flat: bool

    def atk(self, dr, name):
        for _ in range(3 if self.is_auto else 1):
            dmg = self.damage if self.is_flat else roll(self.damage)
            print(f"{name}: DR {dr} DMG {dmg}")

class Name(str):
    pass

class HP(int):
    pass

class Morale(int):
    pass

class ToDodge(int):
    pass

@dataclass
class Enemy:
    name: Name
    hp: HP
    to_dodge: ToDodge
    morale: Morale
    armor: Armor
    weapon: Weapon
    group: object = field(init=False, repr=False)
    start_hp: HP = field(init=False, repr=False)

    def dmg(self, amount):
        blocked = self.armor.blk()
        amount -= blocked
        if amount < 1:
            amount = 1
        self.hp -= amount
        print(f"{self.name}: HP {self.hp}")
        if self.hp <= 0:
            self.group.kill(self.name)
        elif self.hp <= self.strt_hp // 3:
            print(f"{self.name}: BLOODIED (Rolling Morale)")
            self.mrl()
            self.strt_hp = 0

    def kill(self):
        self.group.kill(self.name)
    
    def atk(self, mod):
        dr = self.to_dodge + mod
        self.weapon.atk(dr, self.name)

    def mrl(self):
        if roll(6) + roll(6) > self.morale:
            action = "FLEES" if roll(2) == 1 else "SURRENDERS"
            while True:
                inp = input(f"{self.name}: {action} (Y/n)? ")
                if inp.lower() in ["y", "n", ""]: break

            if inp.lower() != "n":
                self.group.kill(self.name)

    def __post_init__(self):
        self.strt_hp = self.hp

class Group:
    leader: Name
    enemies: dict[Name, Enemy]
    initEnemies: int

    def __init__(self, enemies: list[Enemy]):
        self.leader = enemies[0].name \
            if len(enemies) > 0 and enemies[0] != None else \
            None
        self.enemies = {}
        self.initEnemies = 0
        for enemy in enemies:
            self.add(enemy)

    def get_enemy(self, name):
        return self.enemies[name]

    def run(self):
        if self.currentTurn >= len(self.turnOrder):
            print("Enemy Turns Over. Resetting...")
            self.rst()
            return
        attacking = self.enemies[self.turnOrder[self.currentTurn]]
        print(f"{attacking.name}: ATTACKING")
        mod = int(input(f"{attacking.name}: DR Mod: "))
        attacking.atk(mod)
        self.currentTurn += 1

    def mrl(self):
        for e in self.enemies.values():
            e.mrl()

    def kill(self, name: Name):
        if name not in self.enemies:
            print("Error: Can't kill {name}")
            return

        del self.enemies[name]

        print(f"{name}: DEAD")

        if self.leader == name:
            print("LEADER DEAD: Rolling morale")
            self.mrl()
            self.leader = None
        if len(self.enemies) <= self.initEnemies // 2:
            print("HALF DEAD: Rolling morale")
            self.mrl()
            self.initEnemies = 0

    def __getattr__(self, name):
        enemy = self.get_enemy(name)
        if enemy == None:
            print(f"Error: Enemy {name} not found")
        return enemy
    
    def add(self, enemy: Enemy, leader: bool = False):
        if enemy.name in self.enemies:
            print(f"Error: {enemy.name} already exists")
        else:
            self.enemies[enemy.name] = enemy
            enemy.group = self

            if self.initEnemies > 0:
                self.initEnemies += 1

            if leader:
                self.leader = enemy.name    

def n(name: str) -> Name:
    return Name(name)

def h(hp: int) -> HP:
    return HP(hp)

def m(morale: int) -> Morale:
    return Morale(morale)

def w(damage: int, is_auto: bool = False) -> Weapon:
    return Weapon(damage, is_auto, False)

def wf(damage: int, is_auto: bool = False) -> Weapon:
    return Weapon(damage, is_auto, True)

def a(resist: int, is_flat: bool = True) -> Armor:
    return Armor(resist, is_flat)

def d(to_dodge: int) -> ToDodge:
    return ToDodge(to_dodge)

def ne(*args):
    STATS: dict[type, str]= {
        Name: "name", HP: "hp", ToDodge: "to_dodge", 
        Morale: "morale", Armor: "armor", Weapon: "weapon",
    }
    enemy_props = {}

    for i, arg in enumerate(args):
        if type(arg) in STATS:
            prop = STATS[type(arg)]
            if prop in enemy_props:
                print(f"Error: {arg} [{i}] is a repeated {prop} value")
                return None
            enemy_props[prop] = arg
        else:
            print(f"Error: {arg} [{i}] is of type {type(arg)}")
            return None
        
    for prop in STATS.values():
        if prop not in enemy_props:
            print(f"Error: {prop} not set")
            return None
    
    return Enemy(**enemy_props)



# format
# groups of enemies are separated by line breaks
# enemy stats are separated by commas
# leader always first
# e.g.
Group([
    ne(n("fish"), h(10), d(4), w(4, True), a(1), m(4)),
    ne(n("gamer"), h(200), d(14), w(6), a(10, False),  m(11)),
])

# usage
# 0. group = parse(string)
# 1. who_starts()
# 2. group.odr() to pick an attack order for the enemies
# 3. group.name.dmg(amount) to damage enemies
# 4. group.run() runs 1 enemies turn at a time
