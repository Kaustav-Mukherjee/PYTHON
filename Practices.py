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



#Validate the Quality and correctness of Email Values: 
# 1. Must not be Empty 
# 2. Must contain '.' and "@" 
# 3. Must contain exactly one "@" symbol. 
# 4. Must end with ".com", ".org" or ".net" 
# 5. Must not be longer than 254 characters 
# 6. Must start and end with a letter or digit.

email = "kausty.@gmail.com*"
#Clean the strings for whitespaces
email = email.strip()
#Apply the checks
if email == "":
    print('Email cannot be empty.') # 1.

if not('.' in email and '@' in email):
    print('Email must contain . and @') #2.

if email.count('@') !=1:
    print('Email must contain exactly one "@" symbol') #3.

if not email.endswith(('.com', '.org', '.net')):
    print('Email must end with ".com", ".org" or ".net"') #4.

if len(email) > 254:
    print('Email must not be longer than 254 characters ') #5.

if not(email[0].isalnum() and email[-1].isalnum()):
    print('Email must start and end with a letter or digit') #6.


    ## WE ARE NOT USING ELIF HERE, BECAUSE IN THE LAST CONDITION - THE EMAIL MUST END WITH A LETTER/DIGIT, IF WE ARE USING ELIF THE CONDITION STOPS AT THE CONDITION NO.4 AND DOESN'T CHECK THE REST OF THE CONDITIONS. THUS WE'RE USING INDEPENDENT IF.

