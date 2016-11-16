# Created by Ibukun on 11/16/2016.

"""
    Given a base-10 integer, n, convert it to binary (base-2).
    Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
"""

def decToBin(n):
    arr = []
    while n:
        if n == 0:
            arr.append(0)
        else:
            arr.append(n % 2)
            n = n / 2
    arr.reverse()
    print arr
    return arr


def countConsecOnes(arr):
    count = []
    num = 0
    for i in arr:
        if i == 0:
            count.append(num)
            num = 0
        else:
            num += 1
    count.append(num)
    if not count:
        return sum(arr)
    return max(count)


# assume n = 439
n = 439
print (countConsecOnes(decToBin(n)))