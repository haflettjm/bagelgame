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
    print("When I say:")

#Main Logic
def main():

    #Initialize game state
    gameState = 'run'



    while gameState != 'quit':
        gameStart()

if __name__ == '__main__':
    main()