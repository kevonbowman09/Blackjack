import random
import time 

hand = []
house = []

def start():
    if hand:
        print("")
        hand.clear()
        house.clear()
        time.sleep(1.5)
    
    print("Starting game!\n")
    
    for x in range(2):
        hand.append(random.randint(1,13))
        house.append(random.randint(1,13))
    
    time.sleep(1)
    printTable(hand, False)
    time.sleep(0.25)
    printTable(house, True)
    time.sleep(0.35)
    hitOrStand()

def readableCard(card):
    if card == 1:
        return "A"
    elif card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    else:
        return card

def printTable(table, isTable):
    newTable = []
    
    for card in table:
        newTable.append(readableCard(card))
    
    if isTable == True:
        newTable[-1] = "?"
    
    addStr = ""
    if len(newTable) > 2:
        for index, card in enumerate(newTable):
            if index != (len(newTable) - 1):
                addStr = addStr + str(card) + ", "
            else:
                addStr = addStr + "and " + str(card)
    else:
        addStr = str(newTable[0]) + " and " + str(newTable[1])
        
    if table == hand:
        print("You have " + addStr + ".")
    else:
        print("The house has " + addStr) 

def hitOrStand():
    time.sleep(1)
    answer = input("Would you like to hit or stand? [h/s]")
    
    if answer == "h":
        hit()
    elif answer == "s":
        print("Stand!\n")
        stand()
    else:
        print("\nInvalid input... Try Again!")
        hitOrStand()

def hit():
    newCard = random.randint(1,13)
    hand.append(newCard)
    time.sleep(0.5)
    print("You got a " + str(readableCard(newCard)) + "!\n")
    
    handValue = adder(hand)
    
    if handValue > 21:
        time.sleep(0.75)
        print("Bust! You lose.")
        start()
    else:
        time.sleep(1)
        printTable(hand, False)
        hitOrStand()
    
def stand():
    time.sleep(1)
    houseValue = adder(house)
    handValue = adder(hand)

    if houseValue < 17:
        print("The house is going to hit.")
        time.sleep(1.25)
        newCard = random.randint(1,13)
        house.append(newCard)
        print("The house got a " + str(readableCard(newCard)) + "!\n")
        stand()
    else:
        print("The house will not hit.\n")
        time.sleep(1.5)
        printTable(hand, False)
        printTable(house, False)
        time.sleep(1.25)
        
        if houseValue > 21:
            print("The house busted! You win!")
            start()
        else:
            if houseValue > handValue:
                if houseValue == 21:
                    print("The house got a Blackjack. You lose...")
                    start()
                else:
                    print("The house wins. You lose...")
                    start()
            if houseValue == handValue:
                if houseValue == 21:
                    print("Wow! Double Blackjack! Tie!")
                    start()
                else:
                    print("Tie...")
                    start()
            if houseValue < handValue:
                if handValue == 21:
                    print("Blackjack! You win!")
                    start()
                else:
                    print("You win!")
                    start()
                
def adder(table):
    addTable = []
    for card in table:
        addTable.append(card)
    addTable.sort(reverse=True)
    
    total = 0
    for card in addTable:
        if card == 1:
            if total + 11 <= 21:
                total = total + 11
            else:
                total = total + 1
        elif card >= 11:
            total = total + 10
        else:
            total = total + card
    
    return total
            
start()

