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
