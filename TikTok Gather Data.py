from TikTokApi import TikTokApi
import json
from random import uniform
from datetime import datetime
from re import sub

api = TikTokApi()

results = 10

file_iter = datetime.now()
file_iter = file_iter.strftime("%Y/%m/%d %H:%M:%S")
file_iter = sub("(/)|(:)|( )", "", file_iter)

f = open("TikTok_DB/DB_" + file_iter + ".json", "w")
f.write("{")

for j in range(10):
    trending = api.trending(count=results, request_delay=uniform(0.5,1.5))

    for i in range(len(trending)):
        f.write("\"")
        f.write(trending[i]['id'])
        f.write("\": ")
        json_obj = json.dumps(trending[i])
        f.write(json_obj)
        if i < len(trending) - 1:
            f.write(",\n")

f.write("}")
f.close()
