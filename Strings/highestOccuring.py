from sys import stdin
def highest(string):
    n = len(string)
    if n <= 1:
        return string[0]
    max_count = 0
    result = string[0]
    for i in range(0, n-1):
        count = 1
        for j in range(i+1, n):
            if string[i] == string[j]:
                count += 1
        if count > max_count:
            max_count = count
            result = string[i]
    return result


string = input().strip().strip()
output = highest(string)
print(output)