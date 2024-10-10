# 1463번: 1로 만들기

## First Thoughts

3->1: Divide by 3
2->1: Divide by 2 or Subtract 1

while the source number is an integer greater than 1
  divide by 3 unless it's not divisible by 3
  divide by 2 unless it's not divisible by 2

```python
while source_number != 1:
    if (source_number % 3 == 0):
        source_number /= 3
    elif (source_number %2 == 0):
        source_number /= 2
    else:
        source_number -= 1
    print(f"Current: {source_number}")
    total_computations += 1

print(total_computations)
```

example of 10:
10 (/2) 5 (-1) 4 (/2) 2 (/2) 1 => 4 computations
but,
10 (-1) 9 (/3) 3 (/3) 1 => 3 computations

## Approach

Knowing that this problem is categorized as dynamic programming, I came up with the following approach:

Using a priority queue to find the minimum number of operations

example of 10:                (current_comp, number)
10: (%3, %2, -1) = (_, 5, 9) [(1, 5), (1, 9)]
 5: (%3, %2, -1) = (_,_, 4) [(1, 9), (2, 4)]
 9: (%3, %2, -1) = (3, _, 8) [(2, 3), (2, 4), (2, 8)]
 3: (%3, %2, -1) = (1) <- no need further computation

1. prioritize lower current_computation
2. when these are identical, prioritize smaller number (thinking heuristically)

## Answers from other people

```python
def make_one(n):
  dp = [0] * (n + 1)

  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
      dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
      dp[i] = min(dp[i], dp[i // 3] + 1)

  return dp[n]

if __name__ == "__main__":
  n = int(input())
  print(make_one(n))
```

I found most of the answers created a list of size n+1 and iterated through the list to find the minimum number of operations.

- I wonder
  - if this is still considered as dynamic programming
  - why my approach is not used by others (when it's significantly faster)
