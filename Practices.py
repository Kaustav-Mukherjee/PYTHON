x = "A"
print(x) #This will print the value of x    
# # #Ask for a value
y = input("Enter a value: ") #This will prompt the user to enter a value for y and store it in the variable y
print(y) #This will print the value of y
print(x+y) #This will print the concatenation of x and y


# # Turn the messy string into a single, clean summary with name, role and age.
# # "968-Maria, ( D@t@ Engineer ) ;; 27y " to name: maria | role: data engineer | age: 27

messy = "968-Maria, ( D@t@ Engineer ) ;; 27y ".lower().strip().strip("968-").replace(")","").replace("(","").replace("@","a").replace("y","").replace(";","").replace(",","")
name = messy[0:5]
role = messy[6:20]
age = messy[22:]

print('name: '+ name +' '+'|'+' role: '+ role + ' ' + '|' + ' age: '+ age)


# Generate a random integer between 1 and 100, and check if the result is an even number.

import random
x = random.randint(1,100)
print(isinstance(x,int))


# Check if a users name is not empty and the age is grater than or equal to 18
# Check if the password is at least 8 characters long and does not contain spaces
# Check if a user's email is not empty, contains '@', and ends with a '.com'
# Check if a username is a string, is not None, and is longer than 5 characters
# Check if the user is either an admin or a moderator, and either they're not banned or theey've verified their email.

username = input("Enter username: ")
password = input("Enter Password: ")
age = input("Enter age: ")
email = input("Enter email: ")
is_admin = True
is_moderator = False
is_banned = False
has_verified_email = True

print(username is not "" and int(age) >= 18)
print(len(password) >= 8 and " " not in password)
print(email is not "" and "@" in email and ".com" in email)
print(isinstance(username, str) and username is not None and len(username)>5)
print((is_admin or is_moderator) and (not is_banned or has_verified_email))
