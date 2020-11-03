# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today we will learn about Modules: time, datetime, math, & how to create your own!

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# To use a module, we have to import it first. We do this with the keyword import.
# We also have to install the module if it is one not already downloaded with the IDE.
# Or we can make our own module.

# Lets try out the time module, a widely known one.
# We can use this module to make a program "sleep" or to access the time. First we need to import
# To use the module's functions we use the dot operator: nameOfModule.nameOfFunction()
import time
print("Starting in...")
time.sleep(.5)              # Creates a .5 second pause before the next line of code executes
print("3")
time.sleep(1)               # Creates a 1 second pause before the next line of code executes
print("2")
time.sleep(1)               # Creates a 1 second pause before the next line of code executes
print("1")
time.sleep(1)               # Creates a 1 second pause before the next line of code executes
print("GO!")

# I used this module for the CS Club video, let me show you the code.

# While the time module can also access the time, I prefer the module datetime
# datetime has more capabilities... Now you try to import it
# Use the module's function: datetime.datetime.now() to access the current date and time.
# Store it as a variable called currentDate and then print
import datetime
currentDate = datetime.datetime.now()
print(currentDate)
time = currentDate.strftime("%H")
print(time)
# This data form (datetime.now()), can be transformed into a useful data type with other functions
# Use the function .strftime("H") on the currentDate variable and store it in the variable: hour. Print!
# for this function .strftime(), the argument will change the returned data type. "H", gives the hour as a string

# Now we will use the math module. This is a very common module.
import math
print(math.cos(4.565))      # Returns the cosine of x radians
print(math.radians(180))    # Converts angle x from degrees to radians
print(math.pi)              # The mathematical constant π = 3.141592…, to available precision
print(math.pow(2, 3))       # First number raised to the second number

# There are many more functions of the math module. Just look up "__ python module" online to find all documentation
# We can also create modules and use them. To do so, this cannot easily be done on repl, so just follow along on
# my shared screen to watch me code it. Or download an IDE and follow along.

# First create a new python file and the functions you plan to use, all under one project
# Then on the file you would like to use the module on, import the python file name.
# Now to access the module's functions, call on it like this: nameOfModule.nameOfFunction()

# Lets try it.
# Make a new python file called susd. Make sure it is under the same project folder.
# Now copy the function below that we made in lesson #4, into the susd file
"""
def susdEmail(firstName, lastname, idNumber):
    firstInital = firstName[0]
    lastTwo = idNumber % 100
    email = firstInital + lastname + str(lastTwo) + "@susdgapps.org"
    return(email)
"""
# Now import the susd module into this project and call on the susdEmail function, with the correct arguments.
import susd
matthewEmail = susd.susdEmail("Matthew", "Salaway", 765534)
print(matthewEmail)
