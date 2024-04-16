quit = "0"
while quit == "0":
    commonamountneeded = 12087
    rareamountneeded = 3287
    epicamountneeded = 427
    legendaryamountneeded = 43
    championamountneeded = 31
    commongold = 240625
    raregold = 240600
    epicgold = 239400
    legendarygold = 230000
    championgold = 210000
    commonxp = 5800
    rarexp = 5791
    epicxp = 5725
    legendaryxp = 5250
    championxp = 4400
    quit = input("Would you like to check how many cards you need (Type 0) or do you want to quit: ")
    rarity = input("What rarity do you want to check? ")
    if rarity == "common":
        amount = 0
        level = int(input("What level is your card (if you don't have it, type 0"))
        if level == 0:
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 1:
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 2:
            commonxp = commonxp - 4
            commongold = commongold - 5
            commonamountneeded = commonamountneeded - 3
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 3:
            commonxp = commonxp - 9
            commongold = commongold - 25
            commonamountneeded = commonamountneeded - 4
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 4:
            commonxp = commonxp - 15
            commongold = commongold - 75
            commonamountneeded = commonamountneeded - 17
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 5:
            commonxp = commonxp - 25
            commongold = commongold - 225
            commonamountneeded = commonamountneeded - 37
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 6:
            commonxp = commonxp - 50
            commongold = commongold - 625
            commonamountneeded = commonamountneeded - 87
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 7:
            commonxp = commonxp - 100
            commongold = commongold - 1625
            commonamountneeded = commonamountneeded - 187
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 8:
            commonxp = commonxp - 200
            commongold = commongold - 3625
            commonamountneeded = commonamountneeded - 387
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 9:
            commonxp = commonxp - 400
            commongold = commongold - 7625
            commonamountneeded = commonamountneeded - 787
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 10:
            commonxp = commonxp - 800
            commongold = commongold - 15625
            commonamountneeded = commonamountneeded - 1587
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 11:
            commonxp = commonxp - 1400
            commongold = commongold - 30625
            commonamountneeded = commonamountneeded - 2587
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 12:
            commonxp = commonxp - 2200
            commongold = commongold - 65625
            commonamountneeded = commonamountneeded - 4087
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 13:
            commonxp = commonxp - 3800
            commongold = commongold - 140625
            commonamountneeded = commonamountneeded - 7087
            amount = int(input("How many cards do you have already? "))
            commonamountneeded = commonamountneeded - amount
            print("this will take {} cards and {} gold and it will give you {}xp".format(commonamountneeded, commongold, commonxp))
        elif level == 14:
            print("You don't need any more of this card to get level 14, but if you get 50,000 more you can get "
                  "enough elite wild cards to upgrade it to level 15")
    if rarity == "rare":
        amount = 0
        level = int(input("What level is your card (if you don't have it, type 0"))
        if level == 0:
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 3:
            rareamountneeded = rareamountneeded - 0
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 4:
            rarexp = rarexp - 6
            raregold = raregold - 50
            rareamountneeded = rareamountneeded - 3
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 5:
            rarexp = rarexp - 16
            raregold = raregold - 200
            rareamountneeded = rareamountneeded - 7
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 6:
            rarexp = rarexp - 41
            raregold = raregold - 600
            rareamountneeded = rareamountneeded - 17
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 7:
            rarexp = rarexp - 91
            raregold = raregold - 1600
            rareamountneeded = rareamountneeded - 37
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 8:
            rarexp = rarexp - 191
            raregold = raregold - 3600
            rareamountneeded = rareamountneeded - 87
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 9:
            rarexp = rarexp - 391
            raregold = raregold - 7600
            rareamountneeded = rareamountneeded - 187
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 10:
            rarexp = rarexp - 791
            raregold = raregold - 15600
            rareamountneeded = rareamountneeded - 387
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 11:
            rarexp = rarexp - 1391
            raregold = raregold - 30600
            rareamountneeded = rareamountneeded - 787
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 12:
            rarexp = rarexp - 2191
            raregold = raregold - 65600
            rareamountneeded = rareamountneeded - 1287
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 13:
            rarexp = rarexp - 3791
            raregold = raregold - 140600
            rareamountneeded = rareamountneeded - 3087
            amount = int(input("How many cards do you have already? "))
            rareamountneeded = rareamountneeded - amount
            print("This will take {} cards and {} gold and it will give you {}xp".format(rareamountneeded, raregold, rarexp))
        elif level == 14:
            print("You don't need any more of this card to get level 14, but if you get 10,000 more you can get "
                  "enough elite wild cards to upgrade it to level 15")
    if rarity == "epic":
        amount = 0
        level = int(input("What level is your card (if you don't have it, type 0"))
        if level == 0:
            print(epicamountneeded)
        elif level == 6:
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 7:
            epicxp = epicxp - 25
            epicgold = epicgold - 400
            epicamountneeded = epicamountneeded - 3
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 8:
            epicxp = epicxp - 125
            epicgold = epicgold - 2400
            epicamountneeded = epicamountneeded - 7
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 9:
            epicxp = epicxp - 325
            epicgold = epicgold - 6400
            epicamountneeded = epicamountneeded - 17
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 10:
            epicxp = epicxp - 725
            epicgold = epicgold - 14400
            epicamountneeded = epicamountneeded - 37
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 11:
            epicxp = epicxp - 1325
            epicgold = epicgold - 29900
            epicamountneeded = epicamountneeded - 77
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 12:
            epicxp = epicxp - 2125
            epicgold = epicgold - 64900
            epicamountneeded = epicamountneeded - 127
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 13:
            epicxp = epicxp - 3725
            epicgold = epicgold - 139900
            epicamountneeded = epicamountneeded - 227
            amount = int(input("How many cards do you have already? "))
            epicamountneeded = epicamountneeded - amount
            print("This will cost {} cards amd {} gold and give you {}xp".format(epicamountneeded, epicgold, epicxp))
        elif level == 14:
            print("You don't need any more of this card to get level 14, but if you get 2500 more you can get "
                  "enough elite wild cards to upgrade it to level 15")
    if rarity == "legendary":
        amount = 0
        level = int(input("What level is your card (if you don't have it, type 0"))
        if level == 0:
            print("This will take {} cards and {} gold and give you {}xp".format(legendaryamountneeded, legendarygold, legendaryxp))
        elif level == 9:
            amount = int(input("How many cards do you have already? "))
            legendaryamountneeded = legendaryamountneeded - amount
            print("This will take {} cards and {} gold and give you {}xp".format(legendaryamountneeded, legendarygold, legendaryxp))
        elif level == 10:
            legendaryxp = legendaryxp - 250
            legendarygold = legendarygold - 5000
            legendaryamountneeded = legendaryamountneeded - 3
            amount = int(input("How many cards do you have already? "))
            legendaryamountneeded = legendaryamountneeded - amount
            print("This will take {} cards and {} gold and give you {}xp".format(legendaryamountneeded, legendarygold, legendaryxp))
        elif level == 11:
            legendaryxp = legendaryxp - 850
            legendarygold = legendarygold - 20000
            legendaryamountneeded = legendaryamountneeded - 7
            amount = int(input("How many cards do you have already? "))
            legendaryamountneeded = legendaryamountneeded - amount
            print("This will take {} cards and {} gold and give you {}xp".format(legendaryamountneeded, legendarygold, legendaryxp))
        elif level == 12:
            legendaryxp = legendaryxp - 1250
            legendarygold = legendarygold - 55000
            legendaryamountneeded = legendaryamountneeded - 13
            amount = int(input("How many cards do you have already? "))
            legendaryamountneeded = legendaryamountneeded - amount
            print("This will take {} cards and {} gold and give you {}xp".format(legendaryamountneeded, legendarygold, legendaryxp))
        elif level == 13:
            legendaryxp = legendaryxp - 3250
            legendarygold = legendarygold - 130000
            legendaryamountneeded = legendaryamountneeded - 23
            amount = int(input("How many cards do you have already? "))
            legendaryamountneeded = legendaryamountneeded - amount
            print("This will take {} cards and {} gold and give you {}xp".format(legendaryamountneeded, legendarygold, legendaryxp))
        elif level == 14:
            print("You don't need any more of this card to get level 14, but if you get 34 more you can get "
                  "enough elite wild cards to upgrade it to level 15")
    if rarity == "champion":
        amount = 0
        level = int(input("What level is your card (if you don't have it, type 0"))
        if level == 0:
            print("This will take {} cards amd {} gold and it will give you {}xp".format(championamountneeded, championgold, championxp))
        elif level == 11:
            amount = int(input("How many cards do you have already? "))
            championamountneeded = championamountneeded - amount
            print("This will take {} cards amd {} gold and it will give you {}xp".format(championamountneeded, championgold, championxp))
        elif level == 12:
            championxp = championxp - 800
            championgold = championgold - 35000
            championamountneeded = championamountneeded - 3
            amount = int(input("How many cards do you have already? "))
            championamountneeded = championamountneeded - amount
            print("This will take {} cards amd {} gold and it will give you {}xp".format(championamountneeded, championgold, championxp))
        elif level == 13:
            championxp = championxp - 2400
            championgold = championgold - 110000
            championamountneeded = championamountneeded - 11
            amount = int(input("How many cards do you have already? "))
            championamountneeded = championamountneeded - amount
            print("This will take {} cards amd {} gold and it will give you {}xp".format(championamountneeded, championgold, championxp))
        elif level == 14:
            print("You don't need any more of this card to get level 14, but if you get 34 more you can get "
                  "enough elite wild cards to upgrade it to level 15")
