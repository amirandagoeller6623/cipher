import qrcode
import random
cntn = "yes"
def createdeck():
    cardsindeck = [0, 1, 2, 3, 4, 5, 6, 7]
    amount = 0
    amountofcards = 0
    wincons = ["Skeleton Barrel", "Mortar", "Royal Giant", "Elixir Golem", "Barbarian Barrel", "Hog Rider", "Giant",
               "Royal Hogs", "Three Musketeers", "Wall Breakers", "Goblin Barrel", "Goblin Drill", "Balloon",
               "Goblin Giant", "X-Bow", "Electro Giant", "Golem", "Miner", "Ram Rider", "Graveyard", "Lava Hound",
               "Royal Recruits"]
    airdefense = ["Bats", "Archers", "Minions", "Witch", "Musketeer", "Baby Dragon", "Wizard", "Spear Goblins",
                  "Minion Horde", "Ice Wizard", "Princess", "Three Musketeers", "Ice Spirit", "Fire Spirit",
                  "Inferno Dragon", "Mega Minion", "Dart Goblin", "Goblin Gang", "Electro Wizard", "Hunter",
                  "Executioner", "Zappies", "Rascals", "Flying Machine", "Magic Archer", "Electro Dragon", "Firecracker",
                  "Archer Queen", "Skeleton Dragons", "Mother Witch", "Electro Spirit", "Phoenix", "Little Prince"]
    buildings = ["Barbarian Hut", "Elixir Collector", "Goblin Hut", "Inferno Tower",
                 "Bomb Tower", "Furnace", "Goblin Cage", "Tesla", "Tombstone", "Cannon"]
    bigspells = ["Fireball", "Rocket", "Poison", "Earthquake"]
    smallspells = ["Arrows", "Zap", "The Log", "Tornado", "Barbarian Barrel", "Giant Snowball", "Royal Delivery"]
    cheaptanks = ["Knight", "Valkyrie", "Mini P.E.K.K.A", "Dark Prince", "Miner", "Lumberjack", "Bandit", "Royal Ghost",
                  "Fisherman", "Mighty Miner", "Battle Healer", "Skeleton King", "Golden Knight", "Little Prince"]
    expensivetanks = ["P.E.K.K.A", "Prince", "Giant Skeleton", "Elite Barbarians", "Rascals", "Mega Knight", "Monk"]
    champions = ["Skeleton King", "Archer Queen", "Golden Knight", "Monk", "Little Prince"]
    grounddefense = ["Goblins", "Barbarians", "Bomber", "Skeleton Army", "Guards", "Miner", "Bowler", "Ice Golem",

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
        amount = random.randint(0,1)
        if amount == 0:
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
    amount = 0
    championslot = 0
    numberofchampions = 0
    for x in range(8):
        if cardsindeck[amount] in champions:
            championslot = amount
            numberofchampions = numberofchampions + 1
        amount = amount + 1
    amount = -1
    if numberofchampions > 1:
        print(0)
        for x in range(7):
            if cardsindeck[amount] == championslot:
                amount = amount + 2
            else:
                amount = amount + 1
            if cardsindeck[amount] in champions:
                cardsindeck[amount] = airdefense[random.randint(0, 20)]
    return cardsindeck
def builddeck():
    dupe = ""
    deck = []
    card = ""
    data = []
    exists = "no"
    deckdata = ""
    variablessucktoo = int(0)
    cardnames =  ["Mirror",
                  "Skeletons",
                  "Electro Spirit",
                  "Fire Spirit",
                  "Ice Spirit",
                  "Heal Spirit",
                  "Goblins",
                  "Spear Goblins",
                  "Bomber",
                  "Bats",
                  "Zap",
                  "Giant Snowball",
                  "Ice Golem",
                  "Barbarian Barrel",
                  "Wall Breakers",
                  "Rage",
                  "The Log",
                  "Archers",
                  "Arrows",
                  "Knight",
                  "Minions",
                  "Cannon",
                  "Goblin Gang",
                  "Skeleton Barrel",
                  "Firecracker",
                  "Royal Delivery",
                  "Tombstone",
                  "Mega Minion",
                  "Dart Goblin",
                  "Earthquake",
                  "Elixir Golem",
                  "Goblin Barrel",
                  "Guards",
                  "Skeleton Army",
                  "Clone",
                  "Tornado",
                  "Miner",
                  "Princess",
                  "Ice Wizard",
                  "Royal Ghost",
                  "Bandit",
                  "Fisherman",
                  "Little Prince",
                  "Skeleton Dragons",
                  "Mortar",
                  "Tesla",
                  "Fireball",
                  "Mini P.E.K.K.A",
                  "Musketeer",
                  "Goblin Cage",
                  "Valkyrie",
                  "Battle Ram",
                  "Bomb Tower",
                  "Flying Machine",
                  "Hog Rider",
                  "Battle Healer",
                  "Furnace",
                  "Zappies",
                  "Baby Dragon",
                  "Dark Prince",
                  "Freeze",
                  "Poison",
                  "Hunter",
                  "Goblin Drill",
                  "Electro Wizard",
                  "Inferno Dragon",
                  "Phoenix",
                  "Magic Archer",
                  "Lumberjack",
                  "Night Witch",
                  "Mother Witch",
                  "Golden Knight",
                  "Skeleton King",
                  "Mighty Miner",
                  "Barbarians",
                  "Minion Horde",
                  "Rascals",
                  "Giant",
                  "Goblin Hut",
                  "Inferno Tower",
                  "Wizard",
                  "Royal Hogs",
                  "Witch",
                  "Balloon",
                  "Prince",
                  "Electro Dragon",
                  "Bowler",
                  "Executioner",
                  "Cannon Cart",
                  "Ram Rider",
                  "Graveyard",
                  "Archer Queen",
                  "Monk",
                  "Royal Giant",
                  "Elite Barbarians",
                  "Rocket",
                  "Barbarian Hut",
                  "Elixir Collector",
                  "Giant Skeleton",
                  "Lightning",
                  "Goblin Giant",
                  "X-Bow",
                  "Sparky",
                  "Royal Recruits",
                  "P.E.K.K.A",
                  "Electro Giant",
                  "Mega Knight",
                  "Lava Hound",
                  "Golem",
                  "Three Musketeers"]
    cardnumbers = ["28000006",
                   "26000010",
                   "26000084",
                   "26000031",
                   "26000030",
                   "28000016",
                   "26000002",
                   "26000019",
                   "26000013",
                   "26000049",
                   "28000008",
                   "28000017",
                   "26000038",
                   "28000015",
                   "26000058",
                   "28000002",
                   "28000011",
                   "26000001",
                   "28000001",
                   "26000000",
                   "26000005",
                   "27000000",
                   "26000041",
                   "26000056",
                   "26000064",
                   "28000018",
                   "27000009",
                   "26000039",
                   "26000040",
                   "28000014",
                   "26000067",
                   "28000004",
                   "26000025",
                   "26000012",
                   "28000013",
                   "28000012",
                   "26000032",
                   "26000026",
                   "26000023",
                   "26000050",
                   "26000046",
                   "26000061",
                   "26000093",
                   "26000080",
                   "27000002",
                   "27000006",
                   "28000000",
                   "26000018",
                   "26000014",
                   "27000012",
                   "26000011",
                   "26000036",
                   "27000004",
                   "26000057",
                   "26000021",
                   "26000068",
                   "27000010",
                   "26000052",
                   "26000015",
                   "26000027",
                   "28000005",
                   "28000009",
                   "26000044",
                   "27000013",
                   "26000042",
                   "26000037",
                   "26000087",
                   "26000062",
                   "26000035",
                   "26000048",
                   "26000083",
                   "26000074",
                   "26000069",
                   "26000065",
                   "26000008",
                   "26000022",
                   "26000053",
                   "26000003",
                   "27000001",
                   "27000003",
                   "26000017",
                   "26000059",
                   "26000007",
                   "26000006",
                   "26000016",
                   "26000063",
                   "26000034",
                   "26000045",
                   "26000054",
                   "26000051",
                   "28000010",
                   "26000072",
                   "26000072",
                   "26000024",
                   "26000043",
                   "28000003",
                   "27000005",
                   "27000007",
                   "26000020",
                   "28000007",
                   "26000060",
                   "27000008",
                   "26000033",
                   "26000047",
                   "26000004",
                   "26000085",
                   "26000055",
                   "26000029",
                   "26000009",
                   "26000028"]
    print("Here's a list of every card: {}".format(cardnames))
    ihatelistdatarules = input("Would you like a random deck?")
    deck = []
    if ihatelistdatarules == ("yes"):
        deck = createdeck()
        dupeset = set(deck)
        while 6 in deck or 7 in deck or len(dupeset) != len(deck):


            deck = createdeck()
    else:
        while len(deck) < 8:
            card = input("What card would you like to add to your deck? ")
            exists = "no"
            variablessucktoo = int(0)
            for y in cardnames:
                if card == y:
                    deck.append(cardnames[variablessucktoo])
                    exists = "yes"
                variablessucktoo += 1
            if exists != "yes":
                print("That's not a card(it's case sensitive)!")
            else:
                print("Added {} to your deck!".format(card))
    data = []
    for z in range(8):
        data.append(cardnumbers[cardnames.index(deck[z])])
    print("Here's your deck: {}, {}, {}, {}, {}, {}, {}, {}".format(deck[0], deck[1], deck[2], deck[3], deck[4], deck[5], deck[6], deck[7]))
    deckdata = "https://link.clashroyale.com/deck/en/?deck=" + str(data[0]) + ";" + str(data[1]) + ";" + str(data[2]) + ";" + str(data[3]) + ";" + str(data[4]) + ";" + str(data[5]) + ";" + str(data[6]) + ";" + str(data[7])
    qr = qrcode.QRCode(version =1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)
    qr.add_data(deckdata)
    qr.make(fit=True)
    img = qr.make_image()
    img.save("deck.png")
while cntn == "yes":
    builddeck()
    cntn = input("Would you like to make another deck? ")
qr = qrcode.QRCode(version =1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)
qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
qr.make(fit=True)
img = qr.make_image()
img.save("deck.png")
