# ==========================================================================================
# Loops : Controlling the flow of code. Repeating a block of code over and over until a condition is met.

# ==========================================================================================

# ~ For Loop: Go through a group of items one by one to do something for each item.

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