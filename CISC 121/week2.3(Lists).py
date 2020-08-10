##################################    2D Lists
myList = [[1,2,3],[4,5,6]]

print(myList[0][1])
##  print the rows
print(myList[0])
print(myList[1])

##  print only first two elements of second row
print(myList[1][0:2])

##  Print the columns
print([row[0] for row in myList])
print([row[1] for row in myList])
print([row[2] for row in myList])

##  Number of rows
print(len(myList))

##  Number of columns
print(len(myList[0]))

##  Print the elements of the list
for row in myList:
    for i in row:
        print(i)

##  Alernatively:
for i in range(len(myList)):
    for j in range(len(myList[0])):
        print(myList[i][j])


#####################################    Reading from files
##  output exp to a new file /// reading data
exp = []

infile = open('space.bdi', 'r')
reader = infile.read()

for row in reader:
    newRow = []
    for i in row:
        newRow.append(i)
    exp.append(newRow)
    infile.close()

##  List comprehension    
with open('space.bdi') as infile:
    exp = [[int(r) for r in row.split()] for row in infile]

##  check value type
print(type(exp[0][0]))
##  or    
print(type(exp[0][0] is float))


rows = len(exp)
cols = len(exp[0])
for row in range(rows):
      for col in range(cols):
          data = exp[row][col] * 9
          data += 1
          exp[row][col] = data


    
    








