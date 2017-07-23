#Random Number Game
#7/23/17
#CTI-110 M5HW2 - Random Number Guessing Game
#Jessica Young
#


import random

def generateRandomNumber():
    randomNumber = random.randInt( 1, 100 )
    return randomNumber
                        
def askUserForNumber():
    userNumber = int( input( "Guess the number: "))
    return UserNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high, try again."
    elif userNumber < randomNumber:
        return "Too low, try again."
    elif userNumber == randomNumber:
        return "Congrats, you got it!"

def main():
    randomNumber = generateRandomNumber()
    userNUmber = askUserForNumber()
    message = checkUserNumber( userNumber, randomNumber )

   
    
