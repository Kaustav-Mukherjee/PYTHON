# Data Structures can be categorized by 4 Chracteristics: 1.Ordered, 2.Allow Duplicates, 3.Indexed 4.Mutable.


# ~ For Lists:

my_list = [10,20,30]

    #1. Ordered : Python remembers the exact position of every value we give. The order/ position of the value we've given will not change unless we change it. Lists are ordered.

print(my_list) # At output we can see that the values 10, 20, 30 are printed exactly as we have defined.

    #2. Duplicates : We can store a same value more than once. Lists Allows Duplicates.

my_list1 = [10,20,30,20]
print(my_list1)

    #3. Indexed : We can access the value of anylist, by having the position/index number. Lists are Indexed

print(my_list[1])

    #4. Mutable : Changing/ Modifying the values. Lists are Mutable.

my_list[2] = 40
print(my_list)


#Lists can be very risky, as lists are mutable, and it can be changed. Thus for security reasons we use Tuples.


# ~ For Tuples:

my_tuple = (10,20,30)

    #1. Ordered : Tuples are Ordered.
print(my_tuple) # At output we can see that the values 10, 20, 30 are printed exactly as we have defined.

    #2. Duplicates : Tuples Allows Duplicates.

my_tuple1 = (10,20,30,20)
print(my_list1)

    #3. Indexed : Tuples are Indexed

print(my_tuple[1])

    #4. Mutable : Tuples are Non - Mutable.

my_tuple[2] = 40
print(my_tuple)


# ~ For Sets:

my_set = {10,30,20}

    #1. Ordered : Sets are Unordered.
print(my_set) # At output we can see that the values 10, 30, 20 are not printed exactly as we have defined.

    #2. Duplicates : Sets Doesn't Allow Duplicates.

my_set1= {10,20,30,20}
print(my_set1)

    #3. Indexed : Sets are Not-Indexed.

print(my_set[1])

    #4. Mutable : Sets are Mutable.

my_set.remove(20)
print(my_set)








# ~ For Dictionaries:


my_dict = {
    'a': 10,
    'b': 20,
    'c': 30
}

    #1. Ordered : Dictionaries are Ordered.

print(my_dict) # At output we can see that the values 10, 20, 30 are printed exactly as we have defined.

    #2. Duplicates : Dictionaries Does Not Allow Duplicates for KEYS, but allows duplicates for values.

my_dict1 = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a': 40
}
print(my_dict1)

    #3. Indexed : Dictionaries are not Indexed.

print(my_dict[1]) 
#We cannot access values through Index in Dictionaries, We can access the values by using their Keys.
print(my_dict['b']) 

    #4. Mutable : Dictionaries are Mutable.

my_dict['c'] = 40
print(my_dict)



