import requests
import re

url = 'https://adventofcode.com/2020/day/7/input'
headers = {
    'Cookie': '_ga=GA1.2.1931018988.1606257418; _gid=GA1.2.494245323.1607037582; session=53616c7465645f5fe33b704fdab95cd43e4e0cf32f49c3ad6f104b3fbbf60e2fb7d7040bef55a50ad3c30f5739bf9488',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'br, gzip, deflate',
    'Host': 'adventofcode.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Referer': 'https://adventofcode.com/2020/day/1',
    'Connection': 'keep-alive',
}

page = requests.get(url, headers=headers)

rules = page.text.splitlines()

count = 0

firstBags = []

nextBags = []

for index, rule in enumerate(rules):
    if re.search("(.*)\sbags\scontain.*shiny gold", rule):
        count += 1
        firstBags.append(re.search("(.*)\sbags\scontain.*shiny gold", rule).groups()[0])
        del rules[index]

prevBags = firstBags
nextBags = []

while True:
    if len(nextBags) > 0:
        prevBags = nextBags
    nextBags = []
    for bag in prevBags:
        for index, rule in enumerate(rules):
            if re.search("(.*)\sbags\scontain.*" + re.escape(bag), rule):
                count += 1
                nextBags.append(re.search("(.*)\sbags\scontain.*" + re.escape(bag), rule).groups()[0])
                del rules[index]
    if len(nextBags) == 0:
        break

print(count, "bags that can contain a shiny gold bag")

inGoldBags = []
inGoldBags2 = []
prevBags2 = []
nextBags2 = []

for index, rule in enumerate(rules):
    if re.search("shiny gold\sbags\scontain(.*)", rule):
        inGoldBags = re.search("shiny gold\sbags\scontain(.*)", rule).groups()[0]

for bag in inGoldBags.split(","):
    inGoldBags2.append([re.search("(\w+\s\w+)\sbags", bag).groups()[0], int(bag[1])])

prevBags2 = inGoldBags2
nextBags3 = []

countArray = []

for item in inGoldBags2:
    countArray.append(item[1])

while True:
    if len(nextBags3) > 0:
        prevBags2 = nextBags3
        nextBags3 = []
    for bag in prevBags2:
        for rule in rules:
            if re.search(bag[0] + "\sbags\scontain(.*)", rule):
                containedBags = re.search(bag[0] + "\sbags\scontain(.*)", rule).groups()[0]
                if re.search(bag[0] + "\sbags\scontain(.*)", rule).groups()[0] == " no other bags.":
                    continue
                else:
                    if "," in re.search(bag[0] + "\sbags\scontain(.*)", rule).groups()[0]:
                        for bag2 in re.search(bag[0] + "\sbags\scontain(.*)", rule).groups()[0].split(","):
                            countArray.append(int(bag2[1]) * bag[1])
                            nextBags3.append([re.search("(\w+\s\w+)\sbag", bag2).groups()[0], int(bag2[1])*bag[1]])
                    else:
                        nextBags3.append([re.search("(\w+\s\w+)\sbag", containedBags).groups()[0],int(containedBags[1]) * bag[1]])
                        countArray.append(bag[1] * int(re.search(bag[0] + "\sbags\scontain(.*)", rule).groups()[0][1]))
    if len(nextBags3) == 0:
        break

print("the shiney gold bag containes",sum(countArray), "bags!")

