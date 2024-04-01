import random
amount = 0
amountofcards = 0
wincons = ["Skeleton Barrel", "Mortar", "Royal Giant", "Elixir Golem", "Barbarian Barrel", "Hog Rider", "Giant",
           "Royal Hogs", "Three Musketeers", "Wall Breakers", "Goblin Barrel", "Goblin Drill", "Balloon",
           "Goblin Giant", "X-Bow", "Electro-Giant", "Golem", "Miner", "Ram Rider", "Graveyard", "Lava Hound",
           "Royal Recruits"]
airdefense = ["Bats", "Archers", "Minions", "Witch", "Musketeer", "Baby Dragon", "Wizard", "Spear Goblins",
              "Minion Horde", "Ice Wizard", "Princess", "Three Musketeers", "Ice Spirit", "Fire Spirit",
              "Inferno Dragon", "Mega Minion", "Dart Goblin", "Goblin Gang", "Electro Wizard", "Hunter",
              "Executioner", "Zappies", "Rascals", "Flying Machine", "Magic Archer", "Electro Dragon", "Firecracker",
              "Archer Queen", "Skeleton Dragons", "Mother Witch", "Electro Spirit", "Phoenix", "Little Prince"]
buildings = ["Barbarian Hut", "Elixir Collector", "Goblin Hut", "Inferno Tower",
             "Bomb Tower", "Furnace", "Goblin Cage", "Tesla", "Tombstone", "Cannon"]
bigspells = ["Fireball", "Rocket", "Poison", "Earthquake"]
smallspells = ["Arrows", "Zap", "The Log", "Tornado", "Barbarian Barrel", "Snowball", "Royal Delivery"]
cheaptanks = ["Knight", "Valkyrie", "Mini PEKKA", "Dark Prince", "Miner", "Lumberjack", "Bandit", "Royal Ghost",
              "Fisherman", "Mighty Miner", "Battle Healer", "Skeleton King", "Golden Knight", "Little Prince"]
expensivetanks = ["PEKKA", "Prince", "Giant Skeleton", "Elite Barbarians", "Rascals", "Mega Knight", "Monk"]
champions = ["Skeleton King", "Archer Queen", "Golden Knight", "Monk", "Little Prince"]
grounddefense = ["Goblins", "Barbarian", "Bomber", "Skeleton Army", "Guards", "Miner", "Bowler", "Ice Golem",
                 "Cannon Cart",]
cycle = ["Ice Spirit", "Fire Spirit", "Skeletons", "Electro Spirit", "Heal Spirit"]
pushbuilding = ["Lumberjack", "Sparky", "Elite Barbarians", "Night Witch", "Fisherman", "Rage", "Freeze", "Mirror",
                "Clone"]
card1 = wincons[random.randint(0, 21)]
amountofcards = amountofcards + 1
for x in range(random.randint(1, 2)):
    if amount == 0:
        card = random.randint(0, 13)
        card2 = cheaptanks[card]
        cheaptanks.pop(card)
        amountofcards = amountofcards + 1
        amount = 1
    elif amount == 1:
        card = random.randint(0, 6)
        card3 = expensivetanks[card]
        expensivetanks.pop(card)
        amountofcards = amountofcards + 1
amount = 0
if amountofcards == 2:
    for x in range(random.randint(1, 3)):
        if amount == 0:
            card = random.randint(0, 32)
            card3 = airdefense[card]
            airdefense.pop(card)
            amountofcards = amountofcards + 1
            amount = 1
        elif amount == 1:
            card = random.randint(0, 31)
            card4 = airdefense[card]
            airdefense.pop(card)
            amountofcards = amountofcards + 1
            amount = 2
        elif amount == 2:
            card = random.randint(0, 30)
            card5 = airdefense[card]
            airdefense.pop(card)
            amountofcards = amountofcards + 1
            amount = 2
else:
    for x in range(random.randint(1, 2)):
        if amount == 0:
            card = random.randint(0, 32)
            card4 = airdefense[card]
            airdefense.pop(card)
            amountofcards = amountofcards + 1
            amount = 1
        elif amount == 1:
            card = random.randint(0, 31)
            card5 = airdefense[card]
            airdefense.pop(card)
            amountofcards = amountofcards + 1
amount = 0
buildingornot = random.randint(0, 3)
if buildingornot > 0:
    card6 = buildings[random.randint(0, 9)]
    amountofcards = amountofcards + 1
if amountofcards == 6:
    card7 = smallspells[random.randint(0, 6)]
    amountofcards = amountofcards + 1
else:
    card6 = smallspells[random.randint(0, 6)]
    amountofcards = amountofcards + 1
if amountofcards == 6:
    bigspellornot = random.randint(0,2)
    if bigspellornot > 0:
        card7 = bigspells[random.randint(0,3)]
        amountofcards = amountofcards + 1
