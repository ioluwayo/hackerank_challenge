# Created by Ibukun on 11/12/2016.


'''

    After an exhausting morning, Mirko fell asleep. His brother Stanko, however,
    just awoke and, like his brother, is all about excitement.
    Stanko found N rings of varying radiuses in the garage.
    He arranged them on the floor so that each ring (except the first and last) touches the ones before and after it.
    
    He started turning the first ring and noticed that the other rings turned as well; some faster, some slower!
    Thrilled with his discovery, he decided to count how many times the other rings turn while the first ring turns
    once. He gave up after noticing that this number is not always an integer and not knowing what to do.
    
    Write a program that determines how many times each ring turns while the first turns once.
    input file : prsteni.txt
    
'''


from fractions import Fraction
infile = open("prsteni.txt")
n = int(infile.readline())
radius = infile.readline().strip().split(' ')
for i in range(1, n):
    if Fraction(float(radius[0])/float(radius[i]))% 1:
        print Fraction(int(radius[0]), int(radius[i]))
    else:
        print str(Fraction(int(radius[0]), int(radius[i])))+'/1'