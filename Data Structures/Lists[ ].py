# ==========================================================================================
# Lists : []: Ordered collection of items, which is very flexible. We can modify  like adding, changing , allowing duplicates.
# ==========================================================================================

# ~ Create Lists:

x = [] #Creating an empty list.
letters = ['a', 'b', 'c'] #Creating a list with strings.
numbers = [1,2,3,4,5,6,7,8,9,0] #Creating a list with numbers.
mixed = [1,'a', True, None] #Creating a list with various data types.
print(x)
print(type(x))
print(letters)
print(numbers)
print(type(letters))
print(type(numbers))
print(type(mixed))

# Python while creating a list, will create an object in the memory for the variable with an object type - 'LIST', then separate objects for each value, with object type of strings, integers,etc. depending on values, and here the eral values are stored.
# Now to connect those variable object and each string objects, python will interanaly create within the list an 'Array', which will be containing addresses reffereing to each of the string objects.

    # Creating lists with the built in function, list(): 

empty = list() #Creating an empty list.
print(empty)

letters = 'Python' #A basic string value.
letters = list('Python') #This takes the string value and separates it letter by letter into a list.
print(letters)

numbers = list(range(5)) #range() generates numbers from 0 to 4, list() converts them in a list.
print(numbers)

    # Nested Lists (Matrix) : 2 dimensional lists- Lists contained with other rows of lists, inside a list.

matrix = [['a','b','c'],
          ['d','e','f']]
print(matrix)

mixed_matrix = [['a','b','c'],
                [1,2,3],
                [True]]
print(mixed_matrix)
print(type(mixed_matrix))







# ~ How to Read & Access Lists:

lst = ['a','b','c', 'd']
print(lst) #This will access all the items, inside the list

#Now, if we want to access something specific inside the list, we use indexing:
# INDEXING: To access the item at last/first/something in the middle in the list, we need to have the position of the specific item within that list. Those number is the INDEX , it goes left to right (starting from 0) or from right to left (starting from -1)

lst = ['a','b','c', 'd']
print(lst[0]) #This will access the 1st item in the list.
print(lst[-1]) #This will access the last item in the list. Better to use negative numbers to access the last items in the list, instead of counting.

    #Accessing and Reading Matrix.

matrix = [['a','b','c'],    # Row 0 / Row -3
          ['d','e','f'],    # Row 1 / Row -2
          ['g','h','i']]    # Row 2 / Row -1

print(matrix)       # Prints the whole matrix as it is.
print(matrix[1])    # Prints the 2nd row of the matrix.
print(matrix[2][1]) # Prints the value at the 2nd position of the last row of the matrix.

 # Here the syntax is : list_name[row_number][Value_Position_number]

print(matrix[-1][-1]) # Prints the last item of the last row of the matrix.
print(matrix[0][0]) # Prints the first item of the first row of the matrix.

# SLICING: To access multiple items in a list.

print(lst[:2]) #Prints the 1st 2 characters from the list.
print(lst[1:3]) #Prints 2 characters from the list, skipping the 1st character.
print(lst[3:]) #Prints the characters starting from 3rd position upto the last.
print(lst[:]) #If we don't define anything here, it will print the list as it is.

print(matrix[:2]) #Prints the 1st 2 rows(lists) from the matrix.
print(matrix[1:]) #Prints the last 2 rows(lists) from the matrix.

print(matrix[2][:2]) #Prints the 1st 2 values from the last row(list) in the matrix.







# ~ How to UNPACK Lists: Taking items out of a list and putting it in different variables.

person = ['Maria', 29, 'Data Engineer', 'Spain'] 

    # name = person[0]
    # age = person[1]
    # role = person[2]
    # country = person[3]

    #Now only using Indexes will make our code long and hard to extend. Thus:

name, age, role, country = person #Order of the values in the list, must match the order of the variables here.

print(name)
print(country)
print(role)
print(age)

## ** SPECIAL USAGE OF LISTS,: IF WE WANT TO ONLY HAVE THE FIRST AND LAST ITEM IN A LIST, AND ALL THE REST OF IT MUST BE INSIDE ONE SINGLE VARIBALE, THEN:

name, *details , country = person #This ASTERISK * will mark all the list in the middle into one variable.

print(name)
print(country)
print(details)

name, *details = person #THIS WILL ASSIGN THE NAME AS TE FIRST VARIABLE AND EVERYTHING ELSE IN ANOTHER VARIABLE.
print(name)
print(details)

*details, country = person #THIS WILL ASSIGN THE COUNTRY AS TE LAST VARIABLE AND EVERYTHING ELSE IN ANOTHER VARIABLE.
print(details)
print(country)

## Skipping items using Underscore '_' : This helps in skipping the items we don't want, thereby reducing the need for more variables and also reducing Storage.

name, _, role, _ = person
print(name)
print(role)

name, *_, country = person ## This will group the rest of the variables and will just skip it.








# ~ How to EXPLORE & ANALYZE Lists:

numbers = [1,5,2,3,4,8,0,7,6]
list1 = [1,2,3,4]
list2 = [5,2,3,4]

print('Max: ', max(numbers)) # Prints the MAX VALUE IN THE LIST.

print('Min: ', min(numbers)) # Prints the MIN VALUE IN THE LIST.

print('Sum: ', sum(numbers)) # Prints the SUMMATION OF ALL THE VALUES IN THE LIST.

print('Length: ', len(numbers)) # Prints the LENGTH OF THE STRING(NO. OF ITEMS IN THE LIST).

print('All: ', all(numbers)) # Prints the boolean for all the values in a list. Returns TRUE IF ALL VALUES ARE TRUE. It considers 0 as missing value.

print('Any: ', any(numbers)) # Prints TRUE even if there is only 1 true value



print('Count: ', numbers.count(5)) # Prints the NO. OF TIMES AN ITEM HAS APPEARED IN A LIST.

print('Index: ', numbers.index(5)) # Prints the POSITION OF THE FIRST OCCURANCE OF A VALUE.



print(4 in numbers) # CHECKS AND PRINTS WETHER A VALUE IS PRESENT IN A LIST.
print(9 not in numbers) # CHECKS AND PRINTS WETHER A VALUE IS NOT PRESENT IN A LIST.

print(list1 == list2) # COMPARES WETHER 2 LISTS HAVE SAME VALUES.
print(list1 < list2) # COMPARES THE FIRST VALUE OF THE 2 LISTS, IF THEY ARE EQUAL, THEN THEY MOVE TO THE NEXT ELEMENT
print(list1 is list2) # CHECKS WETHER THE MEMORY ADRESS OF THE LISTS. 










# ~ How to CHANGE (UPDATING, INSERTING, REMOVING ITEMS) Lists:

letters = ['a','b','c']

matrix = [['a','b','c'],    # Row 0 / Row -3
          ['d','e','f'],    # Row 1 / Row -2
          ['g','h','i']]    # Row 2 / Row -1

    ## ADDING NEW ITEMS:

letters.append('x')     # Appends the new value at the end of the list.
print(letters) 

letters.insert(0,'1') # Inserting new values at a specific position. .insert(index_no., new_value)
print(letters) 

matrix.append(['x','y','z']) # Appends the new list at the end of the matrix.
print(matrix) 

matrix.insert(0, ['x','y','z']) # Inserting new list at a specific position. .insert(row_no., new_value)
print(matrix) 

matrix[1].append('x')  #Appends the new value at the end of the specific list inside the maytix.
print(matrix) 

matrix[1].insert(0,'q')  #Inserts the new value at the specific position of the specific list inside the matix.
print(matrix) 




    ## REMOVING ITEMS:

letters.remove('c') # Deletes an item from the list based on its value. Only removes the 1st match.
print(letters) 

letters.pop(1) # Removes and returns an item based on it's position. IF WE DON'T MENTION POSITION NO, INSIDE POP, By default it will remove the last value in the list.
print(letters) 

removed = letters.pop(1) # By this we can find out the items removed.
print(letters) 
print('Removed Item:', removed)

letters.clear()     # Removes Everything from the list and makes it an empty list
print(letters) 

matrix.remove(['x','y','z']) # Deletes a list from the matrix based on its value. Only removes the 1st match.
print(matrix) 

matrix.pop() # Removes and returns a list based on it's position.
print(matrix) 

matrix[1].remove('e') # Removes the specific value from the specific list in the matrix.
print(matrix) 

matrix[-1].pop(0) # Removes the value from the specific position from the specific list in the matrix.
print(matrix) 



letters = ['a','b','c']

matrix = [['a','b','c'],    # Row 0 / Row -3
          ['d','e','f'],    # Row 1 / Row -2
          ['g','h','i']]    # Row 2 / Row -1


    ## UPDATING ITEMS:

letters[0] = 'x' # Updates the letter at 0 position to 'x'.
print(letters) 

matrix[-1] = ['x','y','z'] # Updates list for a certain row in a matrix
print(matrix) 

matrix[0][0] = '-' # Updates the value at the speified position of the specified row in a matrix.
print(matrix) 










# ~ How to ORDER / SORT Lists:

letters = ['c', 'a', 'b']
matrix = [['a','b','c'],    # Row 0 / Row -3
          ['d','e','f'],    # Row 1 / Row -2
          ['g','h','i']]    # Row 2 / Row -1


letters.sort() #Default sorting : ASCENDING
print(letters)

letters.sort(reverse= True) #DESCENDING
print(letters)

matrix.sort(reverse=True) # Sorts based on the first element of each list.  If first items are same, thn moves to the 2nd elements
print(matrix) 

matrix[1].sort(reverse=True) # Sorts the items of a specific list inside a matrix.
print(matrix)

new_letters = sorted(letters) # Sorts the items in a list but doen't change the original list.
print(letters)
print(new_letters)

new_letters = sorted(letters, reverse=True) # Sorts the items in a list but doen't change the original list.
print(letters)
print(new_letters)

letters = ['c', 'a', 'b']

letters.reverse() #F lips the list around.
print(letters)

new_list = list(reversed(letters)) # Flips the list around without changing the original list
print(letters)
print(new_list)










# ~ How to COPY Lists:

letters = ['a','b','c']


















