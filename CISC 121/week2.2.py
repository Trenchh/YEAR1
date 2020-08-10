##single quotes vs double
##if you want quotation marks in string, use the opposite of the marks,
##ex: use single ' to include " in quote
print("'hello'")
print('"hello"')

#######################################################   LISTS
myList = [1,2,3,4,5]
print(myList)

myList = ["hello", "hi", "yes"]
print(myList)

####    can have ultiple data types
myList = ["eyes", 1, 2]
print(myList)

a = 1
b = 2
c = 3

myList = [a,b,c]
print(myList)

####    accessing list
print(myList[0])
print(myList[1])
print(myList[2])

myList = ["I", "like", "chocolate"]
print(myList[0])
print(myList[1])
print(myList[2])

####    changing value in list
myList[2] = "cake"
print(myList[0])
print(myList[1])
print(myList[2])

####    Inserting a value
myList.insert(1, "do not")
print(myList)

####    Adding to the end of the list
myList.append("?")
print(myList)

####    Remove an element
myList.pop(1)
print(myList)

####    idk what relevance this has
myList+= myList
print(myList)

myList = [1,2,3]
print(myList*2)

####    Loops
myList = ["keep", "on", "trucking", "you", "are", "doing", "great"]
for i in myList:
    print(i)

for i in range(len(myList)):
    print(myList[i])

fruitSalad = ["apple", "banana", "orange"]
for fruit in fruitSalad:
    print(fruit)
    fruit = "watermelon"
    print(fruitSalad)




#### practice

fruitSalad = ["tomato", "lettuce", "strawberry", "chicken"]
fruit = ["tomato", "strawberry", "apple", "orange"]
notFruit = []

for i in fruitSalad:
    if i in fruit:
        print(i)
    else:
        notFruit.append(i)
print(notFruit)

for i in notFruit:
    fruitSalad.remove(i)
print(fruitSalad)

        













