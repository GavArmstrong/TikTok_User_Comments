from TikTokApi import TikTokApi
import json
from random import uniform
from datetime import datetime
from re import sub

api = TikTokApi()

results = 5

file_iter = datetime.now()
file_iter = file_iter.strftime("%d/%m/%Y %H:%M:%S")
file_iter = sub("(/)|(:)|( )", "", file_iter)

f = open("TikTok_DB/DB_" + file_iter + ".json", "w")



for j in range(20):
    trending = api.trending(count=results, request_delay=uniform(0.5,1.5))

    for i in trending:
        json_obj = json.dumps(i)
        f.write(json_obj)


f.close()
