# ==========================================================================================
# Functions : A small, usable block of code that does one specific job.
# ==========================================================================================

## Sources of Functions:

#1. Built-In Functions: Predefined Functions already available within Python
#2. Standard Library Functions: Written by Python Team but to use it we have to import it. 
#3. External Library: Written by Community, Companies. Install, Import and work.
#4. User Defined Functions: Custom Functions written by a coder.

# USER - DEFINED FUNCTIONS:
# It has 2 parts -  Function definition and Function Call. 

# Function Definition -

# {
#     def function_name():
#         <line of code>    |
#         <line of code>    | - Body
#         <line of code>    |
# }

# Function Call - 
# {
#     function_name()
# }


# PARAMETERS AND ARGUMENTS:

    #Function Shapes:

# PARAMETERS: Names used in function definition that describe what data the function expects.
# ARGUMENTS: Actual values passed in a function call that are addigned to parameters.


# Function Definition -

# {
#     def function_name(PARAMETER):
#         <line of code>    |
#         <line of code>    | - Body
#         <line of code>    |
# }

# Function Call - 
# {
#     function_name(ARGUMENT)
# }



def clean_data():
    name = input('Enter your name: ')
    print(name.strip().lower())

clean_data() # In This code we haven't passed any parameters/ arguments.




def clean_name(name):
    print(name.strip().lower())

clean_name('   KaUStAV        ')
clean_name('   KaDGTHJHiab   ')

    # Parameters, Local & Global Variables :

    # GLOBAL VARIABLE: Any Variable which is created outside the function, and can be accessed Anywhere.
    # LOCAL VARIABLE : A variable created inside a function , which can be accessed Only Inside the function.


def clean_text(name): #name is the PARAMETER, it keeps the raw value, which will be resued.
    cleaned = name.strip().lower() #cleaned is the LOCAL VARIABLE which holds the procesed version.
    print('Raw:', name)
    print('Cleaned:', cleaned)

clean_text('   KaUStAV        ')  


# Scope-  Parameters and local variables can only be accessed inside the function. If we want to run it  outside the function it will throw an error. Like :
# print('Raw:', name)
# print('Cleaned:', cleaned)

# Traceback (most recent call last):
#   File "/home/kaustav-mukherjee/Documents/PYTHON/Ch_Functions/Functions.py", line 84, in <module>
#     print('Raw:', name)
#                   ^^^^
# NameError: name 'name' is not defined





# Let there be a rule in a company, where if the case rule is 'lower' then only we will make the texts lowercased.

case_rule = 'lower' # case_rule is the GLOBAL VARIABLE.

def clean_text(name): #name is the PARAMETER, it keeps the raw value, which will be resued.
    cleaned = name.strip() #cleaned is the LOCAL VARIABLE which holds the procesed version.
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    print('Raw:', name)
    print('Cleaned:', cleaned)

clean_text('   KaUStAV        ')  











    # POSITIONAL & KEYWORD ARGUMENTS:

def clean_name(first_name, last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print('first name is:', first)
    print('last name is:', last)
    print(full_name)

clean_name('   KaUStAV        ', '  MuKHeRJee') #No. of Arguments must match the number of parameters.



        # POSITIONAL ARGUMENTS : Values pass to the function, based on their Order.

def clean_name(first_name, last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print('first name is:', first)
    print('last name is:', last)
    print(full_name)

clean_name('   KaUStAV        ', '  MuKHeRJee') #Positional Argument. The ORDER of the Arguments MUST MATCH the order of the Parameters.



        # KEYWORD ARGUMENTS : Values pass to the function based on their Names.

def clean_name(first_name, last_name, country):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print('first name is:', first)
    print('last name is:', last)
    print(full_name,'from',country)

clean_name(country= 'India' ,last_name= 'MUKHERJEE', first_name='Shankha') #Keyword Argument. The order of the arguments doesn't matter .


## NOTE: Between 2 - 3 parameters Positional Arguments can be used. For more then 3, use keyword arguments.





    # MIXED ARGUMENT: Mixing positional and keyword arguments. # NOTE: In Mixed Arguments, we must start with Positional Arguments ,then Keyword Arguments.

clean_name('mARia', last_name= 'PUCHa', country='DE')
# clean_name(first_name='mARia','PUCHa', country='DE') #SyntaxError: positional argument follows keyword argument.




    # DEFAULT PARAMETER: Paramater that has already a value, so if we don't pass anything in Python uses that value automatically.

def clean_name(first_name, last_name, country='n/a'):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print('first name is:', first)
    print('last name is:', last)
    print(full_name,'from',country)

clean_name('Kumar','Suresh') #This won't show any error because we have already given a default value to the country in parameter.





# ~ *args & **kwargs : Allows functions to accept an UNKNOWN NUMBER of arguments

# In the previous codes we have mentioned the number of parameter(inputs) for our functions. But in some scenarios we don't know how many values we will pass through the function, It IS when *args and **kwargs are used.
































