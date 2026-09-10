# ==========================================================================================
# Conditional Statements: Checkpoints that checks a condition.

# TRUE- Runs the code.
# FALSE- Skips the code.

# IF - Starts the 1st Condition.
# ELIF - Adds a follow up cndition if the previous fails.
# ElLSE - 'fallback' if none of the conditions are met. 
# ==========================================================================================

# ~ Standalone IF:
    # IF statement : Defines the first condition

score = 100
if score >= 90:
    print("A")

# ~ Two Way Decision:
    # Else statement: Runs only if all previous conditions are false.

score = 50
if score >= 90:
    print("A")
else:
    print("F")

# ~ Multi Condition statements:
    # Elif statement: Asks a follow-up question only runs if previous conditions were false

score = 81
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")


score = 81
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# ~ Nested If statement: If statemnt, inside another If
score = 90
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# ~ Connecting Conditions

score = 90
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



# ~ Independent Ifs : Each if is checked separately, All conditions are checked even if one is already true.
score = 90
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Projet is Submitted")
else:
    print("Project not Submitted")


# ~ Ternary Operator (Inline If) Instead of writing If Else in multiple lines, we write ths in a single line, applicable for simple logic.
    ##THE OUTPUT OF THIS INLINE IF, CAN BE STORED IN A VARIABLE

score = 90
print("A" if score >= 90 else "F")

grade = "A" if score>=90 else "B" if score>= 80 else "F"
print(grade)


# ~ Match Case: Evaluate a value against multiple values, Runs the code of the first match.

country = input('Enter your Country name: ')

    #1st Method, classical way of writing conditional statement:
if country == 'United States':
    print('US')
elif country == 'India':
    print('IN')
elif country == 'Egypt':
    print('EG')
elif country == 'Germany':
    print('DE')
else:
    print('Unknown Country')

    #2nd Method, Using MATCH CSE: Can be used only for matching values
match country:
    case 'United States' | 'USA': #We can use '|' to match multiple values in a single case.
        print('US')
    case 'India':
        print('IN')
    case 'Egypt':
        print('EG')
    case 'Germany':
        print('DE')
    case _:                            #This signifies Default case which is the ELSE statement in IF ELSE.
        print('Unknown Country')
