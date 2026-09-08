# ==========================================================================================
# Strings::
#
# ~ A String is a sequence of characters, enclosed in single or double quotes.
# ~ Used to represent text data in Python.
# ~ Immutable, meaning once created, their value cannot be changed.
# ==========================================================================================

#Types:

name = "Kaustav" #This is a string enclosed in double quotes
print(type(name)) #This will print the data type of variable name, which is <class 'str'>

age = 25
print(type(age)) #This will print the data type of variable age, which is <class 'int'>

#print('Your age is:' + age) #This will raise a TypeError because we are trying to concatenate a string and an integer. We need to convert the integer to a string using the str() function.

print('Your age is:' + str(age)) #This will print the string "Your age is:25" by converting the integer age to a string using the str() function. The original data type stays the same, but at the print the datatype gets converted to do a string concatenation. 

# To change the data type of the age at the variable level, we can do the following:
age = str(age) #This will convert the integer age to a string and store it in the variable age
print(type(age)) #This will print the data type of variable age, which is now <class 'str'>
print('Your age is:' + age) #Here we can concatenate the string and the variable, because both are now strings.

#Math operations on strings:
password = "password123"
print(len(password)) #This will print the length of the string "password123" using the variable password. The len() function returns the number of characters in a string, including spaces and punctuation. OUTPUT: 11


text = '''
Python is easy to learn.
Python is powerful.
Many people love python.
'''
print(text.count("Python")) #This will count the number of occurrences of the substring "Python" in the string text.
#Here the output comes as 2 , because the count() method is case-sensitive, and it only counts the "Python" with only the uppercase P. The "python" with lowercase p is not counted.
print(text.count("python"))
#Here only the "python" with lowercase p is counted, and the output comes as 1. The "Python" with uppercase P is not counted.


#Transformation of strings:

# ~replace()
price = "1234,56"
print(price.replace(",","."))

phone = "123-456-7890"
print(phone.replace("-","/")) #This will replace all occurrences of the hyphen (-) in the string phone with a forward slash (/). The output will be "123/456/7890".
print(phone.replace("-", "")) #This will replace all occurrences of the comma (-) in the string phone with an empty string (""), effectively removing them. Since there are no commas in the string phone, the output will be the same as the original string: "123-456-7890".  

price ="$1,299.99"
print(price.replace("$","").replace(",", "")) #This will replace the dollar sign ($) in the string price with an empty string (""), effectively removing it. Then, it will replace all occurrences of the comma (,) in the string price with an empty string (""), effectively removing them as well. The output will be "1299.99".
#Chained methods are executed in order from left to right. Each replace() runs on the result of the one before it. 


#Convert the messy phone number to a clean format: +49 (176) 123-4567 to 00491761234567
phone = "+49 (176) 123-4567"
print(phone.replace("+","00").replace("(","").replace(")","").replace("-","").replace(" ","")) #OUTPUT: 00491761234567

first_name = "Kaustav"
last_name = "Mukherjee"
name = first_name + " " + last_name #This will concatenate the strings first_name and last_name with a space in between and store it in the variable name
print(name) #This will print the string "Kaustav Mukherjee" using the variable name

# ~f-string
age = 25
print('My name is' , name , 'and I am' , str(age) , 'years old') #This will print the string "My name is Kaustav Mukherjee and I am 25 years old" using the variables name and age. The str() function is used to convert the integer age to a string for concatenation.
print(f'My name is {name} and I am {age} years old') #This will print the string "My name is Kaustav Mukherjee and I am 25 years old" using the variables name and age. The f-string allows us to embed expressions inside string literals, using curly braces {}. It automatically converts the values to strings for concatenation.

print(f'2 + 3 = {2+3}') #This means we can also insert not oly variables but also expressions inside the curly braces{}.

#Now, if i want to print the curly brackets at the output as well:
print(f"{{This is me}}")


# ~split()
stamp = "2023-06-01 12:30:45"
stamp.split(" ")
print(stamp.split(" ")) #This will split the string stamp into a list of substrings, using the space character as the delimiter. The output will be ['2023-06-01', '12:30:45'].
print(type(stamp.split(" "))) #The split() method returns a list of substrings.

stamp = "2023-06-01"
print(stamp.split("-"))

csv_file = "1234,Kaustav,India,25,2002-06-19,M"
print(csv_file.split(","))

# ~String Repeat (*)
print("="*30)
print("ha"*3)
print("="*30)

# ~String Indexing & Slicing

text = "Python"


print(text[0])
print(text[-6]) # Both of these Extracts the first character from the string.

print(text[5])
print(text[-1]) #Both of these extracts the last character from the string.

date = "2026-09-20"

print(date[0:4]) #extracting the month from the string.

print(f'The Year is: {date[0:4]}, The month is: {date[5:7]}, The date is: {date[8:]}')


# Data Cleansing: Removing Spaces

text = input('enter your text with whitspaces:')

print(text.lstrip()) #Removes unwanted spaces from the left side.
print(text.rstrip()) #Removes unwanted spaces from the right side.
print(text.strip()) #Removes unwanted spaces from the both sides.

    #Removing any characters, not only spaces from a string value:
    
text = "####I Love to code##########"
print(text.strip("#"))

    #Checking for extra spaces in data:
text = "  Engineering  "
print(len(text)) #Gives the total length of the text
print(len(text.strip())) #Gives the trimmed length of the text

print(print(len(text)) == len(text.strip()))
#Making th output prettier-

no_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())

print('Number of spaces in text:', no_of_spaces)
print('Is my data clean?', is_clean)

# Data Cleansing: Case Conversion

text = "Python PROGRAMMING"
print(text.lower()) #Makes all letters lowercase
print(text.upper()) #Makes all letters uppercase

    #Cleaning up data before searching-
search = "Email".lower().strip()
data = "EmAIl".lower().strip()

print(search == data)


# Searching:

phone ="+48-176-12345"
print(phone.startswith("+49")) #Finds the value at the start of a string. Output in Boolean

email = "kaustavmukherjee2023@gmail.com" 
print(email.endswith("gmail.com")) #Finds the value at the end of a string. Output in Boolean

print("@" in email) #Finds the value throughout the string. Output in Boolean

print(email.find("@")) #Finds the First Position of occurence of the value in the string.

    #=======================================================================================================
    #Use Case: Searching and removing the country codes for mobile numbers

phone1 = "+48-176-12345"
phone2 = "48-665-34567"
phone3 = input('Enter phone number:')

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
print(phone1, phone2, phone3)

    #=======================================================================================================

# Check and Validate:

country = 'India'
print(country.isalpha()) #Only gives the output as true if each and every one of the characters in the string is a letter.

number = '0123456789'
print(number.isnumeric()) #Only gives the output as true if each and every one of the characters in the string is a number.
#Also, isnumeric() doesn't accept float numbers




















