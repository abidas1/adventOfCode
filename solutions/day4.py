import requests
import re

url = 'https://adventofcode.com/2020/day/4/input'
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

passports = page.text.split("\n\n")

required = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

valid = 0
valid2 = 0


def validateData(passport):
    count = 0
    if re.search("byr:(\d{4})", passport):
        if int(re.search("byr:(\d{4})", passport).groups()[0]) >= 1920 and int(
                re.search("byr:(\d{4})", passport).groups()[0]) <= 2002:
            count += 1
    if re.search("iyr:(\d{4})", passport):
        if int(re.search("iyr:(\d{4})", passport).groups()[0]) >= 2010 and int(
                re.search("iyr:(\d{4})", passport).groups()[0]) <= 2020:
            count += 1
    if re.search("eyr:(\d{4})", passport):
        if int(re.search("eyr:(\d{4})", passport).groups()[0]) >= 2020 and int(
                re.search("eyr:(\d{4})", passport).groups()[0]) <= 2030:
            count += 1
    if re.search("hgt:\d*(cm|in)", passport):
        if re.search("hgt:\d*(cm|in)", passport).groups()[0] == "cm":
            if int(re.search("hgt:(\d*)cm", passport).groups()[0]) >= 150 and int(
                    re.search("hgt:(\d*)cm", passport).groups()[
                        0]) <= 193:
                count += 1
        elif re.search("hgt:\d*(cm|in)", passport).groups()[0] == "in":
            if int(re.search("hgt:(\d*)in", passport).groups()[0]) >= 59 and int(
                    re.search("hgt:(\d*)in", passport).groups()[
                        0]) <= 76:
                count += 1
    if re.search("hcl:\#[a-f0-9]{6}", passport):
        count += 1
    if re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport):
        count += 1
    if re.search("pid:[0-9]+", passport):
        if len(re.search("pid:([0-9]+)", passport).groups()[0]) == 9:
            count += 1
    if count == 7:
        return True


for passport in passports:
    count = 0
    for index, item in enumerate(required):
        if item in passport:
            count += 1
    if count == 7:
        valid += 1
        if validateData(passport):
            valid2 += 1

print(valid)
print(valid2)
