import random
def createdeck():
    cardsindeck = [0, 1, 2, 3, 4, 5, 6, 7]
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
    cardsindeck[0] = wincons[random.randint(0, 21)]
    amountofcards = amountofcards + 1
    for x in range(random.randint(1, 2)):
        if amount == 0:
            card = random.randint(0, 13)
            cardsindeck[1] = cheaptanks[card]
            cheaptanks.pop(card)
            amountofcards = amountofcards + 1
            amount = 1
        elif amount == 1:
            card = random.randint(0, 6)
            cardsindeck[2] = expensivetanks[card]
            expensivetanks.pop(card)
            amountofcards = amountofcards + 1
    amount = 0
    if amountofcards == 2:
        for x in range(random.randint(2, 3)):
            if amount == 0:
                card = random.randint(0, 32)
                cardsindeck[2] = airdefense[card]
                airdefense.pop(card)
                amountofcards = amountofcards + 1
                amount = 1
            elif amount == 1:
                card = random.randint(0, 31)
                cardsindeck[3] = airdefense[card]
                airdefense.pop(card)
                amountofcards = amountofcards + 1
                amount = 2
            elif amount == 2:
                card = random.randint(0, 30)
                cardsindeck[4] = airdefense[card]
                airdefense.pop(card)
                amountofcards = amountofcards + 1
                amount = 2
    else:
        for x in range(random.randint(1, 2)):
            if amount == 0:
                card = random.randint(0, 32)
                cardsindeck[3] = airdefense[card]
                airdefense.pop(card)
                amountofcards = amountofcards + 1
                amount = 1
            elif amount == 1:
                card = random.randint(0, 31)
                cardsindeck[4] = airdefense[card]
                airdefense.pop(card)
                amountofcards = amountofcards + 1
    if cardsindeck[4] == 4:
        cardsindeck[4] = grounddefense[random.randint(0, 8)]
    amount = 0
    buildingornot = random.randint(0, 3)
    if buildingornot > 0:
        cardsindeck[5] = buildings[random.randint(0, 9)]
        amountofcards = amountofcards + 1
    if amountofcards == 6:
        cardsindeck[6] = smallspells[random.randint(0, 6)]
        amountofcards = amountofcards + 1
    else:
        cardsindeck[5] = smallspells[random.randint(0, 6)]
        amountofcards = amountofcards + 1
    if amountofcards == 6:
        bigspellornot = random.randint(0, 2)
        if bigspellornot > 0:
            cardsindeck[6] = bigspells[random.randint(0, 3)]
            amountofcards = amountofcards + 1
    if amountofcards == 6:
        cardsindeck[6] = cycle[random.randint(0, 3)]
        amountofcards = amountofcards + 1
    elif amountofcards == 7:
        cardsindeck[7] = cycle[random.randint(0, 3)]
        amountofcards = amountofcards + 1
    for x in range(8 - amountofcards):
        if amountofcards == 6:
            cardsindeck[6] = pushbuilding[random.randint(0, 8)]
            cardsindeck[7] = pushbuilding[random.randint(0, 8)]
        elif amountofcards == 7:
            cardsindeck[7] = pushbuilding[random.randint(0, 8)]
    if cardsindeck[6] == 6:
        cardsindeck[6] = pushbuilding[random.randint(0, 8)]
        cardsindeck[7] = cycle[random.randint(0, 4)]
    return cardsindeck
decklist = createdeck()