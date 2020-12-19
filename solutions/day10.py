import requests

url = 'https://adventofcode.com/2020/day/10/input'
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

voltages = list(map(int, page.text.splitlines()))

voltages.append(0)

voltages.append(max(voltages) + 3)

voltages = sorted(voltages)

oneJolt = 0
threeJolt = 0

for index, v in enumerate(voltages):
    if index != len(voltages) - 1:
        if voltages[index + 1] - v == 1:
            oneJolt += 1
        elif voltages[index + 1] - v == 3:
            threeJolt += 1
        else:
            continue

print(oneJolt * threeJolt)

voltageGraph = {}

for v in voltages:
    if v + 3 in voltages and v + 1 in voltages and v + 2 in voltages:
        voltageGraph[v] = set([v + 1, v + 2, v + 3])
    elif v + 3 in voltages and v + 1 in voltages:
        voltageGraph[v] = set([v + 3, v + 1])
    elif v + 3 in voltages and v + 2 in voltages:
        voltageGraph[v] = set([v + 3, v + 2])
    elif v + 2 in voltages and v + 1 in voltages:
        voltageGraph[v] = set([v + 2, v + 1])
    elif v + 3 in voltages:
        voltageGraph[v] = set([v + 3])
    elif v + 3 in voltages:
        voltageGraph[v] = set([v + 3])
    elif v + 2 in voltages:
        voltageGraph[v] = set([v + 2])
    elif v + 1 in voltages:
        voltageGraph[v] = set([v + 1])
    else:
        continue

count = 0

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nextNode in graph[vertex] - set(path):
            if nextNode == goal:
                global count
                count += 1
            else:
                stack.append((nextNode, path + [nextNode]))


dfs_paths(voltageGraph, min(voltages), max(voltages))

print(count)




