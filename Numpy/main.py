import numpy as np
data = [8,89,67,55,46,3,22,56,78,12,32,11,5,76,90]
data2 = [82,80,61,53,47,39,22,52,78,12,30,16,5,78,90]



# sort() function return a sorted copy of an array.
print(np.sort(data))
print()



"""greater_equal()it compare two list and return true or False.if the number is greater or 
 equal return ##! True 
 else retuen ##! False"""
print(np.greater_equal(data,data2))
print()


"""greater() it compare two list and return true or False.if the number is greater then return ##!True 
 else retuen ##! False"""
print(np.greater(data, data2))
print()

"""less_equal() it compare two list and return true or False.if the number is less or equal then
return ##! True 
else retuen ##! False"""
print(np.less_equal(data, data2))
print()



"""less() it compare two list and return true or False.if the number is less then return ##!True 
else retuen ##! False"""
print(np.less(data,data2))