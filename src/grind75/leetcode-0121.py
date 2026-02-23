# 121. Best Time to Buy and Sell Stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest: int = prices[0]
        max_profit: int = 0

        for i in range(1, len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            else:
                if max_profit < prices[i] - cheapest:
                    max_profit = prices[i] - cheapest

        return max_profit


if __name__ == "__main__":
    examples = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]
    solution = Solution()
    for example_input, example_output in examples:
        result = solution.maxProfit(example_input)
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] Expected: {example_output}, Result: {result}")
