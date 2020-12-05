from lxml import html
import requests

url = 'https://adventofcode.com/2020/day/1/input'
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
tree = html.fromstring(page.content)

expenseReport = sorted(list(map(int, page.text.splitlines())))


########### part 1 ##############

def solvePart1(array, start, end):
    if array[start] + array[end] == 2020:
        print(array[start] * array[end])
        return
    if array[start] + array[end] > 2020:
        solvePart1(array, start, end - 1)
    if array[start] + array[end] < 2020:
        solvePart1(array, start + 1, end)


solvePart1(expenseReport, 0, len(expenseReport) - 1)

########### part 2 ##############

check = False


def solvePart2(array, start, mid, end):
    if array[start] + array[mid] + array[end] == 2020:
        print(array[start] * array[mid] * array[end])
        global check
        check = True
        return
    if array[start] + array[mid] + array[end] > 2020:
        if end - 1 < mid or end - 1 < 0:
            return
        solvePart2(array, start, mid, end - 1)
    if array[start] + array[mid] + array[end] < 2020:
        if mid + 1 > end or mid + 1 > len(expenseReport) - 1:
            return
        solvePart2(array, start, mid + 1, end)


for x in range(len(expenseReport) - 1):
    solvePart2(expenseReport, x, x + 1, len(expenseReport) - 1)
    if check:
        break
