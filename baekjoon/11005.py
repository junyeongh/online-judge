# https://www.acmicpc.net/problem/11005
number, base = [int(x) for x in input().split()]

result = ''
while (number>0):
    number, digit = divmod(number, base)
    if digit > 9:
        result += chr(digit + ord('A') - 10)
    else:
        result += str(digit)

print(result[::-1])