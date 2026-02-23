# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = "".join(filter(lambda x: x.isalnum(), s.lower()))
        for i in range(len(sp) // 2):
            if sp[i] != sp[-i - 1]:
                return False

        return True


if __name__ == "__main__":
    examples = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]
    solution = Solution()
    for example_input, example_output in examples:
        result = solution.isPalindrome(example_input)
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] Expected: {example_output}, Result: {result}")
        ...
