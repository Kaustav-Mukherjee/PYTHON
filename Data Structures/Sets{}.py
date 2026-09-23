# ==========================================================================================
# Sets : {}: Unordered collection of unique items.
# ==========================================================================================

a = {10,20,30,40}

a.add(50) #Adds a value in the set.
print(a)


a.update('Hi') # Merges another group of values(Iterables) into the set.
a.update({1,2})
print(a)

#We can use Math Operators as Quick Shortcuts: | & - ^

a |= {4,5} #This Operator acts like UPDATE
print(a)

a.discard(10) #Works like REMOVE, but if there is a value given to remove but it is not inside the set, it won't break the code, unlike REMOVE. 

print(a)


# MATHEMATICAL OPERATIONS ON SETS::

a = {10,20,30,40}
b = {30,40,50,60}

## NOTE: Math operators return a new set and leave the original sets untouched.

    # union(): Combines ALL UNIQUE items from BOTH SETS.

print(a.union(b))
print(a | b) # Works same as union()

    #intersection(): Returns only the shared / same / overlapping items between 2 sets

print(a.intersection(b))
print(a & b) # Works same as intersection()

    # difference(): Only the items in the first set, which is not present in another set.

print(a.difference(b)) # Returns items in A which are not in B.
print(a - b) # Works the same as difference()
print(b - a) # Returns items in B, which are not in A.

    # symmetric_difference(): Only Returns the items not shared by the sets.

print(a.symmetric_difference(b))
print(a ^ b) # Works same as symmetric_difference()





# RELATIONSHIPS BETWEEN TWO SETS:
a = {30,40}
b = {30,40,50,60}

print(a.issubset(b)) # Returns TRUE if ALL items in this set exists in the other.
print(b.issuperset(a)) # Returns TRUE when it includes ALL items of the other set.
print(a.isdisjoint(b)) # Returns TRUE if both sets share no items(No Overlapping)


