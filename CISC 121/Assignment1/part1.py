##  PART 1
##  Name: Superhero Kitten Name Generator
##  Date: September 25th, 2017
##  Version: v0.1
##  Author: Ryan Protheroe
##  Description: Assigns the user a superhero kitten name based on the ascii values of their first and last name

import time


def main():
    ##  Declaring arrays
    listOfSuperheroPrefixes = ['Super', 'Ultra', 'Marvel', 'Mega', 'Laser', 'Lightning', 'Thunder', 'Power', 'Iron', 'Captain']
    listOfKittenPostfixes = ['Fuzz', 'Whiskers', 'Purr', 'Paw', 'Claw', 'Fang', 'Snuggle', 'Cuddle', 'Cute Overload']

    ##  Acquiring first and last name, welcome script
    firstName = askForName("Welcome to the Superhero Kitten Name Generator!\nPlease enter your first name:")
    print("Hello,",firstName)
    time.sleep(1)       ##  Adds 1 second delay to program
    lastName = askForName("Could you please enter your last name?")
    print("Thank you,",firstName,lastName)
    time.sleep(1)
    print("I will now generate your superhero kitten name")
    time.sleep(1)
    print("Thinking......")
    time.sleep(3.5)

    ##   Generating prefix and postfix
    total = calculateASCIITotal(firstName)
    ##  Use modulo to calculate an index value within the length of the array 
    prefix = listOfSuperheroPrefixes[total % len(listOfSuperheroPrefixes)]  
    total = calculateASCIITotal(lastName)
    postfix = listOfKittenPostfixes[total % len(listOfKittenPostfixes)]
    print("You shall now be called,",prefix,postfix)    ##  Prints superhero kitten name
    
def askForName(question):
    print(question) 
    name = input()  ##  Acquires user input
    return name

def calculateASCIITotal(name):
    sumOfASCII = 0
    for i in range(len(name)):  ##  Loops the length of the name
        sumOfASCII += ord(name[i])  ##  Adds ASCII Value of character at index i to ongoing total
    return sumOfASCII

main()
