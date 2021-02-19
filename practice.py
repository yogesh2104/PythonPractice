'''**************Operater**************'''
# a = 3
# b = 4

# # Arithmetic Operators
# print("The value of 3+4 is ", 3+4)
# print("The value of 3-4 is ", 3-4)
# print("The value of 3*4 is ", 3*4)
# print("The value of 3/4 is ", 3/4)

# Assignment Operators 
# a = 34
# a -= 12
# a *= 12
# a /= 12
# print(a)

# Comparison Operators
# b = (14<=7)
# b = (14>=7)
# b = (14<7)
# b = (14>7)
# b = (14==7)
# b = (14!=7)
# print(b)

# # Logical Operators
# bool1 = True
# bool2 = False
# print("The value of bool1 and bool2 is", (bool1 and bool2))
# print("The value of bool1 or bool2 is", (bool1 or bool2))
# print("The value of not bool2 is", (not bool2))

'''************** End Operater**************'''


'''**************Typecasting**************'''

# a = "35fgrfg34"
# a = int(a)
# print(type(a))
# print(a + 5)

'''************** End Typecasting**************'''

'''************** Input **************'''

# a = input("Enter a number: ")
# a = int(a) # Convert a to an Integer(if possible)
# print(type(a))

'''************** End Input **************'''


'''**************String**************'''


# b = "Yogesh's" # --> Use this if you have single quotes in your strings
# b = 'Yogesh"s'
# b = '''Yogesh"s and 
#        Yogesh's'''
# print(b)
# print(type(b))

'''**************String slicing**************'''

# greeting = "Good Morning, "
# name = "Yogesh"
# print(type(name))

# Concatenating two strings
# c = greeting + name
# print(c)
# name = "Yogesh"
# print(name[4])
# name[3] = "d" --> Does not work

# print(name[1:4])
# print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
# c = name[-4:-1] # is same is name[1:4]
# print(c)

# name = "YogeshIsGood"
#  d = name[0::3]
# d = name[:0:-1]
# print(d)

'''************** End String slicing**************'''


'''************** String function**************'''

# story = "once upon a time there was a boy named Yogesh who learn python and create notes."

# String Functions
# print(len(story))
# print(story.endswith("notes"))
# print(story.count("c"))
# print(story.capitalize())
# print(story.find("upon"))
# print(story.replace("Yogesh", "YogeshIsGood"))

'''************** End String function**************'''

'''************** String practice set **************'''

# letter = '''Dear <|NAME|>,
# Greetings from ABC coding house. I am happy to tell you about your selection
# You are selected!
# Have a great day ahead!
# Thanks and regards,
# Yogesh Singh
# Date: <|DATE|>
# '''
# name = input("Enter Your Name\n")
# date = input("Enter Date\n")
# letter = letter.replace("<|NAME|>", name)
# letter = letter.replace("<|DATE|>", date)
# print(letter)

'''************** End String practice set **************'''

'''************** End String**************'''



'''************** List**************'''

# Create a list using []
# a = [1, 2 , 4, 56, 6]

# Print the list using print() function
# print(a)

# Access using index using a[0], a[1], a[2]
# print(a[2])

# Change the value of list using
# a[0] = 98
# print(a)

# We can create a list with items of different types
# c = [45, "Yogesh", False, 6.9]
# print(c)


# a =[1,2,3,45,5,6,7,8,9,0]
# a[5] = 89
# print(a)
# print(a[0:7:4])

# list1 = ["Yogesh", "singh", "mahesh"]
# list2 = [1,4,2,5,3,6,8,7,9]
# list2.sort()  #Sort the list in ascending order and return None.
# list2.reverse() # Reverse *IN PLACE*.
# list2.append(8)  # Append object to the end of the list.
# list2.insert(3,5) #Insert object before index.
# list2.pop(2) #Remove and return item at index (default last).
# print(list2)




'''************** End List **************'''

'''************** Tuple **************'''

# tup = (1,2,4,6,8,5,4,1,3,7,8,0)
# print(type(tup))
# print(tup[1],tup[4])

'''************* Tuple Method ************'''
# tup2 = tup.count(1)
# typ2 = tup.index(2)
# print(typ2)


'''************** End Tuple **************'''

'''************** List and Tuple practice set  **************'''

# list1 = []
# print(type(list1)) # to identify the class it is list or not.
# user_list = input("Enter your 1 friuts name :")
# list1.append(user_list)
# print(list1)
# user_list = input("Enter your 2 friuts name :")
# list1.append(user_list)
# print(list1)

# user_list = input("Enter your 3 friuts name :")
# list1.append(user_list)
# print(list1)

# user_list = input("Enter your 4 friuts name :")
# list1.append(user_list)
# print(list1)

# user_list = input("Enter your 5 friuts name :")
# list1.append(user_list)
# print(list1)

# user_list = input("Enter your 6 friuts name :")
# list1.append(user_list)
# print(list1)

# user_list = input("Enter your 7 friuts name :")
# list1.append(user_list)
# print(list1)


# write program to count the number of zero in the following in tuple
# tup = (7,0,8,0,0,9)
# print(tup.count(0))



'''  ************** End List and Tuple practice set  **************'''




'''  ************** Dictionary and set  **************'''

# dec = {
#     "first" : "second", "third" : "yogesh"
# }
# print(dec.keys())  # this is how all the keys of dictionary
# print(dec['first'])
# print(dec['third'])


# a = {1,2,3,43,2,3,1}
# print(type(a))
# print(a)

# a.add(8)
# a.remove(3)
# a.pop()
# print(a) 


# set1 = {"banana","cherry","apple"}
# set2 = ["asd","cvb"]
# set1.update(set2)
# print(set1)


# practice set 

# dic1 = {
#     "Shuprabhat" : "Good Morning",
#     "Bhagwan" : "God",
#     "Raat" : "Night" ,
#     "Shubah" : "Morning"
# }
# hindi_word = dic1.keys()
# print(hindi_word)
# user_input = input("Enter the word form list :")
# # print(user_input)
# print("The meaning of your word is :" , dic1[user_input.capitalize()])




# s ={18 , "18"}
# print(s)

# import this  # In python THIS module written a programming poem

# tex ="The best things in life are free!"
# if "free" in tex:
#     print("Isme hai")
# else:
#     print("Nhi hai") 

# tex ="The best things in life are free!"
# print("yogesh" not in tex)

# a = "hello"
# b = "Good boy Yogesh"
# print(a +" "+ b) #Cancatenation of string
# print(a.upper())
# print(a.strip()) #Return a copy of the string with leading and trailing whitespace removed.
# print(a.replace("hello", "good boy"))
# print(a.split(", "))


# age = 22
# txt = "Hello I am Yogesh I am {} old"
# print(txt.format(age)) #we can combine strings and numbers by using the format() method! 
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

# total = 0
# i = 1
# while i <= 100 :
#     total += i
#     i += 1
# print( "The sum of the first 100 integers is", total )

'''  ************** Dictionary and set  **************   '''

# import json # daily python trick!
# my_dic = {"b":123,"a":"abs","c":0xc0ffee}
# print(my_dic)
# print(json.dumps(my_dic, sort_keys=True, indent=3))

# a = 22
# if (a>9):
#     print("Greater")
# else:
#     print("lesser")


# q .write a program to print yes when the age entered by the user is greather than or equal to 18
# a = int(input("Enter your age :"))
# if (a >= 18):
#     print("Yes, you are adult")
# else:
#     print("You are baby")





# q find greatest number entered by user
# num1  = int(input("Enter first number :"))
# num2  = int(input("Enter second number :"))
# num3  = int(input("Enter third number :"))
# num4  = int(input("Enter fourth number :"))

# if (num1 > num4):
#     f1 = num1
# else:
#     f1 = num2
# if (num2 > num3):
#     f2 = num1
# else:
#     f2 = num2
# if (f1 > f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")



# find out student pass or fail 
# sub1 = int(input("Enter first subject marks :"))
# sub2 = int(input("Enter second subject marks :"))
# sub3 = int(input("Enter third subject marks :"))
# sub4 = int(input("Enter fourth subject marks :"))

# if (sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33):
#     print("You are fail because you got less than 33% marks")
# elif (sub1+sub2+sub3+sub4)/4 <40 :
#     print("You are fail due to total percentage less than 40")
# else:
#     print("Congratulations! You are passed the exam.")

# write program to find spam
# span_list = ["make a lot of money", "buy now", "subscribe now", "subscribe this", "click me", "click now"]
# user_span = input("Enter the message hrer :")
# if user_span in span_list:
#     spam = True
# else: 
#     spam = False
# if (spam):
#     print("This is spam message!")
# else:
#     print("This is not spam message")



#  write the program to find username contain less than 10 character

# user_name = input("Enter you name here :")
# name_len = len(user_name)
# if (name_len >= 10):
#     print("It's perfect!")
# else:
#     print("Enter your name atleast 10 character")


#  write a program to find out whether given name is present in list or not!
# ch_list = ["yogesh", "singh", "vishal", "kumar"]
# usr_enter = input("Enter word here :")
# if usr_enter in ch_list:
#     print("Word is present in list")
# else:
#     print("Contact admin to add word in list")


# a = 0 
# while a < 50:
#     a = a+1
#     print(a)


# lst = ["asd", "fgh", "trw", "sfcfb","powe","owwef","joefefq"]
# l = 0
# while l<len(lst):
#     print(lst[l])
#     l = l + 1

# num = int(input("Enter number here :"))
# i = 1 
# while i in range(1,11):
#     print(str(num) + " X " + str(i) + " = " + str(i*num))
#     i +=1



# num = int(input("Enter number :"))
# prime = True
# for i in range(2, num):
#     if (num%i == 0):
#         prime = False
#         break
# if prime:
#     print(num,"This is number Prime")
# else:
#     print(num, "This is not prime number!")



# num = int(input("Enter number here :"))
# prime = True
# for i in range(2,num):
#     if (num%i == 0):
#         prime =False
#         break
# if prime:
#     print(num, "This number is prime")
# else:
#     print(num, "This number is not prime number")



# num = 16
# sum = 0
# while(num > 0):
#     sum += num
#     num -= 1
#     # formula to calculate sum of natural number is (n*(n+1)/2)
#     print("The sum is", sum)


# num = int(input("Enter the number :"))
# total_number = int(num*(num+1)/2)
# print(total_number)

# num = int(input("Enter number here :"))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
# print(f"The factorial of number is {factorial}")



# print 
# *
# **
# ***
# ****
# n = int(input("Number of line you want to print :"))
# for i in range(n):
#     print("*" * (i+1))


# n = 3
# for i in range(3):
#     print(" " * (n-i-1), end = "")
#     print("*" * (2*i+1), end = "")
#     print(" " * (n-i-1))



# reverse table
# num = int(input("enter the number= "))
# i=1
# while i<=10:
#     print(num,"X",i,"=",num*i)
#     i= i+1



# story maker
# import random
# when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
# who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
# name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
# residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
# went = ['cinema', 'university','seminar', 'school', 'laundry']
# happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
# print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))


# class Railform:
#     def printData(self):
#         print(f"Name is {self.name}")
#         print(f"Name is {self.train}")

# tryclass = Railform()
# tryclass.name = "Yogesh Singh"
# tryclass.train = "Kurla patana"
# tryclass.printData()

# def square(x):
#     result = 0
#     for i in range(x):
#         result += x
#         return result
# print(square)





# class Emp:
#     company = "YouTube"
#     def getSalary(self):
#         print("Salary was not given")
# yog = Emp()
# # yog.getSalary()
# Emp.getSalary(yog)




# class emp:
#     company = "Google"


#     def getsalary(self):
#         print(f"salary of this empoloyee is {self.salary}")
    


    # @staticmethod  #To remove self parameter  This is also a decorator to make as a static method
#     def greet():
#         print("Good Morning,Sir")

# yogesh = emp()
# yogesh.salary = "100K"
# yogesh.greet()
# yogesh.getsalary()































