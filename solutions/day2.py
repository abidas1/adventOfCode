import requests
import re

url = 'https://adventofcode.com/2020/day/2/input'
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

passwords = page.text.splitlines()

########### part 1 & 2 ############

count1 = 0
count2 = 0

for password in passwords:
    splitArray = password.split(": ")
    passwordString = splitArray[1]
    matchingLetter = splitArray[0][-1]
    matchRange = tuple(map(int, re.match("(\d{1,2})-(\d{1,2})", splitArray[0]).groups()))
    if passwordString.count(matchingLetter) in range(matchRange[0], matchRange[1] + 1):
        count1 += 1

    if (passwordString[matchRange[0] - 1] == matchingLetter and passwordString[matchRange[1] - 1] != matchingLetter) or (passwordString[matchRange[0] - 1] != matchingLetter and passwordString[matchRange[1] - 1] == matchingLetter):
        count2 += 1

print(count1)
print(count2)
