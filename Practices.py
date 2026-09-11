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


    # WE ARE NOT USING ELIF HERE, BECAUSE IN THE LAST CONDITION - THE EMAIL MUST END WITH A LETTER/DIGIT, IF WE ARE USING ELIF THE CONDITION STOPS AT THE CONDITION NO.4 AND DOESN'T CHECK THE REST OF THE CONDITIONS. THUS WE'RE USING INDEPENDENT IF.



# Print the 7-times table from 1 to 10 using for loop:

for number in range(1,11):
    print(f'7 X {number} = {7*number}')

    #OUTPUT:
    # 7 X 1 = 7
    # 7 X 2 = 14
    # 7 X 3 = 21
    # 7 X 4 = 28
    # 7 X 5 = 35
    # 7 X 6 = 42
    # 7 X 7 = 49
    # 7 X 8 = 56
    # 7 X 9 = 63
    # 7 X 10 = 70


# Print a left aligned pyramind of stars with 6 rows using a for loop:

for star in range(1,7):
    print('*'*star)

    #OUTPUT:
    # *
    # **
    # ***
    # ****
    # *****
    # ******

# Loop through a list of Days and print only the working days, skipping the weekends.

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
weekends = ['Saturday', 'Sunday']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')

# Scan emails to block unsafe data from entering your system.

emails = [
    'data@gmail.com',
    'kaustavmukhe456@gmail.com',
    'kalmukhe12@yahoo.in',
    'DROP TABLE USERS;',
    'shankhalikamallick@gmail.com'
]
for email in emails:
    if ';' in email:
        print('SQL INJECTION ALERT !!!!')
        break
    print(f'Processing emails: {email}')


emails = [
    'data@gmail.com',
    'kaustavmukhe456@gmail.com',
    'kalmukhe12@yahoo.in',
    'DROP TABLE USERS;',
    'shankhalikamallick@gmail.com'
]
for email in emails:
    if '@' not in email:
        print('SQL INJECTION ALERT !!!!')
        break
    print(f'Processing emails: {email}')

# Check for Missing Names in a list:

names = ['Kausty', 'Shanky', 'Kundky', None, 'Shovky']
for name in names:
    if name is None:
        print('Found a missing name.')
        break
else:
    print('All names are available!')



# Check wether any filename appears more than once. Print 'Duplicate Found' if a duplicate exists, else print 'All files are unique'

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

for file in file_list:
    if file_list.count(file) > 1:
        print('Duplicate Found')
        break
else:
    print('All files are unique')