# EXERCISE - 30
# Non defualt arguments should be placed before default arguments
# Beacuse if we have non-defualt arguments before default than python will get confused for which argument value is passed

# EXERCISE - 36
with open("C:\\Users\\aasharma\\Downloads\\words1.txt", "r") as file:
    my_data = file.read()
    my_list = my_data.strip().split(" ")
    print(len(my_list))


"""
    There are 2 types of file paths in python :
    1. Absolute path
    2. Relative path

    In windows, we use 2 backlashes beacuse each backlash needs to be escaped by using another backslash.
    So in place of deciding, whether we should use / or \, we rather use os.path.join() method which handles the separators according to OS

    To get the current working directory, we can use 
    # os.getcwd() method

    The current working directory can also be changed during runtime using the os.chdir() method,
    # os.chdir("pass_new_file_dir_path")

    Absolute Path :
    This is the complete path from the root directory to that particular file
    To get the absolute path of current file, use
    # os.path.abspath(__file__)

    Relative Path :
    To minimize the complexity offered by Absolute Path, the concept of Relative Path is used.
    Relative path means the path of a certain file relative to the current working directory

"""

# EXERCISE - 37
import re

with open("C:\\Users\\aasharma\\Downloads\\words2.txt", "r") as file:
    file_content = file.read()

    # SOL. - 1
    file_content = file_content.replace(",", " ")
    my_new_list = file_content.split(" ")
    print(len(my_new_list))

    # SOL. - 2
    # This solution includes using the built-in re module, which provides regular expression matching operations. 
    # We will be using the split method of that module and the expression "|" is meant to replace commas with spaces
    string_list = re.split(",| ", file_content)
    print(len(string_list))

    import math
    print(dir(math)) # to print out all the methods of a particular directory

    # to see how a particluar method of a module works, we can simply
    help(math.pow)

    # EXERCISE - 42
    # to print the sum of homologous elements of each sequence in a new line

    a = [1, 2, 3]
    b = (4, 5, 6)

    """
        zip function returns a zip object, which is an iterator of tuples where the first item in each passed iterator paired together, 
        and then second item is each passed iterator are paired together

        If the length of iterables are different, then the iteraor with the minimum is length is the new iterator length
    """
    
    for i, j in zip(a,b):
        print(i + j)

    for i in range(len(a)):
        print(a[i] + b[i])
    
    """
        #### IMPORTANT
    """
    # EXERCISE - 43
    # creating a script to generate a file where all letters of English alphabet are listed two in each line
    # ex.
    # ab
    # cd, etc.
    import string

    with open("my_script.txt", "w") as file :
        for lst1, lst2 in zip(string.ascii_lowercase[0 : : 2], string.ascii_lowercase[1 : : 2]):
            file.write(lst1 + lst2 + "\n")

# EXERCISE 45
# make 26 text files of with name as each alphabet of english and each file should contain only one letter or alphabet

import os, string 

if not os.path.exists("letters") :
    os.mkdir("letters")
    for alpha in string.ascii_lowercase :
        with open("letters\\" + alpha + ".txt", "w") as file :
            file.write(alpha)

# EXERCISE 46
# to extract the character from each file from letters directory
import glob # this library is used to return all file paths that match a specific pattern

# generally glob patterns specify sets of filenames with wildcard characters. These patterns are :
# 1. Astrisk(*) - matches zero or more characters
# 2. Question Mark(?) - matches exactly one character

letters = []
file_list = glob.glob("letters\\*.txt")

for file_name in file_list :
    with open(file_name, "r") as file :
        letters.append(file.read())

print(letters)

# using format specifiers
firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % (firstname, secondname))

import json
from pprint import pprint
with open("C:\\Users\\aasharma\\Downloads\\company1.json", "r") as file:
    data = json.load(file)
    pprint(data["employees"])


"""
    Python truncate() method truncates the file size. If the optional size argument is present, the file is truncated to (at most) that size.
    enumerate(a) in python creates an enumerate object which yields pairs of indexes and items. Then we iterate through that object print out the item-index pairs in each iteration together with some other strings.
"""

