import sys

input = sys.stdin.readline

while True:
    n = input().strip()
    if n == "0":
        break
    else:
        left, right = 0, len(n) - 1
        is_palindrome = True
        while left < right:
            if n[left] != n[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1
        if is_palindrome:
            print("yes")
        else:
            print("no")

# 01234
# 121
# 1231
# 12421
# 0
