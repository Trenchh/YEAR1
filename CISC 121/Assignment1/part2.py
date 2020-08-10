##  PART 2
##  Name: Find The Space Junk
##  Date: September 29th, 2017
##  Version: v0.1
##  Author: Ryan Protheroe
##  Description: This program reads a .bdi file that if there is a 1 surrounded by 0's it is declared space junk
##               and the indices of the space junk is printed out

def main2():
    content = readBasicDigitalImageFile("space.bdi")    ##2D array of .bdi file
    count = 0
    for r in range(len(content)):   ## Loops through rows
        for c in range(len(content[r])):    ## Loops through columns
            check = isPixelSpaceJunk(content,r,c)
            if check == True:
                count += 1
                print("row:",r,"column:",c,"is junk")
    print("There is a total of:",count,"pixels that are space junk")

def isPixelSpaceJunk(myList, row, column):
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
    with open(fileName) as textFile:
        rows = [line.split() for line in textFile]  ## Creates 2D Array of rows in space.bdi
    return rows

main2()
