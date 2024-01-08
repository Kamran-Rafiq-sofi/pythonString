def remove_duplicates( string ):
    if len(string) == 0:
        return string
    answer = ""
    answer += string[0]
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            answer += string[i]
    return answer


# string =input().strip().split()
string = input()
output = remove_duplicates(string)
print(output, end="\n")