'''
[question]
3
3 2
3 2 1
3 2 1 0
3 2 1
3 2
3
'''
size = 3
for x in range(size,-(size+1),-1):
    for y in range(size, abs(x)-1,-1):
        print(y,end="")
    print()



'''
[print]
3
23
123
0123
123
23
3
'''

size = 3
for x in range(size,-(size+1),-1):
    for y in range(abs(x),size+1):
        print(y,end="")
    print()




'''[Question is]
D
DC
DCB
DCBA
DCB
DC
D
'''
size = 3
for x in range(size,-(size+1),-1):
    for y in range(size, abs(x)-1,-1):
        print(chr(y+65),end="")
    print()



"""
[print]
11111
22222
33333
44444
55555

"""
for x in range(1,6):
    for y in range(1,6):
        print(x,end="")
    print()



"""[print]
    12345
    12345
    12345
    12345
    12345
"""
for x in range(1,6):
    for y in range(1,6):
        print(y,end="")
    print()




"""[print]

55555
44444
33333
22222
11111

"""
for x in range(5,0,-1):
    for y in range(5,0,-1):
        print(x,end="")
    print()



"""[print]
    54321
    54321
    54321
    54321
    54321   
"""
for x in range(5,0,-1):
    for y in range(5,0,-1):
        print(y,end="")
    print()


"""[print]
    1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
"""
n=5
k=1
for x in range(1,n+1):
    for y in range(1,n+1):
        print("{:2d}".format(k),end="")
        k+=1
    print()
