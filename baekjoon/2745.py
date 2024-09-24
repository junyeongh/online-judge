# https://www.acmicpc.net/problem/2745
number, base = input().split()
base = int(base)

number_list = list(number)

coefficient = 1
result = 0
# for i in number[::-1]:
#     print(i)
for i in range(len(number_list)-1, -1, -1):
    digit = ord(number_list[i]) - 48
    if digit > 9:
        digit -= 7
    result += coefficient * digit
    coefficient *= base

print(result)

# 1.
# str = list(input().split(" "))
# print(int(str[0], int(str[1])))

# 2.
# for _ in N[::-1]: