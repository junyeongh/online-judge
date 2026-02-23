import sys

input = sys.stdin.readline

# 1. Get inputs
n = int(input())
vec = [float(input()) for _ in range(n)]

# 2. Calculated using Dynamic Programming
"""
a   b   c   d
ab  bc  cd
abc bcd
abcd
"""
# variable to store
max_product = vec[0]

for i in range(1, n):
    vec[i] = max(vec[i], vec[i] * vec[i - 1])
    max_product = max(max_product, vec[i])

print(f"{max_product:.3f}")
