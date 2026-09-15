# ==========================================================================================
# Loops : Controlling the flow of code. Repeating a block of code over and over until a condition is met.

# ==========================================================================================


# ==========================================================================================
# ~ For Loop: Go through a group of items one by one to do something for each item.
# ==========================================================================================


for i in (1,2,3,4,5):
    print(f"Round: {i}")


items = (1,2,3,4,5) #Instead of writing the sequence in the for loop we can assign it to a variable and then mention the variable in the loop. Also we are using tuples as a sequence
for item in items: #Use the singular name as the variable name and the plural for the sequence name.
    print(f"Round: {item}")

        ## Sequences to use in a For loop: -tuples, -list, -strings, -range. We can also add files, dictionaries, etc. Anythinh which is iterable we can add as a sequence.

items = [1,2,3,4,5] #Using Lists as a squence
for item in items: 
    print(f"Round: {item}")

items = [1,2,3,4,5,'HI'] 
for item in items: 
    print(f"Round: {item}")


items = 'Python' #Since strings are a sequence of letters, each letter has its own value.
for item in items: 
    print(f"Round: {item}")

items = ' Python' #Since strings are a sequence of letters, each letter has its own value.
for item in items: 
    print(f"Round: {item}")


for item in range(5):  #Using RANGE as a sequence The number 5 here is the stopping number. It stops after printing from 0 to 4.
    print(f"Round: {item}")

for item in range(1,5):  #Using RANGE as a sequence The number1 is the starting number (Default starting number is 0) and 5 here is the stopping number. It stops after printing from 1 to 4. The stop number wont be included.
    print(f"Round: {item}")

for item in range(1, 10, 2):  #the number 2 is the incremental nu./ stops.
    print(f"Round: {item}")


#Usage of for loops in going through values and aggregating data like summing, counting or averaging.:

scores =[80, 50, 60, 75]
total = 0
for score in scores:
    total = total + score
    print('Current total: ',total)
print('Final total: ', total)

#Usage in transforming data like cleaning data before processing
files = [' Report.csv ', 'DATA.csv ', ' final.TXT '] #Problems: Inconsistent casing and unnecessary spaces
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print('Processing File:',file)

# Loop Control Statements: ~break, ~continue, ~pass

# ~ BREAK statement: It stops the loop immediately. It jumps out and ends the code rightaway.

names = ['john', 'maria', '', 'kausty']
for name in names:
    if name == '':
        print('Empty Value detected!')
        break
    print(f'Name = {name}')


# ~ CONTINUE Statement: It skips one loop cycle without stopping the loop. Skips the current round and goes to the next.

names = ['john', 'maria', '', 'kausty']
for name in names:
    if name == '':
        print('Empty Value detected!')
        continue
    print(f'Name = {name}')


# ~ PASS Statement: It is a placeholder, where nothing happens. 

names = ['john', 'maria', '', 'kausty']
for name in names:
    if name == '':
        pass #This is to check and replace the value for later.
    print(f'Name = {name}')

    #LATER:
names = ['john', 'maria', '', 'kausty']
for name in names:
    if name == '':
        name = name.replace('','unknown')
    print(f'Name = {name}')

# ~ ELSE Statement: Runs a block of code  only if the for loop finishes naturally. Loop completed without breaks.

items = [1,3,4,7]
for i in items:
    print(i)
else: #UNDER NORMAL CONDITIONS THIS ELSE STATEMENT IS COMPLETETLY USELESS. IF WE JUST GIVE THE PRINT STATEMENT PYTHON WILL RUN IT AS SAME AS GIVING THE ELSE STATEMENT.
    print('Loop is completed.')

    #This ELSE statement only has its value when there's a 'break'.

    ## ELSE + BREAK:

items = [1,3,4,7]
for i in items:
    if i % 2 == 0:
        print('Even no. found: ', i)
        break
else: 
    print('All numbers are ODD.')


# Nested Loops: Loop inside another loop! Used for crossing and combine data(Data Pairing), Navigating Hierarchy

for x in range(4): #Outer Loop
    for y in range(3): # Inner Loop
        print(f'({x},{y})')

## DATA PAIRING:

colors = ['red', 'green', 'blue', 'magenta']
sizes = ['XXL', 'XL', 'L', 'M', 'S', 'XS', 'XXS']

for color in colors:
    for size in sizes:
        print(f'{color} - Size: {size}')



## NAVIGATE HIERARCHY:

years = [2026, 2027]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
days = range(1,29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')



# ==========================================================================================
# ~ WHILE Loop: Repeats a block of code- over and over as long as condtition is True.
# ==========================================================================================

# ==========================================================================================
# Brief difference between for loops vs. while loops:
#     In for loops, as long we have values from the iterator(sequence), the program keeps looping. There are 2 issues in it:
#         1. We are always predefining the sequence. We know how many times the program will iterate.
#         2. The condition is always predefined from python, and we cannot change it.
#     But for While loops, we can define the condition for the iteration, and as long as it is true we're gonna keep looping and iterating.
# ==========================================================================================

# ==========================================================================================
# 2 categories of while loops:
    # . WHILE CONDITION: We define the cond. and loop will keep gping until the condition becomes False.
    # . WHILE TRUE: The loop is going to run forever, thus we add a break statement in order to force the loop to stop.
# ==========================================================================================


# ~ WHILE Condition:

i = 1                    #INITIALIZATION
while i <= 5:            #CONDITION
    print(i)
    i += 1               #UPDATE


# Write a program that keeps asking "Do you agree" until the user types "Yes"
answer = "" 
while answer != 'Yes':
    answer = input("Do you agree? (Yes/No): ")
print('Thank You')

# ~ WHILE TRUE:

while True:
    answer = input("Do you agree? (Yes/No): ")
    if answer == 'Yes':
        break
print('Thank You')


# ==========================================================================================
#               WHILE Condition                   |               WHILE True               
# ------------------------------------------------|------------------------------------------    
#                                                 |
# 1. Exists Normally , when condition = FALSE     | 1. Must have extra IF and BREAK statements
# 2. Safer and more Readable                      | 2. Risk of infinite loop, but more Flexible
# 3. Used to make Counter, Limited Retries or     | 3. Used in Open Ended scenarios, like a trigger,
# Validating inputs from customers                | if we are trying to connect to a database, stream, api, etc.
# ==========================================================================================

# ==========================================================================================
#               FOR Loop                          |               WHILE Loop               
# ------------------------------------------------|------------------------------------------    
#                                                 |
# 1. Loops over a fixed sequence, where python    | 1. Loops while the condition given is TRUE
# creates an object code iterator.                | 
# 2. For loops require predefined conditions.     | 2. We can add our own conditions for the iterations.
# 3. For loops are used when we know for how many | 3. While Loops are used when we don't know the no. of 
#  times the loop will run. Also for Processing   | iterations we need, we're waiting for a trigger/condition.
#  Data.                                          |
# 4. Advantages: Safe, Simple, Clear.             | 4. Advantages: Advanced, Flexible, Dynamic.
# 5. Limited Flexibility.                         | 5. Complex, High Rish of builing infinite loops.
# ==========================================================================================




