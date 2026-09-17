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




# ~ How to UNPACK Lists:
















































