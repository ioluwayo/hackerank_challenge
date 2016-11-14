# Created by Ibukun on 10/30/2016.
'''
    This program is my solution to the "diagonal difference" challenge on hackerrank.
    Given a square matrix of size ,N X N calculate the absolute difference between the sums of its diagonals.
    Input format :
    The first line should contain a single integer, N. The next N lines denote the matrix's rows,
    with each line containing N space-separated integers describing the columns.
'''
n = int(raw_input().strip())
# read a line from stdin
a = []
# create a list variable
for a_i in xrange(n):
    # the map allows you to use 0,1,2... as keys
    a_temp = map(int, raw_input().strip().split(' '))
    # strip the string of trailing spaces and new line, then split it by space.
    # store it as a list of integers in a_temp
    a.append(a_temp)
    # append the list into this list
right = []
left = []
for i in range(n):
    # the premise is to identify the diagonal.
    # apparently in  a matrix, its just [0][0],[1][][2][2]...[n-1][n-1]
    right.append(a[i][i])
    # the left diagonal tho is just the revers. so [1][n-1],[1][n-2]....[n-1][0]
    left.append((a[i][n-(i+1)]))
print (abs(sum(right)-sum(left)))
# print the difference of the diagonal sum
