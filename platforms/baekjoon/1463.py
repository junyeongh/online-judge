import sys
import heapq

input = sys.stdin.readline

# initial input
source_number = int(input())
# number of total computations to make the number into 1
total_computations = 0

heap = [(0, source_number)]
visited = set()

while heap:
    total_computations, current = heapq.heappop(heap)

    if current == 1:
        break

    if current in visited:
        continue

    visited.add(current)

    if current % 3 == 0:
        heapq.heappush(heap, (total_computations + 1, current // 3))
    if current % 2 == 0:
        heapq.heappush(heap, (total_computations + 1, current // 2))

    heapq.heappush(heap, (total_computations + 1, current - 1))

print(total_computations)
