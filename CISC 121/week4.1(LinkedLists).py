##################################  Linked Lists
def main():
    LL = createTestList()
    print(LL["data"])
    print(LL["next"]["data"])

def createTestList():
    lastNode = {"data":"C", "next":None}
    secondNode = {"data":"B","next":lastNode}
    firstNode = {"data":"A", "next":secondNode}
    return firstNode

"""
COMPLETED VERSION OF THE LINKED LIST MODULE
CISC 121, fall 2014
M. Lamb
"""

def insertValue(linkedList, index, value):
    """
    Adds a new element to a list.
    Parameters:
        value: the value for the new element
        index: the index for the new list element
    The new value does not replace the current element at
    position index; it is inserted before that element and
    the size of the list grows by 1.
    
    The return value is the head of the modified list.
    (That's usually the same as the lis parameter, unless
    we've added a new first element.)
    
    If the index is out of bounds, prints an error message and
    returns the list unchanged.
    """
    # special case: adding to start of list
    if index == 0:
        newNode = {'data':value, \
                   'next':linkedList}
        return newNode

    else:
        newNode = {'data':value}
        before = nthNode(linkedList, index-1)
        if before == None:
            print( "error: attempt to add list" +\
                  "value at illegal index")
            return linkedList
        after = before['next']
        before['next'] = newNode
        newNode['next'] = after
        return linkedList
        

        
def listString(linkedList):
    """
    Returns a string describing the list, suitable for printing.
    """
    result = '['
    current = linkedList
    while current != None:
        result += str(current['data'])
        current = current['next']
        if current != None:
            result += ","
    return result + ']'


def printList(linkedList):
    """
    Prints a representation of a list
    """
    print (listString(linkedList))
    

def createList(plist):
    """
    Creates and returns a linked list containing all of the elements
    of the Python-style list parameter.  A useful shortcut for testing.
    """
    result = None # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist)-1,-1,-1):
        result = insertValue(result, 0, plist[index])
    return result
        

def nthNode(linkedList, n):
    """
    Helper method: returns a reference to node n in a list
    (counting from zero).
    Parameters: the list and an index n
    If there is no node n, returns None.  No error message, because
    this isn't necessarily an error, depending on where the function
    is being called.
    """

    if n < 0:
        return None
    current = linkedList
    count = 0
    while count < n and current != None:
        current = current['next']
        count += 1
    return current


def get(linkedList, index):
    """
    Returns the value of a list element
    Parameters: the list and the index of the element
    If the index is not the index of an existing list element,
        prints an error message and returns None
    """
    node = nthNode(linkedList,index)
    if node == None:
        print ("error")
    return node['data']


def set(linkedList, index, value):
    """
    Changes the value of a list element
    Parameters: the index of the element and the new value
    No return value (always None).
    If the index is not the index of an existing list element,
        writes an error and returns the list unchanged
    """
    node = nthNode(linkedList,index)
    if node == None:
        print ("error")
    else:
        node['data'] = value



def delete(linkedList, index):
    """
    Deletes an element from a linked list.
    Parameter: list and index of the element to delete
    
    The return value is the head of the modified list.
    (That's usually the same as the linkedList parameter, unless
    we've deleted the first element.)
    
    If the index is out of bounds, writes an error message and
    returns the list unchanged.
    """
    if index == 0:
        return linkedList['next']
    
    before = nthNode(linkedList, index-1)
    if before == None:
        print ("error: attempt to delete list " +\
              "element at illegal index")
        return linkedList
        
    nodeToDelete = before['next']
    after = nodeToDelete['next']
    before['next'] = after
    return linkedList


def getSize(linkedList):
    """
    Returns the size of a list
    """
    count = 0
    node = linkedList
    while node != None:
        count += 1
        node = node['next']
    return count











