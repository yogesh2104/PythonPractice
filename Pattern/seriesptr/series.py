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

    