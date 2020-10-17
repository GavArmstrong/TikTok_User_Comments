import pandas as pd
import json
from os import listdir
from os.path import isfile, join

# List the files in te TikTok_DB directory
path = "Test"

files = [item for item in listdir(path=path) if isfile(join(path, item))]

for f in files:
    print(f)

# with open('test.json') as g:
#     read_data = g.read()

# print(read_data)

import os
path = os.getcwd()

print(path)
