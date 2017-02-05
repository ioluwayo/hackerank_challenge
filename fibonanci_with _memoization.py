# Created by ioluwayo on 2017-02-05.
"""
Used a dictionary to store solutions to sub problems "fib(n-1) fib(n-2)" in computing the Nth fibonacci number
The basic algorithm has an exponential time complexity. However, with very simple memoization
the time complexity is about O(n). Since calls to fib(n-1) and fib(n-2) may result in O(1) look up time
in the dictionary.
"""
import sys
def fibo(n):
    fib = {} # for storing fib(n) results
    for k in range(1,n+1):
        if k<=2: f = 1 # base case;
        else: f = fib[k-1]+fib[k-2]
        fib[k] = f
    return fib[n] # just a look up.
if __name__ == '__main__':
    n = int (sys.argv[1]) # command line input.
    print fibo(n)