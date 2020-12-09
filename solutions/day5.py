import requests
import math

url = 'https://adventofcode.com/2020/day/5/input'
headers = {
    'Cookie': '',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'br, gzip, deflate',
    'Host': 'adventofcode.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Accept-Language': 'en-us',
    'Referer': 'https://adventofcode.com/2020/day/1',
    'Connection': 'keep-alive',
}

page = requests.get(url, headers=headers)

boardingPasses = page.text.splitlines()

def getMid(min, max):
    return min + (max - min) / 2


def getLowerRange(min, max):
    return min, math.floor(getMid(min, max))


def getUpperRange(min, max):
    return math.ceil(getMid(min, max)), max


def findZone(charList, min, max):
    newMin = min
    newMax = max
    for i, x in enumerate(charList):
        if x == "F" or x == "L":
            if i == len(charList) - 1:
                return newMin
            newMin, newMax = getLowerRange(newMin, newMax)
        if x == "B" or x == "R":
            if i == len(charList) - 1:
                return newMax
            newMin, newMax = getUpperRange(newMin, newMax)

id_array = []

for boardingPass in boardingPasses:
    id_array.append(findZone(boardingPass[:7], 0, 127) * 8 + findZone(boardingPass[7:10], 0, 7))

print("the max ID in list:", max(id_array))

complete_array = range(min(id_array),max(id_array))

print("your seat ID:",set(complete_array).difference(set(id_array)).pop())

