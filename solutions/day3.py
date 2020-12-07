import requests

url = 'https://adventofcode.com/2020/day/3/input'
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

lines = page.text.splitlines()


def findTrees(stepX, stepY, x=0, y=0, treeCount=0):
    if x >= len(lines[0]):
        x -= len(lines[0])
    if lines[y][x] == '#':
        treeCount += 1
    if y >= len(lines) - 1:
        return treeCount
    return findTrees(stepX, stepY, x + stepX, y + stepY, treeCount)


# Part 1
result = findTrees(3, 1)
print("In part 1, there are %d trees in your path." % result)

# Part 2
result = findTrees(1, 1) * findTrees(3, 1) * findTrees(5, 1) * findTrees(7, 1) * findTrees(1, 2)
print("For part 2, the answer is %d." % result)
