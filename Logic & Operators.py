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


