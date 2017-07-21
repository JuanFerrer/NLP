import os
import sys
import json

# Load [1] and find [2] in [3]
filename = sys.argv[1]
attrib = sys.argv[2]
obj = sys.argv[3]


# Read json file
with open(filename) as file:
    contents = file.read()

# Parse to dictionary
jsonData = json.loads(contents)

# Load objects into list
objs = []
for key in jsonData:
    objs.append(jsonData[key])

# Find attribute
if attrib in jsonData[obj]["attributes"]:
    print "Attribute %s found" % attrib
else:
    print "Attribute %s not present" % attrib

# print json.dumps(jsonData, sort_keys = True, indent = 4, separators =
# (',', ': '))
