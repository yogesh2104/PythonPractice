# Arithmetic series
"""[Print]
    1, 4, 7, 10, 13, 16,....

"""
#number of limit to print
n = 5  
#difference between two number
d = 3 
 #terms
a = 1 

for x in range(1,n+1):
    print("" + str(a),end=",")
    a =a+d




# Geometric Series
    """[print]
    5,10,20,40,80,160,....
    """
#number of limit to print
n = 7 
#ratio diff between two number
r = 2 
#terms
a = 5 
for x in range(1,n+1):
    print(""+str(a),end=",")
    a =a*r


# odd No. Series
    """[print]
    1,3,5,7,9,
    """
n = 5 
for x in range(1,n+1):
    print(""+str(2*x-1),end=",")

    
# even number
    """[print]
    2,4,6,8,10,12,....
    """
n = 6
for x in range(1,n+1):
    print(""+str(2*x),end=",")


# square number
    """[print]
    1,4,9,16,25,....
    """
n=6
for x in range(1,n+1):
    print(x*x,end=",")



"""[print]
  Cube Number [1,8,27,64,125,216,...]
"""
n =6
for x in range(1,n+1):
    print(x*x*x,end=",")



"""[print]
fibonacci Number series [1,1,2,3,5,8,13,21,...]
"""

n = 15
a = 0
b = 1
c = a+b
while(c<=n):
    print(c,end=",")
    c = a+b
    a=b
    b=c


"""[print]
Prime Number [2,3,5,7,11,13,17,.....]
"""
n = 10
num = 1
count = 0
while(num<=n):
    for x in range(1,num+1):
    if(num%x==0):
            count +=1
        if(count==2):
            print(num,end="")
            count = 0
            num += 1