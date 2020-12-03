import pandas as pd
import json
from os import listdir
from os.path import isfile, join


# List the files in te TikTok_DB directory
path = "TikTok_Test"

files = [item for item in listdir(path=path) if isfile(join(path, item))]

for f in files:
    print(f)

from glob import glob as gg


# a = gg(pathname='Test/*.json')
#
# print(a)
#
# df = pd.DataFrame()
#
# print(df)
#
# for f in a:
#     tmp = pd.read_json(f, orient='index')
#     df = pd.concat([df, tmp], axis=0, ignore_index=True)
#
# print(df)

# with open('Test/'+'test1.json') as g:
#     read_data = pd.read_json(g, orient='index')
#     print(read_data)

# Use glob to make a list of json files in the TikTok_Test directory
b = gg(pathname='TikTok_Test/*.json')

print(b[0])

import json

with open(b[0], "r") as h:
    data = json.load(h)

print(data)
