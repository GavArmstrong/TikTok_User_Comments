from TikTokApi import TikTokApi
import json
from random import uniform

api = TikTokApi()

results = 5

f = open("TikTok_DB/DB.json", "w")

#

for j in range(20):
    trending = api.trending(count=results, request_delay=uniform(0.5,1.5))

    for i in trending:
        json_obj = json.dumps(i)
        f.write(json_obj)


f.close()
