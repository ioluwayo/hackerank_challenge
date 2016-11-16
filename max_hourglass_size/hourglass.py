# Created by Ibukun on 11/16/2016.


"""
    consider the array ARR below
                1 1 1 0 0 0
                0 1 0 0 0 0
                1 1 1 0 0 0
                0 0 0 0 0 0
                0 0 0 0 0 0
                0 0 0 0 0 0
    We define an hourglass in  to be a subset of values with indices
    falling in this pattern blow in ARR's graphical representation:
                    a b c
                      d
                    e f g
    There ar 16 hour glasses in ARR.
    Calculate the hourglass sum for every hourglass in ARR, then print the maximum hourglass sum.
    ARR contains the following hour glasses:
            1 1 1   1 1 0   1 0 0   0 0 0
              1       0       0       0
            1 1 1   1 1 0   1 0 0   0 0 0
            
            0 1 0   1 0 0   0 0 0   0 0 0
              1       1       0       0
            0 0 2   0 2 4   2 4 4   4 4 0
            
            1 1 1   1 1 0   1 0 0   0 0 0
              0       2       4       4
            0 0 0   0 0 2   0 2 0   2 0 0
            
            0 0 2   0 2 4   2 4 4   4 4 0
              0       0       2       0
            0 0 1   0 1 2   1 2 4   2 4 0
    the sum of the hour glass with the largest sum is 19
    the hour glass is
                    2 4 4
                      2
                    1 2 4
"""
# solution
arr = [1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],[1, 1, 1, 0, 0, 0],[0, 0, 2, 4, 4, 0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]
hourglass = []
for i in xrange(len(arr)-2):
    for j in xrange(len(arr[i])-2):
        hourglass.append([arr[i][j], arr[i][j+1], arr[i][j+2],arr[i+1][j+1],arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]])
x = []
for i in xrange(len(hourglass)):
    x.append(sum(hourglass[i]))
print (max(x))