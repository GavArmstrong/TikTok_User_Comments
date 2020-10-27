from TikTokApi import TikTokApi
import json
from random import uniform
from datetime import datetime
from re import sub

api = TikTokApi()

results = 2

file_iter = datetime.now()
file_iter = file_iter.strftime("%d/%m/%Y %H:%M:%S")
file_iter = sub("(/)|(:)|( )", "", file_iter)

f = open("TikTok_DB/DB_" + file_iter + ".json", "w")
f.write("{")


for j in range(1):
    trending = api.trending(count=results, request_delay=uniform(0.5,1.5))

    for i in range(len(trending)):
        f.write("{\"id\": \"")
        f.write(trending[i]['id'])
        f.write("\",\n\"TikTok\": ")
        json_obj = json.dumps(trending[i])
        f.write(json_obj)
        f.write("}")
        if i < len(trending) - 1:
            f.write(",\n")

f.write("}")
f.close()
