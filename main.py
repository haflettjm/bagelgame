# Bagles a deductive logic game
'''
    In bagels a deductive logic game you must guess a three digit number based on clues.
    Pico when the guess has a correct digit in the correct place.
    Bagels when the guess has no correct digits.
    10 tries total to guess the secret number.
    (Maybe add in 3rd hint option for guessing a digit that is in the number)
'''
from random import randint

def gameStart():
    print("I am thinking of a 3-digit number. Try to guess what it is. \nHere are some clues:\n")
    print("When I say:\tThat Means:")
    print("\tPico\tOne digit is correct but in the wrong position.\n")
    print("\tFermi\tOne digit is correct and in the right position.\n")
    print("\tBagels\tNo digit is correct.\n")
    print("I have thought up a number.\n")
    print(" You have 10 guesses to get it.\n")
    num = str(randint(100, 999))
    return num


#Handles the hints portion of the game
def hints(theNumber, guessUser):
    #Iterate over both strings and see if one matches and that if it matches is it in the same position

    for x in theNumber:
        if x in guessUser:
            if theNumber.index(x) == guessUser.index(x):
                return 'Fermi'
            else:
                return 'Pico'

    #If it is not found Bagel is returned
    return 'Bagel'


#guessing logic handler

def guessing(theNumber):
    #initialize the guess variable
    guessNumber = 0
    #while there are less then 11 guesses
    while guessNumber < 10:
        #print which guess number your on and grab the input
        guessUser = input(f"Your guess #{guessNumber+1}:\n")

        #Increment number of guesses
        guessNumber += 1

        #Checks to see if the user guessed right
        if guessUser == theNumber:
            print("You guessed right!")
            return

        #if they didn't immediately win switch to hints
        else:
            #print the hint
            print(hints(theNumber, guessUser))

    print("You Lost!")




#Quit logic
def gameQuit(gameState):
    #Set current state just in case
    shouldQuit = int(input("Would you like to quit? Enter 1 for yes 2 for no:\n"))
    #This was harder then it looked WHY
    #Checks User Input
    if False == ((shouldQuit ==1) or (shouldQuit ==2)):
        print("didn't work")
        while False == ((shouldQuit ==1) or (shouldQuit ==2)):
            shouldQuit = int(input("Invalid Input: Please Input 1 for yes 2 for no:\n"))

    if shouldQuit == 1:
        stateChange = 'quit'
    return stateChange

#Main Logic
def main():

    #Initialize game state
    gameState = 'run'

    while gameState != 'quit':
        theNumber = gameStart()
        guessing(theNumber)
        gameState = gameQuit(gameState)

if __name__ == '__main__':
    main()