# something.py
# by: Kendrick Smith
# calculates stats for your D&D character

import random
def main():
    #input
    lvl = eval(input("What is your character level? "))
    if lvl == 1:
        yn = input("Yes or No, would you like to randomize your stats? ")
        if yn == "yes" or yn == "Yes" or yn == "y" or yn == "Y":
            STR = round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())
            DEX = round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())
            CON = round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())
            INT = round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())
            WIS = round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())
            CAR = round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())+round(random.random())
        else:
            print("If you haven't done so already roll 4d6 -1d6 for each of your ability scores.")
            STR = eval(input("First, what is your strength? "))
            DEX = eval(input("Second, what is your dexterity? "))
            CON = eval(input("Third, what is your constitution? "))
            INT = eval(input("Next, what is your intelligence? "))
            WIS = eval(input("Next, what is your wisdom? "))
            CAR = eval(input("Last, what is your charisma? "))
        print("STR is", STR)
        print("DEX is", DEX)
        print("CON is", CON)
        print("INT is", INT)
        print("WIS is", WIS)
        print("CAR is", CAR)
        print("That's all you get for not wanting to randomize in a randomizer.")
    else:
        print("Then what are you doing here? You know how to play already!")
main()
