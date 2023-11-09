from dataclasses import dataclass, field
from pprint import pprint
import random

def roll(n):
    r = 0 if n == 0 else random.randint(1, n)
    print(f"Rolled d{n} got {r}")
    return r

def who_acts():
    if roll(2) == 1:
        print(f"Enemies act first")
    else:
        print(f"Players act first")

@dataclass
class Weapon:
    damage: int
    is_auto: bool

    def atk(self, dr, name):
        for _ in range(3 if self.is_auto else 1):
            dmg = roll(self.damage)
            print(f"{name}: DR {dr} DMG {dmg}")  

@dataclass
class Enemy:
    name: str
    hp: int
    accuracy: int
    morale: int
    armor: int
    weapon: Weapon
    group: object = field(init=False, repr=False)
    strt_hp: int = field(init=False, repr=False)

    def dmg(self, amount):
        blocked = roll(self.armor)
        amount -= blocked
        if amount < 1:
            amount = 1
        self.hp -= amount
        print(f"{self.name}: HP {self.hp}")
        if self.hp <= 0:
            print(f"{self.name}: DEAD")
            self.group.kill(self.name)
        elif self.hp <= self.strt_hp // 3:
            print(f"{self.name}: BLOODIED")
            self.mrl()
            self.strt_hp = 0
        
    def atk(self, mod):
        dr = self.accuracy + mod
        self.weapon.atk(dr, self.name)

    def mrl(self):
        print(f"{self.name}: MORALE")
        if roll(6) + roll(6) > self.morale:
            action = "FLEES" if roll(2) == 1 else "SURRENDERS"
            while True:
                inp = input(f"{self.name}: {action} (Y/n)? ")
                if inp.lower() in ["y", "n", ""]: break
            
            if inp.lower() != "n":
                self.group.kill(self.name)
            

    def ded(self):
        return self.hp <= 0

    def __post_init__(self):
        self.strt_hp = self.hp

@dataclass
class Group:
    leader: Enemy
    enemies: list[Enemy]
    initEnemies: int = field(init=False)
    turnOrder: list[int] = field(init=False)
    currentTurn: int = field(init=False)
    
    def __post_init__(self):
        self.initEnemies = len(self.enemies)
        self.turnOrder = []
        self.currentTurn = 0

    def get_enemy(self, name):
        for e in self.enemies:
            if e.name == name:
                return e
        return None

    def odr(self):
        for i, e in enumerate(self.enemies):
            print(f"[{i}]: {e.name}")
        while True:
            # parses comma separated indexes
            trns = input("Turn order: ")
            trns = list(map(int, trns.split(",")))
            if sorted(trns) == list(range(len(self.enemies))):
                break
            print(f"Error: Invalid turn order {trns}")
        self.turnOrder = trns

    def rst(self):
        self.currentTurn = 0

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
        for e in self.enemies:
            e.mrl()
    
    def kill(self, name):
        killed = None
        for i, e in enumerate(self.enemies):
            if e.name == name:
                self.turnOrder.remove(i)
                self.enemies.remove(e)
                killed = e
        
        if killed == None: return

        print(f"{killed.name}: DEAD")

        if self.leader != None and killed == self.leader:
            self.mrl()
            self.leader = None
        if len(self.enemies) <= self.initEnemies // 2:
            self.mrl()
            self.initEnemies = 0
            
    def __getattr__(self, name):
        enemy = self.get_enemy(name)
        if enemy == None:
            print(f"Enemy {name} not found")
        return enemy
    

    
        


PREFIXES = ["n:", "h:", "m:", "a:", "w:", "d:"]

def remove_prefix(s, prf):
    if not s.startswith(prf):
        print(f"Error: {s} is missing prefix {prf}")
    return s.removeprefix(prf)

def parse(s):
    es = s.split("\n") 
    enemies = []
    for i, e in enumerate(es):
        eas = [remove_prefix(ea.strip(), prf).strip() for ea, prf in zip(e.split(","), PREFIXES)]

        name, hp, morale, rawArmor, rawWeapon, accuracy = eas
        
        hp = int(hp)
        morale = int(morale)
        armor = int(remove_prefix(rawArmor, "d").strip())
        rawWeapon = remove_prefix(rawWeapon, "d").strip()
        weaponDamage = int(rawWeapon.removesuffix("a"))
        weaponAuto = rawWeapon.endswith("a")
        weapon = Weapon(weaponDamage, weaponAuto)
        accuracy = int(accuracy)
        enemy = Enemy(
            name,
            hp,
            accuracy,
            morale,
            armor,
            weapon
        )
        
        enemies.append(enemy)
    group = Group(enemies[0], enemies)

    for e in enemies:
        e.group = group

    pprint(group)
    
    return group
# format
# groups of enemies are separated by line breaks
# enemy stats are separated by commas
# leader always first
# e.g.
"""n: fish, h: 10, m: 4, a: d0, w: d4a, d: 12
n: gamer, h: 200, m: 11, a: d10, w: d6, d: 14"""

# usage
# 0. group = parse(string)
# 1. who_starts()
# 2. group.odr() to pick an attack order for the enemies
# 3. group.name.dmg(amount) to damage enemies
# 4. group.run() runs 1 enemies turn at a time
    

