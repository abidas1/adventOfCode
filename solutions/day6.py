import requests

url = 'https://adventofcode.com/2020/day/6/input'
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

yes_array = page.text.split("\n\n")

yes_array[-1] = yes_array[-1][:-1]

total_array = []

for group in yes_array:
    total_array.append(len(set("".join(group.split()))))

print("total yes answers:", sum(total_array))

count = 0

for group in yes_array:
    all_answers = "".join(group.split())
    num_people = len(group.split("\n"))
    for answer in set("".join(group.split())):
        if all_answers.count(answer) == num_people:
            count += 1

print("total number of questions to which everyone answered 'yes':", count)

