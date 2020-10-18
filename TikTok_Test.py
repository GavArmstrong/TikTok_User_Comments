#from TikTokApi import TikTokApi
#import json

#api = TikTokApi()

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


# from datetime import datetime
# from re import sub
#
# now = datetime.now()
# now = now.strftime("%d/%m/%Y %H:%M:%S")
# now = sub("(/)|(:)|( )", "", now)
#
# print("TikTok_DB/DB_" + now + ".json")

# from os import listdir
# from os.path import isfile, join

# path = os.getcwd()

#files = listdir(path="TikTok_DB")
# file_path = "TikTok_DB"
# files = [file for file in listdir(path=file_path) if isfile(join(file_path, file))]
# print(files)

# import pandas as pd
# #path = "TikTok_DB/test.json"
#
# tbl = pd.read_json(r'\Google Drive\Projects\TikTok User Comments\TikTok_DB\test.json',
#     orient='index')
#
# print(tbl)

# import pandas as pd
# import json
# from os import listdir
# from os.path import isfile, join
# 
# # List the files in te TikTok_DB directory
# path = "Test"
#
# files = [item for item in listdir(path=path) if isfile(join(path, item))]
#
# for f in files:
#     print(f)
#
# import os
# path = os.getcwd()
#
# print(path)
#
# file = join(path, 'test.json')
# print(file)
#
# with open('Test/test.json') as g:
#     read_data = g.read()
#     print(read_data)
