# Control flow review

# code runs from top to bottom. defining functions can help you control the flow of code, or re-use blocks
# if statements help you branch and run certain code blocks while avoiding others

# use an if statement to return if
# x is greater than lower, and less than upper
def between(x, upper, lower):
    # if ...
    return False


# Ranges
# ranges represent a range of integers, and an increment

# starting at zero is inferred, and ranges are exclusive on the upper bound
# range(10) represents the values from 0 - 9 inclusive
# with zero based counting, there are 10 values represented: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(range(10))

# print(range(0, 5))

# you can use the in keyword to tell if a value is in the range. this only works for integers

# print(5 in range(10))

# print(5.1 in range(10))


# additionally, you can add a third parameter to specify the step. can be useful if you just want even or odd numbers, or every 3rd number for example

# range(0, 11, 2) represents all even numbers from 0 to 10 (including 0 and 10)

# print(10 in range(0, 11, 2))
# print(9 in range(0, 11, 2))

# For loops

# for loops let you repeat a section of code as many times as you want. with ranges, they let you operate on the contents individually.
# you can pass an iterator (a range) to the for loop, and run the code on each value

#for i in range(10):
    #print(i)

# sum values from 0 to x
def sum_values_under(x):
    sum = 0
    for i in range(x):
        sum += i
    return sum

#print(sum_values_under(5))



# pair programming challenge: implement factorial function

def factorial(x):
    return 0

# print(factorial(10)) # should give 3628800
# print(factorial(5)) # should give 120