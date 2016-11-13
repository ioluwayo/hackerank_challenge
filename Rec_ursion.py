# Created by Ibukun on 11/9/2016.
'''

    This program calculates the factorial of a number provided through stdin using recursion.

'''
def factorial(N):
    if N <= 1:
        return N
    else:
        return N * factorial(N-1)
    
print "This program uses recursion to find the factorial of a number"
try:
    n = input("Enter a number and press enter: ")
except:
    print "You did not enter a number. Try again"
    quit()
print factorial(int(n))

