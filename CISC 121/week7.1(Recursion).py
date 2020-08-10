def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact*=i
    return fact

#####   Recursively
def fact(n):
    if n <= 1:
        result = 1
    else:
        result = n * fact(n-1)
    return result

#####   Infinite loop/// base case always needed
def badFact(n):
    result = n * badFact(n-1)
    return result

#####   Divide and conquer
def product(a,b):
    if a > b:
        result = 1
    elif a == b:
        return a
    return a * product(a+1, b)

def factorial(n):
    return product(1,n)

#####   Palindromes
def palindrome(string):
    if len(string) < 2:
        return True
    else:
        if string[0] != string[-1]:
            return False
        else:
            return palindrome(string[1:-1])

#####   Recursive Fibonacci
def recursiveFib(n):
    if n <= 1:
        return n
    else:
        return recursiveFib(n-1) + recursiveFib(n-2)
        
#####   Iterative Fibonacci
def iterativeFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        count = 1
        currentFib = 1
        previousFib = 0
        while count < n:
            newFib = currentFib + previousFib
            previousFib = currentFib
            currentFib = newFib
            count +=1
        return currentFib

#####   Reversing String
def reverse(string):
    if len(string) < 2:
        return string
    else:
        print(string)
        return reverse(string[1:]) + string[0]










    
