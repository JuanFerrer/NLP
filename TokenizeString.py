import os
import sys
import re

# Read json file
# with open(filename) as file:
#     contents = file.read()

contents = "At eight o'clock on Thursday morning Arthur didn't feel very good."

sentence = {}

contents = contents.split();

tokens = []

key = "[^\w']"

for word in contents:
    for token in re.split(key, word):
        if token != '':
            tokens.append(token)
            print token

#print tokens