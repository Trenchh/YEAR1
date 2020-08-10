###############################################  Linked list functions with recursion
def createTestList():
    lastNode = {"data":"C", "next":None}
    secondNode = {"data":"B","next":lastNode}
    firstNode = {"data":"A", "next":secondNode}
    return firstNode

def linkedListToString(LL):
    stringResult = "|"
    
    if(LL == None):
        return ""
    stringResult += str(LL["data"])
    if(LL["next"] != None) :
        stringResult += ", "
        return stringResult + linkedListToString(LL["next"])
    else:
        return stringResult

def getNodeAtIndex(LL, index):
    currentNode = LL
    currentIndex = 0
    if (index < 0) or (LL == None):
        return None
    elif(index == 0):
        return LL

    return getNodeAtIndex(LL["next"], index - 1) 

def insertValue(LL, index, value):
    if (index < 0):
        print("error")
        return LL
    if (index == 0) :
        newNode = {"data": value, "next": LL}
        return newNode
    if (LL == None):
        print("Error")
        return LL

    tail = LL["next"]
    LL["next"] = insertValue(LL["next"], index - 1, value)
    return LL

def deleteValue(LL, index):
    if (index < 0):
        print("error")
        return LL
    elif (LL == None):
        print("error")
        return LL
    elif (index == 0) :
        return LL["next"]
    else:
        LL["next"] = deleteValue(LL["next"], index - 1)
        return LL

def setValue(LL, index, value):
    if(index < 0) or (LL == None) :
        print("error")
    elif(index == 0) :
        LL["data"] = value
    else:
        setValue(LL["next"], index - 1, value)

def getLength(LL):
    if(LL == None):
        return 0
    return 1 + getLength(LL["next"])



#####################################################   Towers of Hanoi

def hanoi(numDisks, startPeg = 1, destPeg = 3, tempPeg = 2):
    if (numDisks == 1) :
        print("Move disk from peg", startPeg, "to peg", destPeg)
    else:
        hanoi(numDisks - 1, startPeg, tempPeg, destPeg)
        print("Move disk from peg", startPeg, "to peg", destPeg)
        hanoi(numDisks - 1, tempPeg, destPeg, startPeg)

def hanoi2(numDisks, startPeg = 1, destPeg = 3, tempPeg = 2):
    if (numDisks == 0) :
        return
    else:
        hanoi2(numDisks - 1, startPeg, tempPeg, destPeg)
        print("Move disk from peg", startPeg, "to peg", destPeg)
        hanoi2(numDisks - 1, tempPeg, destPeg, startPeg)

####################################################    Maze

def findPath(maze, row=0, col=0):
    ### Assume the maze is square
    ### Maze is a 2D list
    size = len(maze)

    ### Error handling
    if(row < 0) or ( row >= size) or (col < 0) or (col >= size):
        return False
    elif maze[row][col] != " ":
        return False

    maze[row][col] = "."

    ### Base case, we're done
    if (row ==(size -1)) and (col == (size - 1)):
        return Truw

    ### Recursion, not yet in bottem left corner
    if findPath(maze, row, col - 1):    #Left
        return True
    elif findPath(maze, row, col +1 ):  #Right
        return True
    elif findPath(maze, row - 1, col):  #Up
        return True
    elif findPath(maze, row + 1, col):  #Down
        return True
    
    maze[row][col] = " "
    return False

#####################################################   Expressions

def evaluate(expr):
    if isinstance(expr, dict):
        leftVal = evaluate(expr['left'])
        rightVal = evaluate(expr['right'])
        if expr['operator'] == '+':
            return leftVal + rightVal
        elif expr['operator'] == '-':
            return leftVal - rightVal
        elif expr['operator'] == '*':
            return leftVal * rightVal
        elif expr['operator'] == '/':
            return float(leftVal / rightVal)
        else:
            print("error: unknown operator")
    else:
        return expr

def exprString(expr):
    if isinstance(expr, dict):
        opPrecedence = precedence(expr)
        leftPrecedence = precedence(expr['left'])
        rightPrecendece = precedence(expr['right'])

        leftString = exprString(expr['left'])
        rightString = exprString(expr['right'])

        if leftPrecedence < opPrecedence:
            leftString = '(' + leftString + ')'
        if rightPrecedence < opPrecedence:
            rightString = '(' + rightString + ')'
        return leftString + expr["operator"] + rightString
    else:
        return str(expr)

def printExpr(expr):
    print(exprString(expr))
    
def precedence(expr):
    if isinstance(expr, dict):
        if expr['operator'] in "*/":
            return 2
        else:
            return 1
    else:
        return 3























