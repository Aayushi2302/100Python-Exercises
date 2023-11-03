# EXERCISE 13
# generate a list of strings from '1' to '20' using range()
my_list = range(1, 21)
result = map(str, my_list)
print(list(result))

"""
    python map() function returns a map object(which is an iterator) of the results 
    after applying the given function to each item of a given iterable(list, tuple, etc.)

    syntax : map(func, iter)

    # one or more iterable can be passed to map() function
    # returned value is a map object which can be type-casted

"""

# EXERCISE 14
# SOL. - 1
# remove duplicates from a given list
# we can do that by using set() but in that case the order will not be preserved
# so to preserve the order, we use OrderedDict

# SOL. - 2
"""
    This needs to be imported from collections library in python

    OrderedDict is a datatype in python which unlike set preserve the order
    OrderDict.fromkeys(my_list) would produce a dictionary with unique key 
    [("1", None), (1, None), (2, None)]

"""
from collections import OrderedDict
a = ["1", 1, "1", 2]
my_list = list(OrderedDict.fromkeys(a))
print(my_list)

# SOL. - 3
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

# EXERCISE 15
# Dictionaries can be created in the following manner
my_dict = dict(a = 1, b = 2)
print(my_dict)


# KeyError in python is encountered in dictionaries when, it could not find a key that we are trying to access
# dict.values() returns a list-like dict_values object 

# EXERCISE 22
"""
    There is a function pprint() in python library pprint which is used to print out well-formatted views of datatypes in python
"""
from pprint import pprint
my_dict = {
    "a" : list(range(1, 11)),
    "b" : list(range(11, 21)),
    "c" : list(range(21, 31))
}

pprint(my_dict)

# EXERCISE 25
# to print out the letters of the english alphabet from a to z, one letter per line
"""
    string is a built in module in python and string.ascii_lowercase returns a string object containing all 26 letters of English alphabet
"""

import string
for letter in string.ascii_lowercase:
    print(letter)
