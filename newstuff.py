quit = "0"
while quit == "0":
    commonamountneeded = 12087
    rareamountneeded = 3287
    epicamountneeded = 427
    legendaryamountneeded = 43
    championamountneeded = 31
    quit = input("Would you like to check how many cards you need (Type 0) or do you want to quit: ")
    rarity = input("What rarity do you want to check? ")
    if rarity == "common":
        level = int(input("What level is your card (if you don't have it, type 0"))
        if level == 0:
            print(commonamountneeded)
        elif level == 1:
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print(commonamountneeded)
        elif level == 2:
            commonamountneeded = commonamountneeded - 2
