import sys


def timeConversion(s):
    # Complete this function
    words = s.split(':')
    check = words[2]
    check1 = check[2:4]
    check2 = check[0:2]
    if check1 == 'AM':
        if words[0] == '12':
            words[0] = '00'
            # print(words[0])
            return (words[0] + ':' + words[1] + ':' + check2)
        else:
            return (words[0] + ':' + words[1] + ':' + check2)
    elif check1 == 'PM':
        if words[0] == '12':
            words[0] = '12'
            return (words[0] + ':' + words[1] + ':' + check2)
        else:
            a = int(s[0:2]) + 12
            return (str(a) + ':' + words[1] + ':' + check2)


s = input().strip()
result = timeConversion(s)
print(result)