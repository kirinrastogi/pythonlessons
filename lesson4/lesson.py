# for loop, if statement, and scoping review

# recall that in python, scoping is defined by the indent that you are on.
# creating a variable at the same or higher indent will make it accessible, until the scope is deleted.
# Scope is deleted when the function returns, or when the program ends.

def demo():
    a = 4
    return a

# print(a) # doesn't work, variable is created in demo(), and destroyed when function returns

def demo2():
    sum = 0
    for i in range(10):
        sum += i
    print(i) # works, as it is in scope and has not been deleted yet
    return sum

# demo2()

def demo3(x):
    if x == 3:
        y = 4
    print(y)
    return y

# demo3(3)


# lists

# a list stores a group of objects. can be integers, strings, classes, etc.
# use [] to create, and access a list. 'list' is a keyword, so try giving them a different name

# you can create lists, append to them, and remove from them
def list_demo():
    a = [] # empty list
    print(a)
    a.append("Hello") # now non-empty
    a.append("there!")
    print(a)
    print(len(a))
    a.remove("Hello")
    print(a)

# list_demo()

# lists are often looped over with for loops

# input is list of numbers
def sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

# print(sum([1, 2, 4.5, -3.1, 10]))



# often, you will need to store a variable and make comparisons when looping over lists

# return the maximum value in the list
def max(nums):
    return 0