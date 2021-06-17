'''
question

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


size = 3
for x in range(size,-(size+1),-1):
    for y in range(size, abs(x)-1,-1):
        print(chr(y+65),end="")
    print()