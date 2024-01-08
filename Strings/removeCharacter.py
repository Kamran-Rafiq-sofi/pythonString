# string = input().strip()
# ch = input().strip()[0]
from sys import stdin


def remove(string, ch):
    output = ""
    for i in range(len(string)):
        if string[i] != ch:
            output += string[i]
    return output


string = stdin.readline().strip()
ch = stdin.readline().strip()[0]
result = remove(string, ch)
print(result)
