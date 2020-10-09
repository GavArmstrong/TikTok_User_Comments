from TikTokApi import TikTokApi
import json

api = TikTokApi()

# for tiktok in trending:
#     print(tiktok['id'])
#.encode("utf-8")

# print(len(trending))

#print(trending[0]['stats'])
#print(trending[0]['id'])

# BP = api.getTikTokById(6847667186648059138)
# print(BP)

#print(len("6875482058274229510"))
#print("4"+"5")

# Creating a random 19-digit ID
# from random import randint
# def random_n_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)
#
# count = 5
# for i in range(count):
#     Id = "688060880982019610" + str(random_n_digits(1))
#     TT_Id = api.getTikTokById(int(Id), request_delay=3)
#     print(Id, TT_Id)

# Saving a dictionary
# results = 20
# trending = api.trending(count=results)
#
# for t in trending:
#     print(t['id'])

# saved_json = json.dumps(trending[0])
#
# f = open("dict.json", "w")
# f.write(saved_json)
# f.close()

# from random import uniform
# a = uniform(0.5, 1.5)
# 
# print(a)
