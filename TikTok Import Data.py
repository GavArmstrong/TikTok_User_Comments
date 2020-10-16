import pandas as pd
import json
from os import listdir
from os.path import isfile, join

# List the files in te TikTok_DB directory
path = "TikTok_DB"

files = [item for item in listdir(path=path) if isfile(join(path, item))]


print(files)
