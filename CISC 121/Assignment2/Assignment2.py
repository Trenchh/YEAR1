##  Name: Assignment2
##  Date: October 18th, 2017
##  Version: v0.1
##  Author: Ryan Protheroe

def isSorted(nums): 
    """
    Assumes nums is a linked list of numbers.  
    Returns True if the values in nums are sorted in non-decreasing order,
    False otherwise.  An empty or one-element list is considered sorted.
    """
    ### Check for empty list
    if get(nums, 0) == None:
        print("Empty List")
        return None
    else:
        ### runs through list and check that value is less than next one
        for i in range(getSize(nums) - 1): 
            if (get(nums,i) > get(nums, i + 1)):
                return False
    return True 

def noDups(nums):
    """
    Assumes nums is a linked list of numbers sorted in non-decreasing order.
    Modifies nums to get rid of all duplicate elements.
    Returns a pointer to the first element of the modified version
    of nums
    """
    if get(nums, 0) == None:
        print("Empty List")
        return None
    else:
        i = 0
        while i < getSize(nums) - 1:
            if (get(nums,i) == get(nums, i + 1)):
                nums = delete(nums, i+1)
                i -= 1 
            i += 1
        return nums

def insertInOrder(linkedList, value):
    """
    Inserts a value into a sorted linked list.  Assumes the linkedList
    parameter is sorted in non-decreasing order.
    """
    if get(linkedList, 0) == None:
        print("Empty List")
        return None
    else:
        ### Insert at head
        if get(linkedList,0) > value:
            linkedList = insertValue(linkedList,0,value)
        ### Insert at tail
        elif get(linkedList, getSize(linkedList) - 1) < value:
            linkedList = insertValue(linkedList,getSize(linkedList),value)
        ### If value doesn't exist in list
        elif seqSearch(linkedList, value) == None:
            for index in range(getSize(linkedList)):
                if get(linkedList, index) > value and get(linkedList, index - 1) < value:
                    linkedList = insertValue(linkedList, index, value)
        ### If value already exists in list
        else:   
            index = seqSearch(linkedList, value)
            linkedList = insertValue(linkedList, index, value)
        return linkedList

def sort(nums):
    """
    Assumes nums is a list of numbers but does NOT assume nums is sorted.
    Returns a sorted copy of nums.
    """
    if get(nums, 0) == None:
        print("Empty List")
        return None
    else:
        i = 0
        ### Creating new list
        placeHolder = {'data':1, 'next':None}
        while i < getSize(nums):
            ### Adding fist "real" value to list
            if i == 0:
                value = get(nums,i)
                sortedList = insertValue(placeHolder,i,value)
                sortedList = delete(sortedList, 1)
            ### Sorting List
            else:
                sortedList = insertInOrder(sortedList,get(nums,i))
            i+=1
        return sortedList

#########################################################################################################
# The following functions are "Helper Functions"
#########################################################################################################

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
    
    before = nthNode(linkedList, index - 1)
    if before == None:
        print ("error: attempt to delete list " +\
              "element at illegal index")
        return linkedList
        
    nodeToDelete = before['next']
    after = nodeToDelete['next']
    before['next'] = after
    return linkedList

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
        return None
    return node['data']

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

def seqSearch(linkedList, target):
    """
    Searches through list to find value
    Returns index where value is found
    """
    for index in range(getSize(linkedList)):
        if get(linkedList, index) == target:
            return index
    return None

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
        before = nthNode(linkedList, index - 1)
        if before == None:
            print( "error: attempt to add list" +\
                  "value at illegal index")
            return linkedList
        after = before['next']
        before['next'] = newNode
        newNode['next'] = after
        return linkedList
                    

#########################################################################################################
# The following functions are included for testing purposes, so that you can easily create and print
# linked lists.  You may not call these functions from any of your required functions.
#########################################################################################################

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
    print(listString(linkedList))
    

def createList(plist):
    """
    Creates and returns a linked list containing all of the elements
    of the Python-style list parameter.  A useful shortcut for testing.
    """
    result = None # empty list

    # loop through plist in reverse order and add each element to the
    # start of the result
    for index in range(len(plist)-1,-1,-1):
        result = {'data':plist[index], 'next':result}
    return result
        








