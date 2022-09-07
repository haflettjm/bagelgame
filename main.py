# Bagles a deductive logic game
'''
    In bagels a deductive logic game you must guess a three digit number based on clues.
    Pico when the guess has a correct digit in the correct place.
    Bagels when the guess has no correct digits.
    10 tries total to guess the secret number.
    (Maybe add in 3rd hint option for guessing a digit that is in the number)
'''

def gameStart():
    print("I am thinking of a 3-digit number. Try to guess what it is. \nHere are some clues:\n")
    print("When I say:\tThat Means:")
    print("\tPico\tOne digit is correct but in the wrong position.\n")
    print("\tFermi\tOne digit is correct and in the right position.\n")
    print("\tBagels\tNo digit is correct.\n")
    print("I have thought up a number.\n")
    print(" You have 10 guesses to get it.\n")



#Main Logic
def main():

    #Initialize game state
    gameState = 'run'

    while gameState != 'quit':
        gameStart()
        gameState = 'quit'

if __name__ == '__main__':
    main()