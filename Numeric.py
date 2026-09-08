# ==========================================================================================
# Numerics
#
# ~ Consists of integers, float numbers and complex numbers.
# ==========================================================================================

#Types:

x = 3 # An Integer
y = 5.7 # A float Number
z = 2 + 3j # A complex no.
a = "24" # A string.

print(type(x))
print(type(y))
print(type(z))

print (x * 3) # Output: 9
print (y * 3) # Output: 17.1
print (z * 3) # Output: (6+9j)
print (a * 3) # Output: 242424, because the value is a string, the value gets repeated here 43 times, instead of multiplying 24 by 3.

a = int(a) # Converts the string value into the integer value here
print(type(a))
print (a * 3) # Performs multiplication on the converted integer value.

x = float(x) #Converts the integer value into a float value.
print(type(x))

b = 4 #Consider this as a real number
c = 5 #Will be consdering this as an imaginary number
print(complex(b,c)) #OUTPUT: (4+5j)


# Math Operators :

print(2 + 3) # Performs addition
print(5 - 3) # Performs Substraction
print(5 * 3) # Performs Multiplcation
print(7 / 2) # Performs Division
print(7 // 2) # Performs Floor Division : It divides two numbers and rounds down.
print(7 % 2) # Performs division and returns us the remainder: The leftover part after division, used to check if a number is even.
print (2 ** 3) # Performs Exponentiation: It raises number to the power of another number.

    #Variable Shortcuts:
x = 2
# x = x + 3 Instead of writing like this , we can also do:
x += 3 # Adds x by 3 and assigns it to x .
print(x) 
x -= 1
print(x) # Subtracts x by 1 and assigns it to x.
x *= 2 # Multiplies x by 2 and assigns it to x.
print(x)


# Rounding :

print(abs(2 - 10)) #abs(): Returns the absolute (non- negative) value of a number #Useful for measuring distance, size regardless of direction.

price = 35.5467890
print(round(price)) #round(): Returns the number which is rounded up to the nearest whole number, up or down regarding on what's closer. Used in data analysis to read numbers better.
print(round(price,2)) #Rounds upto the 2nd decimal number.

import math
new_price = 35.5467890
print(math.floor(new_price)) # floor(): Rounds down to the nearest integer.

print(math.ceil(new_price)) # ceil(): Same as that of round() but doesn't give the option to round upto how many places after decimals. Used in data engineering, in splitting data into pages or batches.

print(math.trunc(new_price)) # trunc(): Cuts off the decimal part and keeps the whole number (no rounding).

        # Now like the trunc() function, the same operation can be done through int(). So, if we haven't imported the 'math' in python we'll use int() function.
        # Else if we have already imported 'math' then we use trunc()

print(int(price) == math.trunc(new_price)) #OUTPUT : TRUE.

## SKIPPING sqrt(), sin(), cos(), log() functions.

# Random:

import random
print(random.random()) #Returns a random float number between 0.0 and 1.0. Used to generate and test dummy datas.

print(random.randint(1,6)) #Returns a random whole number between start to end, including both. Used to generate and test dummy datas.

# Validation:

x = 7.0
y = 7.5
print(x.is_integer()) # is_integer(): Checks if a float has no decimal part.
print(y.is_integer())

a = 70
print(isinstance(a, int)) # isinstance(): Checks if a value belongs to a certain data type.
print(isinstance(a, str))