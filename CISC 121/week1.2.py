#####################################################################For loop
##for i in range(0,12):
##    print(i)
##    if i > 6:
##        print(i)
##        continue #goes back up to next iteration of the loop
##    else:
##        i = i+1
##        print(i)



###############################################################infinite loop
##while True:
##    print("infinite") #CONTROL C TO BREAK THE LOOP



#################################################################Functions
##def theDate(year = 2017, month = "September"):
##    ##print(year)
##    return(year, month)
##
##a = theDate(2017)
##a+= 25
##print(a)



#####################################################Global Variables
##PI = 3.14 #automatically global
##
##def main():
##    global PI #declared as global in function
##    PI = 3.14
##
##def mainB():
##    print(PI)
##
##main()
##mainB()



#############################################is vs ==
##a = 4
##b = 7
##print(a == b)
##print(a is b)
##
##print(id(a))
##print(id(b))
##
##b = 4
##print(a is b)
##
##a = float('nan')
##b = float('nan')
##print(a is b)
##
#is compares id's, == compares values



#####################################Order of operations
##x = 2+3 ** 2-4/2
##print(x)
##
##y = (2+3) ** 2-4/2
##print(y)
##


###################################################Function examples
def helloWorld():
    print("Hello, World!")

helloWorld()

def greeting(name, age):
    print("Hello", name)
    print("You are ", age, " years old")
    
greeting("Ryan", 18)
























