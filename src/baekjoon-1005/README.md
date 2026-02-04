# 1005번: ACM Craft

<https://www.acmicpc.net/problem/1005>

topological sort; dynamic programming

## First Thoughts

- Looks similar to max flow problem
- Find all sub routes (junctions) to the goal node
  - e.g., for target node 4: paths 1→2→4 and 1→3→4
  - Answer = max of all path costs to target

## Approach

- DAG longest path problem → **Topological sort (Kahn's) + DP**
- `dp[node]` = node 건설 완료까지 걸리는 최소 시간
- 점화식: `dp[node] = max(dp[predecessor] for all predecessors) + D[node]`
- 선행 건물 없으면 `dp[node] = D[node]`

### Why topological sort is needed

- 단순 index 순서로 순회하면 선행 노드의 dp값이 확정되지 않은 상태에서 계산할 수 있음
- Kahn's algorithm (BFS + in-degree)으로 **모든 선행 노드 처리 후에만** 해당 노드를 처리

### Trace (input 1, W=4)

```
D = [10, 1, 100, 10]
dp = [0, 10, 0, 0, 0]   # in_degree 0
→ [0, 10, 11, 0, 0]     # node 1 → node 2: max(0, 10+1)
→ [0, 10, 11, 110, 0]   # node 1 → node 3: max(0, 10+100)
→ [0, 10, 11, 110, 21]  # node 2 → node 4: max(0, 11+10)
→ [0, 10, 11, 110, 120] # node 3 → node 4: max(21, 110+10)
dp[4] = 120
```

## Complexity Analysis

- Time: O(N + K) — each node and edge processed once
- Space: O(N + K) — adjacency list + in-degree + dp arrays

## Mistakes Made

- `D[i]` vs `D[i-1]`: D is 0-indexed, nodes are 1-indexed
- `map(int, ...)` returns iterator, not list — need `list()` to index
- Tried iterating by index order instead of topological order → wrong results
