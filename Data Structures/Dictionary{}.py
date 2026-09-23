# ==========================================================================================
# DICT(Dictionary) : {}: Collection of Multiple & Related Information. Let's us store Data in Key - Value Pairs, where Keys are the description of the data and the Values are the actual data.
# ==========================================================================================

user = {'id': 1, 'age': 30, 'city': 'howrah'}

# ~ How to Access Dictionary:

print(user['city'])

    #Now, if a KEY is not there in the dictionary, Python throws a KeyError. Therefore how to access:

print(user.get('name')) #If there is a missing key, the default value is 'None'. But if we want to pass a custom value if there is a missing key:
print(user.get('name', 'unknown'))

# ~ Testing if a key exits in the dictionary-

print('age' in user)
print('name' not in user)

# ~ Viewing Objects in the dictionary-

print(user.keys()) # Gives us a live view of the dictionary's keys
print(user.values()) # Gives us a live view of the dictionary's values
print(user.items()) # Gives us a live view of the dictionary's key-value pairs. Output is in a list, which helps in looping, transforming data, building new dicts, comparing and more.

for key,value in user.items():
    print(key,value)


# ~ How to Modify(Add, Remove, Update) in the dictionary-

user['name'] = 'Kausty' #Adding key values in dictionary.
print(user)

user['age'] = 35  #Assign/updates values of already existing keys

user.update({'age':40, 'city':'Paris'}) # Adds new eys and updates existing ones using another dictionary
print(user)

user.pop('age') #Unlike in lists, .pop() must have an argument inside
print(user)

user.popitem() # Retruns and deletes the most recent key value pair from the dictioanry.
print(user)

# ~ Creation:

user1 = {
    'id': None,
    'name': None,
    'age': None,
    'city': None
    }

user1 = dict.fromkeys(['id','name','age','city'], None) #Build a new dictionary where all keys get the same default value. It replaces the code for user1 we have written just above it.
print(user1)


## DICTIONARY COMPREHENSIONS:

# Challenge: Keep Only String Values & Convert Them to UPPERCASE
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

user_str = {
    k: v.upper() #Expression
    for k, v in user.items() #Loop
    if isinstance(v, str) #Filter
}

print(user_str)

