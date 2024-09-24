# 1. Two Sum
# https://leetcode.com/problems/two-sum/submissions/1267660312/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            left = i
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    return [left, right]
                else:
                    right -= 1
