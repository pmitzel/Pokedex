# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 3: Pokedex
# Peter Mitzel, Austin Hull
# Last Modified: 10/17/2017
# ---------------------------------------
# This program will allow the user to search up pokemon
#   from the pokedex based on different variables such
#   as name, number, ect. It will also do a couple more
#   functions such as add up their hitpoints and show
#   the pokedex.
# ---------------------------------------
import string

def printMenu():
    print("1. Print Pokedex")
    print("2. Lookup Pokemon by Name")
    print("3. Lookup Pokemon by Number")
    print("4. Print Number of Pokemon")
    print("5. Print Total Hit Points of All Pokemon")
    print("6. Quit")
    print()

def printPokedex(pokedex):
    print()
    print("The Pokedex")
    for poke in pokedex:
        print("-----------")
        if len(pokedex[poke]) == 4:             # for when pokemon have two types
            print("Number:" + str(poke) + ", Name: " + str(pokedex[poke][0]) +
                  ", HP: " + str(pokedex[poke][1]) + ", Type: " + str(pokedex[poke][2]) +
                  " and " + str(pokedex[poke][3]))
        else:                                   # when pokemon only have one type
            print("Number:" + str(poke) + ", Name: " + str(pokedex[poke][0]) +
                  ", HP: " + str(pokedex[poke][1]) + ", Type: " + str(pokedex[poke][2]))
    print("-----------")
    print("End Pokedex")
    print()
    
def lookupByName(pokedex, name):
    count = 0
    for poke in pokedex:
        if name == pokedex[poke][0]:
            count += 1
            if len(pokedex[poke][0:]) == 4:
                print("Number: " + str(poke) + ", Name: " +
                      str(pokedex[poke][0]) + ", HP: " +
                      str(pokedex[poke][1]) + ", Type: " +
                      str(pokedex[poke][2]) + " and " + str(pokedex[poke][3]))
            elif len(pokedex[poke][0:]) == 3:
                print("Number: " + str(poke) + ", Name: " +
                      str(pokedex[poke][0]) + ", HP: " +
                      str(pokedex[poke][1]) + ", Type: " + str(pokedex[poke][2]))
    while count == 0:
        print("The pokemon named " + str(name) + " does not exist")
        print()
        return
    print()

def howManyPokemon(pokedex):
    number = len(pokedex)
    print("There are " + str(number) + " different Pokemon")
    print()
            
def howManyHitPoints(pokedex):
    total = 0
    for poke in pokedex:
        total += int(pokedex[poke][1])
    print("The total number of hit points for all Pokemon is", total)
    print()
              
def lookupByNumber(pokedex, number):
    if number <= len(pokedex):      #ensuring valid input
        poke = pokedex.get(number)
        if len(poke) == 4:          #pokemon with 2 types
            print("Number: " + str(number) + ", Name: " + str(poke[0]) + ", HP: " +
                  str(poke[1]) + ", Type: " + str(poke[2]) + " and " + str(poke[3]))
        elif len(poke) == 3:        #pokemon with 1 type
            print("Number: " + str(number) + ", Name: " + str(poke[0]) + ", HP: " +
                  str(poke[1]) + ", Type: " + str(poke[2]))
    elif number > len(pokedex):     #returns error if too high of number
        print("Error: Pokemon number " + str(number) + " does not exist")
    else:
        print("That is not a number, try again")
    print()
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def createPokedex(filename):
    pokedex = {}
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)]          # name
        pokedex[index] += [int(pokelist.pop(0))]    # hit points
        pokedex[index] += [pokelist.pop(0)]         # type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)]     # optional second type

    file.close()
    return pokedex

# ---------------------------------------

def getChoice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = getChoice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = getChoice(1, 1000, "Enter a Pokemon number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyHitPoints(pokedex)
    print("Thank you.  Goodbye!")

# ---------------------------------------

main()
