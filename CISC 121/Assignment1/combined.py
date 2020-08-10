##  PART 1
##  Name: Superhero Kitten Name Generator
##  Date: September 25th, 2017
##  Version: v0.3:  Comments included, enhanced style
##  Author: Ryan Protheroe
##  Description: Assigns the user a superhero kitten name based on the ascii values of their first and
##               last name

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
    time.sleep(4)

    ##   Generating prefix and postfix
    totalASCII = calculateASCIITotal(firstName)
    ##  Use modulo to calculate an index value within the length of the array 
    prefix = listOfSuperheroPrefixes[totalASCII % len(listOfSuperheroPrefixes)]  
    totalASCII = calculateASCIITotal(lastName)
    postfix = listOfKittenPostfixes[totalASCII % len(listOfKittenPostfixes)]
    print("You shall now be called,",prefix,postfix)    ##  Prints superhero kitten name
    
def askForName(question):
    """
    Parameter must ask user for either first name or last name
    Return value is the name entered
    """
    print(question) 
    name = input()  ##  Acquires user input
    return name

def calculateASCIITotal(name):
    """
    Parameter is either first name or last name entered by user
    Return value is the sum of the ASCII values that make up such name entered
    """
    sumOfASCII = 0
    for i in range(len(name)):  ##  Loops the length of the name
        sumOfASCII += ord(name[i])  ##  Adds ASCII Value of character at index i to ongoing total
    return sumOfASCII

main()


##  PART 2
##  Name: Find The Space Junk
##  Date: September 29th, 2017
##  Version: v0.2:  Comments included, enhanced style
##  Author: Ryan Protheroe
##  Description: This program reads a .bdi file that if there is a 1 surrounded by 0's it is declared 
##               space junk and the indices of the space junk is printed out

def main2():
    """
    Loops through each value in space.bdi using rows and columns
    Counts the total amount of spacejunk and prints indexes of each
    piece of space junk found
    """
    content = readBasicDigitalImageFile("space.bdi")    ##2D array of .bdi file
    count = 0
    for row in range(len(content)):   ## Loops through rows
        for column in range(len(content[row])):    ## Loops through columns
            check = isPixelSpaceJunk(content,row,column)
            if check == True:
                count += 1
                print("row:",row,"column:",column,"is junk")
    print("There is a total of:",count,"pixels that are space junk")

def isPixelSpaceJunk(myList, row, column):
    """
    Loops through 2D Array of .bdi file using two index's,
    a row and a column, to find values of 1 surrounded by 0's.
    Uses a counter to assure the 1 is surrounded, there should be 8
    0's surrounding the 1.
    Returns a boolean of true or false based on "count" total.
    """
    if int(myList[row][column]) == 1:   ## Only runs if the value at index is a 1
        count = 0
        for r in range(0,3):    ## Need to check 3 rows, the current one, one above and one below
            for c in range(0,3):    ## Need to check 3 columns, the current one, one to the left and one to the right
                if int(myList[row + 1 - r][column + 1 - c]) == 0:   ## Makes sure 1 is surrounded by 0's
                    count += 1     ## Counts number of 0's around the 1   
        if count == 8:  ## Assures the 1 is surrounded by 0's
            return True
        else:
            return False
    else:
        return False
        
def readBasicDigitalImageFile(fileName):
    """
    Reads file and organizes it into a 2D array of "rows",
    returns 2D array
    """
    with open(fileName) as textFile:
        rows = [line.split() for line in textFile]  ## Creates 2D Array of rows in space.bdi
    return rows

main2()
