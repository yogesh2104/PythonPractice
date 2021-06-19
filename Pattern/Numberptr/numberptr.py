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
    1   2  3  4  5
    6   7  8  9 10
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


    
"""[print]
    1  3  5  7  9
    11 13 15 17 19
    21 23 25 27 29
    31 33 35 37 39
    41 43 45 47 49
    
"""
n=5
k=1
for x in range(1,n+1):
    for y in range(1,n+1):
        print("{:2d}".format(k),end="")
        k+=2
    print()


"""[print]
2  4  6  8  10
12 14 16 18 20
22 24 26 28 30
32 34 36 38 40
42 44 46 48 50
"""
n=6
k=2
for x in range(2,n+1):
    for y in range(2,n+1):
        print("{:2d}".format(k),end="")
        k+=2
    print()




"""[print]
 1 2 3 4 5
 2 4 6 810
 3 6 91215
 4 8121620
 510152025
"""
n=5
for x in range(1,n+1):
    for y in range(1,n+1):
        print("{:2d}".format(x*y),end="")
    print()



"""[print]
1 12 13 1
1 22 23 2
1 32 33 3
1 42 43 4
1 52 53 5
"""
for x in range(1,6):
    for y in range(1,4):
        print(f"{y} {x}",end="")
    print()




"""[print]

    111213
    212223
    313233
    414243
    515253
"""
for x in range(1,6):
    for y in range(1,4):
        print(f"{x}{y}",end="")
    print()
