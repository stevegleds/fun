""" One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. 
I think this exercise is to find a single lower case surrounded by exactly 3 upper case letters."""
#import the argv from sys to allow the passing of parameters
# 5 Nov 2013 just managed to read in the contents of the file
# Need to find a lower case letter surrounded by exactly 3 uppercase letters on both sides

from sys import argv
import re # used to provide findall()
#Assign names to the arguments passed to the script when started - script is the name of the python script and filename is the filename passed when the script is called
script, filename = argv

#open the file whose parameter was passed and assign the txt' variable name
source_file = open(filename) # source_file contains the filename and other file info
txt = source_file.read() # The .read() command reads the contents of the file and this is then stored in txt

# This function looks for the pattern to match against the criteria of the problem 
def find_answer(text):
    search = "[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"
    found = re.findall(search, text) # findall will extract all pattern matches
    print(found)
    return found

# This takes the middle lower case letter to form the required answer
def extract_result(answer):
    result = []
    for word in answer:
        result.append(word[4])
    return result
    
answer = find_answer(txt)
print(answer)
print(extract_result(answer))