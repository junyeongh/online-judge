# 1
import sys

input = sys.stdin.readline


N, K = map(int, input().split())

l = [x for x in range(1, N + 1)]
jp = []
for i in range(N):
    idx = (K - 1) % len(l)
    a, e, b = l[0:idx], l[idx], l[idx + 1 :]
    # print(a, "\t", e, "\t", b)

    jp.append(e)
    l = b + a
print(jp)

# 2
from collections import deque
import sys

input = sys.stdin.readline


N, K = map(int, input().split())
q = deque(range(1, N + 1))
result = []
for _ in range(N):
    q.rotate(-(K - 1))
    result.append(q.popleft())
# print(result)
print(f"<{', '.join(str(r) for r in result)}>")
