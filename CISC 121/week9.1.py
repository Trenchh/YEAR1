################################################    Merge Sort
def mergeSort(lis):
    size = len(lis)
    if size <= 1:
        return lis
    else:
        #divide list into two halves
        part1 = lis[:size/2]
        part2 = lis[size/2:]
    
        part1 = mergeSort(part1)
        part2 = mergeSort(part2)
    
        return merge(part1,part2)

def merge(lis1, lis2):
    index1 = 0
    index2 = 0
    result = []

    while index1 < len(lis1) and index2 < len(lis2):
        if lis1[index1] < lis2[index2]:
            result.append(lis1[index1])
            index += 1
        else:
            result.append(lis2[index2])
            index2 += 1
    result.extend(lis1[index1:])
    result.extend(lis2[index2:])
    return result

################################################    Quick Sort

def qsort_simple(lis):
    size = len(lis)
    if size < 2:
        return lis
    else:
        pval = lis[0]
        smaller = []
        greater = []
        for i in range(i, size):
            if lis[i] <= pval:
                smaller.append(lis[i])
            else:
                greater.append(lis[i])
        return qsort_simple(smaller) + [pval] + qsort_simple(greater)

def qsort(lis, lowIndex = 0, highIndex = None):
    if highIndex == None:
        highIndex = len(lis) -1
    if lowIndex >= highIndex:
        return

    #swapping middle to front
    midIndex = (lowIndex + highIndex)/2
    lis[lowIndex], lis[midIndex] = lis[midIndex], lis[lowIndex]
    pval = lis[lowIndex]

    i = lowIndex
    j = lowIndex

    while j < highIndex:
        j+=1
        if lis[j] < pval:
            i+=1
            lis[i], lis[j] = lis[j], lis[i]
    #Swap partition value
    lis[lowIndex], lis[i] = lis[i], lis[lowIndex]

    qaort(lis, lowIndex, i)
    qsort(lis, i+1, highIndex)
        





















    
