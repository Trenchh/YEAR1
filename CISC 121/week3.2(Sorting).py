########################################################    Sorting
####    Bubble Sort
####    Simple, easy to program, but slow
####    Takes pairs of values, if the first is greataer than the next, it swaps, and keeps doing so
####    until the list is all sorted

def bubbleSort(lis):
    for maxIndex in range(len(lis) - 1, 0, -1):
        for i in range(0, maxIndex):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i+1] = lis[i+1], lis[i] #Swapping elements
    

####    Selection Sort
####    Fairly simple and much faster than bubble sort at greater list sizes
####    Finds smallest value then brings to the front and keeps reiterating
def selSort(lis):
    for i in range(len(lis) - 1):
        minIndex = i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[minIndex]:
                minIndex = j
        lis[i], lis[minIndex] = lis[minIndex], lis[i]


import random
def randomList(length):
    rand = []
    for i in range(length):
        rand.append(random.randint(0,length))
    return rand
