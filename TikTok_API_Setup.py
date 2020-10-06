from TikTokApi import TikTokApi
api = TikTokApi()

results = 10

# trending = api.trending(count=results)

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

from random import randint
def random_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

print("68" + str(random_n_digits(19)))
