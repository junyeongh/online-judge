import sys

input = sys.stdin.readline


class Solution:
    def isValid(self, s: str) -> bool:
        # Original implementation (kept for reference)
        # pairs = {
        #     "(": ")",
        #     "[": "]",
        #     "{": "}",
        # }
        # stack = []
        # for char in s:
        #     if char in pairs.keys():
        #         stack.append(pairs[char])
        #     else:
        #         if len(stack) == 0 or stack.pop() != char:
        #             return False
        #         else:
        #             continue
        #
        # return True if len(stack) == 0 else False

        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
                continue
            if len(stack) == 0 or stack.pop() != char:
                return False
        return not stack


# X, Y = map(int, input().split())
# N = int(input())
if __name__ == "__main__":
    examples = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("]", False),
        ("[", False),
    ]
    sol = Solution()
    for example_input, example_output in examples:
        result = sol.isValid(example_input)
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] expected {example_output}")
