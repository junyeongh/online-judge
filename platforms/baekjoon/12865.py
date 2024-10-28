# Knapsack problem
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
# print(f"{n=}, {k=}")

items = [list(map(int, input().split())) for _ in range(n)]  # weight, value
# items.sort(key=lambda x: x[1] / x[0], reverse=True)  # value / weight
# print(items)

# max_value, current_weight = 0, 0
# for weight, value in items:
#     if current_weight + weight <= k:
#         max_value += value
#         current_weight += weight
#     else:
#         break

# print(max_value)

# confused 0-1 knapsack problem with fractional knapsack
##################################################

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j >= items[i - 1][0]:
            dp[i][j] = max(
                items[i - 1][1] + dp[i - 1][j - items[i - 1][0]], dp[i - 1][j]
            )
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
