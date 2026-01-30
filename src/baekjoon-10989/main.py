import sys

input = sys.stdin.readline

n = int(input())
count = [0] * 10_001

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)