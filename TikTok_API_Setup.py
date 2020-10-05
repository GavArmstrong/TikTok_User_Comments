from TikTokApi import TikTokApi
api = TikTokApi()

results = 1

trending = api.trending(count=results)

# for tiktok in trending:
#     print(tiktok['desc'].encode("utf-8"))

# print(len(trending))

print(trending[0].keys())
