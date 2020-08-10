

####################################################   given height and returned all in inches
def totalInches(feet, inches):
    total = feet * 12 + inches
    return total

################################################   given two heights, sum returned in inches
def sumHeights(f1,h1,f2,h2):
    return totalInches(f1,h1) + totalInches(f2,h2)

################################################   given year, returns true if leap year
def leapYear(year):
    if(year%400 == 0):
        return true
    elif(year % 100 == 0):
        return false
    else:
        return (year % 4 == 0)


######################################   getting user input
def askName(text):
    name = input(text)
    print("Hi", name)
    print("HI" + name)

######################################   string length
myString = "This is a string"
print(len(myString))

##############################################   Putting quotations in as text
myString = "My string has quotes"""
print(myString)
myString = "My String has quotes \"\""
print(myString)

######################################################   Two lines of text
myString = "My string has \n two lines"
print(myString)

##################################################   Tab in text
myString = "My string has \t a tab "
print(myString)

################################################## Indexing a string
name = "Rob Robson"
print(name)
print(name[0])

##################################################   Comparing Strings
print("lollipop" < "pop")
## compares the first letter ascii value
print(ord("l"))
print(ord("p"))

print("Bob" == "bob")




