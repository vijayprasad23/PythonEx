import os
'''
There are two types of files:
    Text Files
    Binary Files
A file whose contents can be viewed using a text editor is called a text file. 
A text file is simply a sequence of ASCII or Unicode characters. 
Python programs, HTML source code are some of the example of text files.

A binary file stores the data in the same way as as stored in the memory. 
The mp3 files, image files, word documents are some of the examples of binary files. 
You can't read a binary file using a text editor.

Before you perform any operation on a file, you must the open it. 
Python provides a function called fopen() to open a file. 
It's syntax is:
    fileobject = open(filename,  mode)

The filename is the name or path of the file.

The mode is a string which specifies the type operation you want to perform on the file 
(i.e read, write, append, etc).

"r"	Opens the file for reading. 
If the file doesn't already exists you will get FileNotFoundError error.

"w"	Opens the file for writing. 
In this mode, if file specified doesn't exists, it will be created. If the file exists, then it's data is destroyed.

"a"	Opens the file in append mode. 
If the file doesn't exists this mode will create the file. 
If the file already exists then it appends new data to the end of the file rather than destroying data as "w" mode does.

We can also specify the type of file (i.e text file or binary file.) 
we want to work with in mode string by appending 't' for text files and 'b' for binary files. 
But since text mode is default mode, it is generally omitted while opening files in text mode.
'''

f = open("readme.txt", "w")

f.write("First Line\n")
f.write("Second Line\n")
f.write("Third Line\n")

f.close()

f = open("readme.txt", "r")

print('All  ', f.readlines()) # read all the lines and returns a list. comment this line to see the rest 
print("1st: ", f.read(4), end="\n\n")    # read the first 4 characters
print("2nd: ", f.read(10), end="\n\n")  # read the next 10 character
print("3rd: ", f.read(), end="\n\n")     # read the remaining characters 



f.close()


