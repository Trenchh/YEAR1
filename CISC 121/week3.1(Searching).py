# Two searching functions
# CISC 121, fall 2014
# author: M. Lamb

# Sequential search: if target is an element of lis, returns the index
# of the first occurence of target in lis.  If target is not an
# element of lis, returns None.  Works whether lis is sorted or not.
def seqSearch(lis, target):
    for index in range(0,len(lis)):
        if lis[index] == target:
            return index
    return None    
        

# Binary search: if target is an element of lis, returns the index
# of some occurence of target in lis (not necessarily the first). If target
# is not an element of lis, returns None.
def binSearch(lis, target):
    if len(lis) == 0:
        return None
    low = 0
    high = len(lis)-1
    while low <= high:
        # Invariant: If target is in list,
        # target is in lis[low:high]
        mid = int((low+high)/2)
        if lis[mid] == target:
            return mid
        elif target < lis[mid]:
            high = mid-1
        else: # target > lis[mid]
            low = mid+1
    return None


# Search works with strings too!
# lists of strings for testing
fruit = ["cherry", "apple", "peach", "lemon", "banana", \
         "apricot", "strawberry", "kiwi", "cantalope"]
sortedFruit = ['apple', 'apricot', 'banana', 'cantalope', 'cherry', \
               'kiwi', 'lemon', 'peach', 'strawberry']


"""
Helper function for testing: creates a list of random numbers
Parameter: the length for the list
"""
import random
def randomList(length):
    randList = []
    for i in range(length):
        # Using numbers between 0 and length will produce a list
        # containing duplicates.  Try 100*length instead to get a
        # list with few duplicates to see if that affects performance.
        randList.append(random.randint(0,length))
    return randList

"""
Helper function for testing: creates a SORTED list of random numbers
Parameter: the length for the list
"""
def randomSortedList(length):
    result = []
    n = 0
    for i in range(length):
        n += random.randint(1,5)
        result.append(n)
    return result



