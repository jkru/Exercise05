"""
Opens a file named on the command line and
counts how many times each letter occurs in that file.
 """

from sys import argv
import string

script, filename = argv     

input_file = open(filename)     # open file you want to read

filetext =  input_file.read()   # storing full contents of file in a string
filetext = filetext.lower()     # changing all characters to lowercase

letters = list(string.ascii_lowercase)    # creating list of letters

char_count = []                 # initializing count list that mirrors length of letters list
for i in range(len(letters)):
    char_count.append(0) 

for char in filetext:           # iterating through characters in text
    if char in letters:         # if char is a letter
        char_count[letters.index(char)] += 1    # increment character count

for i in range(len(letters)):   # printing character counts
    print char_count[i]