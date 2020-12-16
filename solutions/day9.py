import requests

url = 'https://adventofcode.com/2020/day/9/input'
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

data = list(map(int, page.text.splitlines()))

invalidNum = 0
copyInvalidNum = invalidNum


def checkSum(x):
    chunkStart = x - 25
    check = False
    for y in range(24):
        for i in range(y + 1, 25):
            if data[chunkStart + y] + data[chunkStart + i] == data[x]:
                check = True
    return check


for x in range(len(data))[25:]:
    if not checkSum(x):
        invalidNum = data[x]
        print(invalidNum, "does not have the property")

reversedData = data[::-1]


def findEncrypt(start, num, inval):
    log = [num]
    while inval > 0 and start < len(reversedData):
        inval -= reversedData[start]
        log.append(reversedData[start])
        start += 1
    if inval == 0:
        print(str(min(log) + max(log)), "is the encryption weakness")
        return


for index, x in enumerate(reversedData):
    if x >= invalidNum:
        continue
    else:
        findEncrypt(index + 1, x, invalidNum)
