from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


if __name__ == "__main__":
    examples = [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1),
        (([5], 5), 0),
        (([-1, 0, 5], 5), 2),
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 13), -1),
    ]
    solution = Solution()
    for example_input, example_output in examples:
        nums, target = example_input
        result = solution.search(nums, target)
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] For: {example_input}")
        print(f"  {example_output} (Expected)")
        print(f"  {result} (Result)\n")
