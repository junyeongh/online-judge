# 242. Valid Anagram
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    examples = [(("anagram", "nagaram"), True), (("rat", "car"), False)]
    solution = Solution()
    for example_input, example_output in examples:
        s, t = example_input
        result = solution.isAnagram(s, t)
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] For: {example_input}")
        print(f"  {example_output} (Expected)")
        print(f"  {result} (Result)\n")
