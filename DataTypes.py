# ==========================================================================================
# Data Types in Python: Python needs to understand how data is treated. That is why data types are required. Data types are used to define the type of value a variable can hold.
# Python has several built-in data types that are used to define the type of value a variable can hold.
# The main data types are:
# - int: for integers
# - float: for floating-point numbers
# - str: for strings
# - bool: for boolean values

# There are 3 categories of data types in Python:
# 1. Contatining no values: NoneType
# 2. Containing single value: Numeric(int, float, complex), str, bool, Date & Time(datetime, date, time).
# 3. Containing multiple values: list, tuple, set, dict, array.

# ==========================================================================================

a = 10      #This is an integer
type_of_a = type(a) #This will return the data type of variable a, which is <class 'int'>
print("The data type of variable a is:", type_of_a) #This will print the data type of variable a

b = 10.5    #This is a float
type_of_b = type(b) #This will return the data type of variable b, which is <class 'float'>
print("The data type of variable b is:", type_of_b) #This will print the data type of variable b

c = "Hello" #This is a string
type_of_c = type(c) #This will return the data type of variable c, which is <class 'str'>
print("The data type of variable c is:", type_of_c) #This will print the data type of variable c

d = 'World' #This is a string
type_of_d = type(d) #This will return the data type of variable d, which is <class 'str'>
print("The data type of variable d is:", type_of_d) #This will print the data type of variable d

e = "10"    #This is a string, even though it looks like an integer
type_of_e = type(e) #This will return the data type of variable e, which is <class 'str'>
print("The data type of variable e is:", type_of_e) #This will print the data type of variable e

f = True    #This is a boolean value  , boolean values are case-sensitive in Python, so True and False are the only valid boolean values.
type_of_f = type(f) #This will return the data type of variable f, which is <class 'bool'>
print("The data type of variable f is:", type_of_f) #This will print the data type of variable f

g = False   #This is a boolean value
type_of_g = type(g) #This will return the data type of variable g, which is <class 'bool'>
print("The data type of variable g is:", type_of_g) #This will print the data type of variable g

h = None    #This is a special data type that represents the absence of a value or a null value. It is often used to indicate that a variable has no value assigned to it.
type_of_h = type(h) #This will return the data type of variable h, which is <class 'NoneType'>
print("The data type of variable h is:", type_of_h) #This will print the data type of variable h

i = ''      #This is an empty string/blank string, it is a string with no characters in it.
type_of_i = type(i) #This will return the data type of variable i, which is <class 'str'>
print("The data type of variable i is:", type_of_i) #This will print the data type of variable i

j = ""      #This is an empty string/blank string, it is a string with no characters in it.
type_of_j = type(j) #This will return the data type of variable j, which is <class 'str'>
print("The data type of variable j is:", type_of_j) #This will print the data type of variable j

k = " "     #This is a string with a single space character in it.
type_of_k = type(k) #This will return the data type of variable k, which is <class 'str'>
print("The data type of variable k is:", type_of_k) #This will print the data type of variable k

l = []      #This is an empty list, it is a list with no elements in it.
type_of_l = type(l) #This will return the data type of variable l, which is <class 'list'>
print("The data type of variable l is:", type_of_l) #This will print the data type of variable l

m = {}      #This is an empty dictionary, it is a dictionary with no key-value pairs in it.
type_of_m = type(m) #This will return the data type of variable m, which is <class 'dict'>
print("The data type of variable m is:", type_of_m) #This will print the data type of variable m



# ==========================================================================================
# Functions/Methods with Data Types:-
# ==========================================================================================

text = "Hello, World!" #This is a string
number = 10 #This is an integer

#FUNCTIONS:-

print(text) #This will print the string "Hello, World!" using the variable text
print(number) #This will print the integer 10 using the variable number

print(type(text)) #This will print the data type of variable text, which is <class 'str'>
print(type(number)) #This will print the data type of variable number, which is <class 'int'>

print(len(text)) #This will print the length of the string "Hello, World!" using the variable text. The len() function returns the number of characters in a string, including spaces and punctuation. OUTPUT: 13
# print(len(number)) #This will NOT print the length of the integer 10 as the len() function is not applicable to integers, and it will raise a TypeError. 

#METHODS:-

print(text.upper()) #This will print the string "HELLO, WORLD!" using the variable text. The upper() method converts all characters in a string to uppercase.
# print(number.upper()) #This will NOT print the string "hello, world!" using the variable text. The value 10 is an integer, and the upper() method is not applicable to integer class.

print(number.bit_length()) #This will print the number of bits required to represent the integer 10 in binary using the variable number. 
# The bit_length() method returns the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros. OUTPUT: 4

#print(text.bit_length()) #This will NOT print the bit length of the string "Hello, World!" as the bit_length() method is not applicable to strings, and it will raise an AttributeError.



age = 25 
height = 5.9
name = "kaustav"
student = True
y = None

print(age, height, name, student, y)
print(type(age), type(height), type(name), type(student), type(y))
print(len(name), len(str(age)), len(str(height)), len(str(student)), len(str(y))) #The len() function is applicable to strings, so we need to convert the other data types to strings using the str() function before applying the len() function.