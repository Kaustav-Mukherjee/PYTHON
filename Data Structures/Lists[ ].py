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
# ==========================================================================================






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
# ==========================================================================================







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
# ==========================================================================================








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
# ==========================================================================================










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
# ==========================================================================================










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
# ==========================================================================================










# ~ How to COPY Lists:

letters = ['a','b','c']
matrix = [
    ['a','b'],
    ['c','d']
]

# Now, if we try to copy, by assigning 'letters' to another varibale like this: xyz = letters it won't work, as the xyz variable doesn't make a copy of the variable, only makes a reference of the original list, but it only points to the same variable. Any modification done in xyz will directly modify the original variable. SO :

# Creating a Shallow Copy : Creating a copy of the oiginal list, independent of the original list, i.e, the modifications in the copied list won't affect the original list.

letters_copy = letters.copy()
letters_copy.append('z')
print('Original:', letters)
print('Copied:  ', letters_copy)

matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copied:  ', matrix_copy)
# Now, in this matrix, if we try to modify the values inside the separate lists, we'll be affecting both the original and the copied lists, because the function .copy() creates a shallow copy, which is only coopying the top level lists but not the values , inside it. Thus, we'll be using:
# DEEP COPY


# Creating a Deep Copy : Python has no built-in deep copy functions, so we have to import it.

import copy 
matrix = [
    ['a','b'],
    ['c','d']
]
matrix_copy = copy.deepcopy(matrix) #new_variable = library_name.function_name(variable_name)
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copied:  ', matrix_copy)

# There is also a copy function inside this copy library.

# list.copy() is only limited to lists, but copy.copy() is more generalized. THEREFORE IT IS ADVISED TO USE THE 'COPY' LIBRARY FOR DEEP AS WELL AS SHALLOW COPIES.


# Checking if Two Variables Refer to the Same Object.:
import copy


original = [
    ['a','b'],
    ['c','d']
]

    # Assignment
copy1 = original
print("Same Object?", original is copy1)

    # Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists?", original[0] is copy2[0])

    # Deep copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared Lists?", original[0] is copy3[0])
# ==========================================================================================










# ~ How to COMBINE Lists:

letters = ['a','b','c','d']
numbers = [1,2,3,4]
comb = letters + numbers # Combines both the lists into one list. Combination depends on thr order of the variables written.
print(comb)

comb1 = [letters,numbers] # Combines both the list separately into one big list.
print(comb1)

numbers.extend(letters) # Extends already existing list and adds the list into it. It doesn't create a new list
print(numbers)


comb3 = zip(letters,numbers) # It pairs the 2 lists up by taking 1st item from the 1st list and combining with the 1st item of the 2nd list, and so on. The outputs of this pairs will be inside parenthesis,(known as tuples). Therefor the output will be a list of tuples.
print(comb3) 
print(list(comb3))

# IMPORTANT : 1. If the lists are not of the same length, the remaining items in the original list will not be included in the output_list. 

letters = ['a','b','c']
numbers = [1,2,3,4]
comb4 = zip(letters,numbers) 
print(list(comb4))

# 2. Also the output of this will be shown as an Iterator like : <Zip object at 0X0000175E84E0> , which we'll convert into a list with the function list()

## We can also pair list, with a string value.
comb5 = list(zip(letters,numbers,'Hi'))
print(comb5)
# ==========================================================================================










# ~ How to Iterate through Lists (Iterators & Iterables): 

# All items/ data types we work in python is stored in Memory. This becomes a big issue if there is huge loads of data, which takes up a lot os space inside memory. But often we don't need this huge bulk of data all at once, we require subsets of it. Now for making this we use, Iterators.
# Iterators : These will not store anything in memory, it produces values 1 by 1 as long as we are asking for it.
# Why do we need iterators : 
# 1. For making Loops- For for loops we need iterators to go through items to execute a block of code to do spmething. 
# 2. To Save Memory. 
# 3. For Speed and Flexibilty. WE CAN BUILD Pipelines on the go without storing anything inside memory.

# 'Iterator' is thr e Process/Machine that is going to help us with the iteration, whereas 'Iterable' is the thing(anything that has a sequence of items) we can loop over, for example list, string values. But not Integers, Boolean values.

letters = ['a','b','c']

    # enumerate(): Takes any iterables and gives the Index(Position No.) and the Value. Output is an iterator thas have to convert to a list.

print(list(enumerate(letters))) 

print(list(enumerate(letters, start=1))) #We can also specify the index number to be start from showing at the output.

        #USAGE: Build a forloop . Helps to find the position of a data in a list.

for index, value in enumerate(letters):
    print(index, value)

    # reversed(): Returns an iterator that flips the data order

print(list(reversed(letters))) 

for l in reversed(letters):
    print(l)

    # zip(): Combines two or more sequences into pairs(tuples)

letters = ['a','b','c']
numbers = [1,2,3]
print(list(zip(letters,numbers)))

for l,n in zip(letters, numbers):
    print(l,n)

    # map(): Transforms data. map(function, Iterable)

letters = ['a','b','c']
print(list(map(str.upper,letters)))

numbers = ['1','2','3']
print(list(map(int,numbers)))

    # filter(): Similar to map function, it filters/cleans out data. filter(function, Iterable)

letters = ['a','b', '', None, 'c', False,0]
print(list(filter(None,letters))) #NONE : Removes Falsy values like : 0, '', False
print(list(filter(bool,letters))) #bool : Removes Falsy values like : 0, '', False (Same as None)

print(list(map(str.upper,(filter(bool,letters)))))

items = ['sql', '12345', 'rtyu', 'python', '98765']

print(list(filter(str.isalpha, items))) # isalpha : Keeps only letter(alphabetic) items

print(list(filter(str.isnumeric, items))) # isnumeric : Keeps only letter(numeric) items
# ==========================================================================================










# ~ LAMBDA FUNCTIONS: Building custom and quick logic

# lambda X : Expression , X is the input , In Expression we have to define what we want to do with the input

multiple = lambda x:x*2     # 'multiple; is a random variable name which stores a lambda function.

print(multiple(4))
print(multiple('a'))

add = lambda x,y: x + y

print(add(47,22))

check = lambda i: i in 'python'
print(check('z'))

prices = ['$12.50','$9.99','$100.00']
converter = lambda p: float(p.replace('$',''))
print(list(map(converter,prices)))
























