import requests

url = 'https://adventofcode.com/2020/day/8/input'
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

instructions = page.text.splitlines()

instructionDict = {}

for index, instruction in enumerate(instructions):
    instructionArray = instruction.split(" ")
    sign = instructionArray[1][0]
    num = instructionArray[1][1:]
    instructionDict[index] = [instructionArray[0], sign, int(num)]


def walkInstructions(doOpp=None, step=0, acc=0, stepArray=[]):
    if step in stepArray:
        return acc
    elif step not in instructionDict:
        print("program finished, acc:", acc)
        return False
    else:
        stepArray.append(step)
    if instructionDict[step][0] == "nop":
        if step == doOpp:
            if instructionDict[step][1] == "+":
                return walkInstructions(doOpp, step + instructionDict[step][2], acc, stepArray)
            elif instructionDict[step][1] == "-":
                return walkInstructions(doOpp, step - instructionDict[step][2], acc, stepArray)
        else:
            return walkInstructions(doOpp, step + 1, acc, stepArray)
    elif instructionDict[step][0] == "jmp":
        if step == doOpp:
            return walkInstructions(doOpp, step + 1, acc, stepArray)
        else:
            if instructionDict[step][1] == "+":
                return walkInstructions(doOpp, step + instructionDict[step][2], acc, stepArray)
            elif instructionDict[step][1] == "-":
                return walkInstructions(doOpp, step - instructionDict[step][2], acc, stepArray)
    elif instructionDict[step][0] == "acc":
        if instructionDict[step][1] == "+":
            return walkInstructions(doOpp, step + 1, acc + instructionDict[step][2], stepArray)
        elif instructionDict[step][1] == "-":
            return walkInstructions(doOpp, step + 1, acc - instructionDict[step][2], stepArray)


print("infinite loop, acc:", walkInstructions())

for key in instructionDict:
    if instructionDict[key][0] == "nop" or instructionDict[key][0] == "jmp":
        if not walkInstructions(key, 0, 0, []):
            break
