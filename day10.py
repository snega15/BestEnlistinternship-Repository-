# STRING CONTAINS ONLY SET OF CHARACTERS

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string =charRe.search(string)
    return not bool(string)
print(is_allowed_specific_char("ABCDEFabcde123450"))
print(is_allowed_specific_char("*&%@#!}{"))

#MATCHES A WORLD CONTAINING 'AB'

import re
def text_match(text):
    patterns = '\w*ab.\W*'
    if re.search(patterns, text):
        return 'found a match!'
    else:
        return('not matched')
print(text_match("the ab is found"))
print(text_match("python excersize"))

#END OF A STRING IS WORD

import re
def text_match(text):
    patterns='\w+\S*$'
    if re.search(patterns, text):
        return 'found a match'
    else:
        return('not matched')
print(text_match("quick fox jumps over the lazy dog."))
print(text_match("gdhfd gyjhjjh hg 6  "))

#SEARCH THE NUMBERS (0-9) OF LENGTH BETWEEN 1 TO 3

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1,12,13,and 345 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))


#MATCH A STRING ONLY CONTAINS UPPER CASE

import re
def text_match(text):
    patterns = '^[A-Z]+$'
    if re.search(patterns, text):
        return 'found  a match'
    else:
        return('not matched')
print(text_match("REEHGHFGF"))
print(text_match("dhjgh"))

    
