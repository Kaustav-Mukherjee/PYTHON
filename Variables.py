# ==========================================================================================
# Variables:
#
# ~ A Variable is a name we create to store a value in memory, So we can use it later in the program.
# ~ Makes program dynamic.
# ~ Reusable, Updatable anytime.``
# ==========================================================================================

x = 10 #This is a variable assignment
print(x) #This will print the value of x

x=20 #This is a variable reassignment
print(x) #This will print the new value of x 

y = x + 5 #This is a variable assignment with an expression
print(y) #This will print the value of y

# OUTPUT:
# 10 
# 20
# 25

print("My name is Kaustav") #This will print the string "My name is Kaustav"
print("Kaustav is learning Python") #This will print the string "Kaustav is learning Python"
print("Kaustav is learning Python and he is enjoying it") #This will print the string "Kaustav is learning Python and he is enjoying it"

name = "Kaustav" #This is a variable assignment
print("My name is", name) #This will print the string "My name is Kaustav" using the variable name. The comma (,) is used to concatenate the string and the variable. It will automatically add a space between them.   
print(name, "is learning Python") #This will print the string "Kaustav is learning Python" using the variable name
print(name, "is learning Python and he is enjoying it") #This will print the string "Kaustav is learning Python and he is enjoying it"

#Therefore, Variables make it easier to store and reuse values in a program, making the code more readable and maintainable. Also making updates supereasy.

name = "Shankha" #This is a variable reassignment
#Now, we have assigned a new value to the variable name. So, now it will store the value "Shankha" instead of "Kaustav". But in the previous print statements will print Kaustav, because they are executed before the value reassignement, and Python executes the code line by line.
language = "Python" #This is a variable assignment
print("My name is", name, "and I am learning", language) #This will print the string "My name is Shankha and I am learning Python" using the variables name and language. The comma (,) is used to concatenate the strings and the variables. It will automatically add a space between them.


value = "datawithbarra.com"
print ('info@' + value) #The plus (+) operator is used to concatenate the string "info@" and the variable value. It will not add a space between them. OUTPUT: info@datawithbarra.com
print ('support@' + value)
print ('www.' + value)

# ==========================================================================================
# INPUT():-
#
# ~ Built-in Python function that allows the user to provide input to the program during its execution.
#
# ==========================================================================================

name = input("Please enter your name: ") #This will prompt the user to enter their name and store it in the variable name
print("Hello, ", name + "!") #This will print a personalized greeting


# ==========================================================================================
#Hard- coded Vs. Dynamic Values:
# Hard-coded values are fixed and cannot be changed during the execution of the program. They are directly written into the code. 
# Dynamic values, on the other hand, can change during the execution of the program. They are usually obtained from user input or other sources. 
# ==========================================================================================


name = input("Please enter your name: ") #This is a Dynamic value, as it is obtained from user input. It can vary each time the program is run, depending on what the user enters.
country = 'India' #This is a Hard-coded value.
print("Hello, ", name, "from", country+ "!")