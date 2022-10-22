import random
from time import sleep
import webbrowser
import os
import ctypes
import urllib.request


# Bingo Calls
calls = ["Lonely Number - 1", "Times trump was impeached - 2", "Cup of tea - 3", "Knock at the door - 4", "Man alive - 5",
         "Half a dozen - 6", "Lucky for some - 7", "Garden gate - 8", "Doctor's Orders - 9", "Boris' Den - 10",
         "Legs eleven - 11", "Kurts age - 12", "Unlucky for some - 13", "Valentine's Day - 14", "Orsons Age - 15",
         "Grandma wishes she was - 16", "Dancing Queens - 17", "Coming of age - 18", "Goodbye teens - 19", "One Score - 20",
         "Royal Salyute - 21", "Two little ducks - 22", "Thee and me - 23", "Kurt wishes he was - 24", "Duck and dive - 25",
         "Half a crown - 26", "Duck and a crutch - 27", "In a state - 28", "Rise and shine - 29", "Dirty Gertie - 30",
         "Get up and run - 31", "Buckle my shoe - 32", "Dirty knee - 33", "Ask for more - 34", "Jump and jive - 35",
         "Three dozen - 36", "More than eleven - 37", "Christmas cake - 38", "Steps - 39", "Life begins - 40",
         "Time for fun - 41", "Winnie the Pooh - 42", "Down on your knees - 43", "Droopy Drawers - 44",
         "Halfway there - 45", "Up to tricks - 46", "Four and seven - 47", "Four dozen - 48", "PC - 49",
         "It's a bullseye! - 50", "Tweak of the thumb - 51", "Chicken Vindaloo - 52", "Stuck in the tree - 53",
         "Man at the door - 54", "All the fives - 55", "Shotts bus - 56", "Heinz Varieties - 57", "Make them wait - 58",
         "Brighton Line - 59", "Grandads age - 60", "Bakers bun - 61", "Tickety-Boo - 62", "Tickle me - 63",
         "Almost retired - 64", "Retirement age - 65", "Clickety click - 66", "Stairway to Heaven - 67",
         "Pick a mate - 68", "Anyway up - 69", "Three score and ten - 70", "Bang on the drum - 71", "36 times 2 - 72",
         "Queen bee - 73", "Hit the floor - 74", "Strive and strive - 75", "Fallout - 76", "Two little crutches - 77",
         "Heaven's gate - 78", "One more time - 79", "Eight and blank - 80", "Stop and run - 81",
         "Straight on through - 82", "Time for tea - 83", "Give me more - 84", "Staying alive - 85",
         "Times kurt gets payed a day - 86", "Amount of food the kittens eat - 87", "Amount of money Orson owes Kurt - 88", "Amount of pounds kurt owes in tax - 89",
         "Top of the shop - 90"]


# Defining the task if the user wants to play again
def reRun():
    try:
        numberOfRounds = int(input("How many numbers would you like generated for this round: "))
    except ValueError:
        numberOfRounds = int(input("Please enter a valid number "))
    numberOfRoundsAsString = str(numberOfRounds)

    confirmRounds = Y
    if confimRounds == 'y' or confimRounds == 'Y':
        print("Lets play bingo!")
        ready = input("Press Enter to get your first number, and again after every number called: ")
    # To start the game, the user can hit Enter. Any other value is also accepted to avoid errors.
    if ready >= '':
        # The game has started, and a variable is declared as a random number between 0 and 90
        nextNumber = random.choice(calls)
        # A list is created for numbers already called to go in
        alreadyCalled = []
        # A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
        x = 0
        actRound = numberOfRounds
    while x < numberOfRounds:
        # The number is reset if it has already been called; x stays the same
        if nextNumber in alreadyCalled:
            nextNumber = random.choice(calls)

        # If the number hasn't been called, then it is included in the list, printed, and reset.
        elif nextNumber not in alreadyCalled:
            alreadyCalled.append(nextNumber)
            print(nextNumber)
            nextNumber = random.choice(calls)
            actRound -= 1
            input("\n")
            x += 1
        # Ends the loop when conditions met
        else:

            break
    numberOfGoesAsString = str(numberOfRounds)
    print("You have reached your selected amount of 90 goes.")
    sleep(0.5)




def program():


        try:
            numberOfRounds = int(input("How many numbers would you like generated for this round: "))
        except ValueError:
            numberOfRounds = int(input("Please enter a valid number "))
        numberOfRoundsAsString = str(numberOfRounds)
        confimRounds = 'y'
        if confimRounds == 'y' or confimRounds == 'Y':
            print("Lets play bingo!")
            ready = input("Press Enter to get your first number, and after every number called: ")
        # To start the game, the user can hit Enter. Any other value is also accepted to avoid errors.
        if ready >= '':
            # The game has started, and a variable is declared as a random number between 0 and 90
            nextNumber = random.choice(calls)
            # A list is created for numbers already called to go in
            alreadyCalled = []
            # A while loop is initiated, so long a x is less than the number of rounds inputted on line 17
            x = 0
            actRound = numberOfRounds
        while x < numberOfRounds:
            # The number is reset if it has already been called; x stays the same
            if nextNumber in alreadyCalled:
                nextNumber = random.choice(calls)

            # If the number hasn't been called, then it is included in the list, printed, and reset.
            elif nextNumber not in alreadyCalled:
                alreadyCalled.append(nextNumber)
                print(nextNumber)
                nextNumber = random.choice(calls)
                actRound -= 1
                input("\n")
                x += 1
            # Ends the loop when conditions met
            else:

                break
        numberOfGoesAsString = str(numberOfRounds)
        print("You have reached your selected amount of " + numberOfGoesAsString + " goes.")
        sleep(0.5)




# Welcome
print("Welcome to Bingo Caller")
sleep(0)
print("After you type a value, press Enter to submit it.")
sleep(0)
program()
