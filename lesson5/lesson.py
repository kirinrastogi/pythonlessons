# Data Structures

# We previously learned about the list.
# Lists can be created with an empty [], or the list() function.
# Lists store data beside each other in memory, and you can access elements from 0 to length - 1
my_list = [1, 2, 3, 4, 5, 6]

# print(my_list[0]) # accessing a list like this is called indexing the list, and the computer jumps to the area of memory specified in the []
# print(my_list[1])
# print(my_list[len(my_list) - 1])

# Removing a value from a list, or adding a value involves a copy of the entire list.

# my_list.append(7) # append finds a new space in memory that can fit the elements sequentially. sometimes this involves a copy

# print(my_list)

# my_list.remove(1) # removes the value 1 from the list, not the indexx

# print(my_list)



# Sets

# sets let you store data in an unordered manner. Iterating over a set doesn't always give you the same order of data.
# adding/removing from a set is extremely fast. sets do not contain duplicates! if a value is added to the set twice, it will only exist there once.

# sets are created with set() or {}. Instead of [], we lookup a value with and are added/removed to with the same functions as before.

my_set = {"Red", "Green", "Blue"}
# my_set.add("Purple")

# print("Green" in my_set)

# print(my_set)
# my_set.remove("Blue")


# iteration
# use the enumerate keyword to get the number, and value in a set. note that the number is not the index, as the set is unordered.

for i, val in enumerate(my_set):
    # print(i)
    print(val)


# Dicts

# dictionaries are like sets but you can associate a value to them. they are very useful for associating data together.
# also created with {}, or the dict() function. Defining a dict requires a colon separator :
# you can use [] to lookup values, and set them in a dictionary

my_phonebook = {"Bob": "+1(613) 555-4821", "Joe": "+1(705) 555-7982"}

# print(my_phonebook["Bob"])

# my_phonebook["Reggie"] = "+1(688) 555-1234"

# print(my_phonebook["Reggie"])