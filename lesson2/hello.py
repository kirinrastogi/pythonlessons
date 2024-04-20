# Statements
# are the building blocks of code, and expressions

3 # valid statement, just means 3

"" # valid statement, just means ""


# Types
# data can have many types, like: 
# strings: text data like "hello world"
# ints: whole numbers like 3
# floats: decimals like 3.14
# bools: yes or no, like True or False
# can use helper functions string(), int(), and float() to create variables of specific types

float(3) # 3.000000000
int(3.1) # useful if you want to truncate a value
str(3.1) # can convert from numbers to string
int("3") # and back


# Operators
# operators are used to make code with statements. some common operators that return numbers are: + - / * 
# some other operators that return bools are: < > == != not

# Expressions
# expressions are built out of statements and operators

3 + 4 # statements 3 and 4, and + is the operator
3 != 4 # evaluates to True
3 == 3 # evaluates to True

# operators are often functions


# Variables
# variables are created with the assignment operator '='
# they can be re-assigned to have different types
# the type function returns the type of the input parameter
# variables are deleted when the scope (current indent) ends

z = "hello world" # z can be accessed until the end of the file
# print(type(z))

z = 3
# print(type(z))



# Functions
# We will learn more about functions soon
# for now, think of them as a block of code that takes some value, and returns another
# functions have their own scope, meaning that the variables contained in them are destroyed after the function return
# they look like def functionName(variable1, variable2):
# code
# return
# functions can have multiple return values, but only one of them can be executed! more on this later

def sum(x, y): # defines a function named sum. create two new variables x and y as input. these can be accessed before the return statement
    return x + y # return the value of x + y

x = 4 # different variable from the one defined in sum

# print(sum) # the value of the code block defined above. can be useful sometimes if you need to pass a function to something else that calls it. sum is a statement

# print(sum(1, 2)) # most of the time, you want to call the function using the () brackets. sum(1, 2) is an expression where the statements are 1 and 2, and the operator is the sum function


# If statements
# if statements can be used to control the flow of code

# the simplest form an if statement evaluates a bool, and if the bool is True does one thing, if False, then the other

if 1 == 1:
    print()
    # print("Math is working!")


def guessNumber(guess):
    if guess > 3:
        print("too high")
    elif guess < 3:
        print("too low")
    else:
        print("correct")