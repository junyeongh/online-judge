import sys
from collections import deque

input = sys.stdin.readline


T = int(input())
for i in range(T):
    # N for numbers of buildings
    # K for numbers of predicates
    N, K = map(int, input().split())

    # D for time takes to build each building
    D = list(map(int, input().split()))

    dp = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    # W for building to win
    W = int(input())

    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            dp[i] = D[i - 1]
            queue.append(i)

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            dp[nxt] = max(dp[nxt], dp[node] + D[nxt - 1])
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    # print(f"{dp[W]=}")
    print(dp[W])
