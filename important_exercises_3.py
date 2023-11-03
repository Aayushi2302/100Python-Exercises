# EXERCISE 69
"""
import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])

"""
# above script will generate error because requests module of python does not have get method. The request library have get method
# and since we are naming this file as requests.py so it will import this current pyhton module.
# so it is recommended to not name the module names in the names of libraries in python

# EXERCISE 70
# print the content of a text file with a URL using python

# This task can be done using the requests library that python offers

# import requests
# response = requests.get("http://www.pythonhow.com/data/universe.txt", headers = {'user-agent': 'customUserAgent'})
# text = response.text
# print(text)

"""
    requests library in python :
    This library is used for making HTTP requests in python. It hides the complexities of making request behind a simple API
    so we can focus on services and consuming data in application

    HTTP methods such as GET and POST is the most commonly used methods. One of the most common HTTP methods is GET.
    To make a GET request, we invoke requests.get() 
"""
# response = requests.get("https://api.github.com")
# response is a powerful object for inspecting the results of request. Response object can be used to extract lot of information regarding a request.
# 1. Status Code - gives the status of the request
# we can use response.status_code to access the status code of the request
# __bool__() is an overloaded method in Response

# import webbrowser

# query = input("Input your query: ")
# webbrowser.open("https://google.com/search?q=%s" % query)
"""
    webbrowser library is a standard library used to open the web browser

"""

# read_csv method of pandas library uses urllib library internally to download file.
# So in case of error, we can use a more powerful lib
# import io
# import pandas
# import requests
 
# r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
# c = r.content
# print(r.content)
# print("-----")
# print(r.text)
# data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
# data2 = pandas.read_csv("sampledata_x_2.txt")
# data12 = pandas.concat([data1, data2])
# data12.to_csv("sampledata12.txt", index=None)

import pandas as pd
import matplotlib.pyplot as plt

x = []
y = []

data1 = pd.read_csv("demo.csv")
for index, row in data1.iterrows():
    x.append(row["x"])
    y.append(row["y"])

plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('XY Graph')
plt.show()

# EX. 83
# to print scrren size use, screeninfo - 3rd party library
from screeninfo import get_monitors

width = get_monitors()[0].width
height = get_monitors()[0].height
print("Width : %s, Height : %s" % (width, height))

# EX 84
# pyglet is a 3rd party library for games in python

import pyglet

new_window = pyglet.window.Window()

label = pyglet.text.Label("Hello World",
                          font_name= "Cooper",
                          font_size=15,
                          x = new_window.width//2,
                          y = new_window.height//2,
                          anchor_x='center',
                          anchor_y='center')

@new_window.event
def on_draw():
    new_window.clear()
    label.draw()

pyglet.app.run()

with open("C:\\Users\\aasharma\\Downloads\\countries_raw.txt","r") as file:
    content = file.readlines()
print(content)

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]
print(content)

"""
    sorted() function in python :
     The sorted() function sorts any sequence, like a tuple or a list, 
     and always returns a list with the elements in sorted order. 

     Note that sorted() does not modify the original sequence. 
"""

"""
    pandas.DataFrame.from_records() convert the structured or record data into a dataframe.
"""

"""
    We're using glob  which is a standard Python library that finds pathnames matching a specified pattern. 
    From glob  we're using glob1  which takes a directory name as the first argument and a pattern which 
    in our case is *.py  which returns all the files starting with whatever and ending with .py in the files  directory.
"""

