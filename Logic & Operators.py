# ==========================================================================================
# Control Flow : It is the logic we write to control how our code runs.
#
# ~ Instructs python should a part of the code is run, skipped or repeated.

# One of the methods of controlling this flow of code by writing Conditional Statements.

    #Conditional Statements: Let's say we are writing our code as normal, and then we come to a point, having 2 blocks of code, but don't want to execute both of them, but want to execute one of the codes, based on the question. Therefore the question we're building inside is the condition, and based on the answer, if the answer is TRUE then we execute one block of the code, but if the answer is FALSE, then we execute the other block of the code.

# The other method of controlling this flow of code by writing Loops.

    #Loops: Instead of repeating the same tasks again and again, we can go and build a loop to execute the code multiple times. Whenever the condition is TRUE, the loop is executed again and again, but when it is FALSE, the code exists the loop condition to execute the rest of the code.

# ==========================================================================================


## Control Flow Statements: Special Instructions in Python to Change the Flow.
    # Condtional Statements - if, else, elif (Helps in making decisions)
    # Loops: for, while (Helps in repeating tasks) also with statements like: break, pass, continue.
    # Boolean Expressions: Build questions(conditions) Python can evaluate as "Yes" or "No" (True or False)
        #a. Values - True, False
        #b. Functions - bool(), any(), all(), isinstance()
        #c. Operators - Comparison Operators (==, !=, <, >, >=, <=), Logical Operators (and, or, not), Membership Operators (in, not in), Identity Operators (is, is not).


# Boolean Expressions:
print(True)
print(False)

    # ~bool(): "TRUE" if the value is non-empty or non zero, "False" if the value is empty or zero.

print(bool(123)) #OUTPUT: TRUE
print(bool("HI")) #OUTPUT: TRUE

print(bool()) #OUTPUT: FALSE
print(bool(0)) #OUTPUT: FALSE Though 0 is a value, but in boolean function it is considered as nothing.
print(bool("")) #OUTPUT: FALSE
print(bool(None)) #OUTPUT: FALSE


    # ~ all(), any(): Helps to evaluate values, more than one.
        # any(): Returns TRUE if atleast one value is TRUE.
        # all(): Returns TRUE if all values are TRUE.

email = input("Enter email: ")
phone = input("Enter phone_no: ")
username = input("Enter username: ")
        #Now the codition is like this, that in a website if any one of the above fields are filled, it allows registration.
print(any([email, phone, username])) # OUTPUT will be TRUE if ANY ONE of the above fields are filled.

        #Now the codition is like this, that in a website ionly if all the above fields are filled, it allows registration.
print(all([email, phone, username])) # OUTPUT will be TRUE if ALL of the above fields are filled.

    # ~ isinstance(): CHecks if a value belongs to a certain data type.
print(isinstance(123, str))
print(isinstance(True, str))

print("Hello".endswith("o"))

    # Comparison operators: It compares two values and return True or False based on the result.
    # == Equal to
    # != Not Equal
    # < Less than
    # > Greater than
    # <= Less than or Equal
    # >= Greater than or Equal

print(10 == 10)
print(10 != 10)
print(7 > 3)
print(7 >= 3)
print(3 < 7)
print(3 <= 7)
print(1 < 4 < 6) # Python executes chain operation here, checking each condition one by one from left to right.

        ## Comparison operators cn also be used to compare strings, 
print("a"== "a")
print("a" == "A")
print("a" < "b")

    # Logical operators: Used to combine multiple boolean expressions.
    # and, or, not

        #~ and : Python returns TRUE only if all the coditions are TRUE.
        #~ or : Python returns TRUE only if one of the coditions is TRUE.
        #~ not : It reverses the truth, turns TRUE into False and vice versa

print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 < 1)
print(3 > 1 or 5 > 1)
print(3 < 1 and 5 < 1)

print(not 3 > 2)
print(not True)
print(not False)

name = ""
print(not name)
print(not 0)

        ## Mixing the conditions:

            # ~ ORDER OF OPERATION: Controlling the execution order
            # "and" operator has higher priority than "or" operator.
            # Paranthesis () has higher priority over and, or.

# Allow access only if the user is logged in or they are guest but they must not be banned.

is_logged_in = True
is_guest = False
is_banned = False

print((is_logged_in or is_guest) and not is_banned)

is_logged_in = True
is_guest = False
is_banned = False

print((is_logged_in or is_guest) and not is_banned)

    # Membership operators: Used to combine multiple boolean expressions.
     #~ in : Checks if a value inside another value, like a string, tuple or other sequence.

print("o" in "Python")
print("f" not in "Python")
print(3 in[1,2,3])

    # Identity operators: Checks if two variables refer to the same object in the memory.

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y) #This is just comparing the values of x and y. OUTPUT: TRUE
print(x is y) #This will return FALSE, since python isn't comparing the values of the variables, it is comparing the separate ID's of the separate objectscreated for x and y.


x = 10
y = 10

print(x == y) #This is just comparing the values of x and y. OUTPUT: TRUE
print(x is y) #In this case, as the value is very simple python is not going to create separate ID's for x and y. It will create the same id. OUTPUT: TRUE

x = ['a', 'b', 'c']
y = x

print(x == y) #This is just comparing the values of x and y. OUTPUT: TRUE
print(x is y) #This will return TRUE as y is assigned the value of x and it is the same object 