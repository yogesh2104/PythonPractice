import numpy as np
# data = [8,89,67,55,46,3,22,56,78,12,32,11,5,76,90]
# data2 = [82,80,61,53,47,39,22,52,78,12,30,16,5,78,90]



# # sort() function return a sorted copy of an array.
# print(np.sort(data))
# print()

# # output   [ 3  5  8 11 12 22 32 46 55 56 67 76 78 89 90]



# """greater_equal()it compare two list and return true or False.if the number is greater or 
#  equal return ##! True 
#  else retuen ##! False"""
# print(np.greater_equal(data,data2))
# print()

# # output [False  True  True  True False False  True  True  True  True  True False True False  True]




# """greater() it compare two list and return true or False.if the number is greater then return ##!True 
#  else retuen ##! False"""
# print(np.greater(data, data2))
# print()

# # output [False  True  True  True False False False  True False False  True False False False False]

# """less_equal() it compare two list and return true or False.if the number is less or equal then
# return ##! True 
# else retuen ##! False"""
# print(np.less_equal(data, data2))
# print()

# # output [ True False False False  True  True  True False  True  True False  True True  True  True]



# """less() it compare two list and return true or False.if the number is less then return ##!True 
# else retuen ##! False"""
# print(np.less(data,data2))

# # output [ True False False False  True  True False False False False False  True False  True False]


##? broadcasting in numpy
# bring array with different shapes into the same shape
# during arithmetic operation is complex with the help of numpy you can do easily.
# Create an array.
# salary = np.array([2000,4000,12000,43210,8000])
# salary_bonus = 1.1
# print(salary*salary_bonus)
# print(salary/salary_bonus)
# print(salary+salary_bonus)

# ? Boolean indexing in numpy
a = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
indices = np.array([[False,False,True],
                    [False,False,False],
                    [True,True,False]])

print(a[indices])
# output [3 7 8]
"""[Explanation]
We create two arrays “a” and “indices”. The first array contains
two-dimensional numerical data. The second array has the same shape and contains Boolean values. 
You can use the indexing array for finegrained data array access. This creates a new NumPy array from
the data array containing only those elements for which the
indexing array contains “True” Boolean values at the respective
array positions. Thus, the resulting array contains the three
values 3, 7, and 8 """
