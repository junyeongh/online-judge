from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rm, cm = len(image), len(image[0])
        target = image[sr][sc]
        if target == color:
            return image

        queue = [(sr, sc)]
        for cell in queue:
            r, c = cell
            if image[r][c] == target:
                image[r][c] = color

            if 0 < r and image[r - 1][c] == target:
                queue.append((r - 1, c))
            if r + 1 < rm and image[r + 1][c] == target:
                queue.append((r + 1, c))

            if 0 < c and image[r][c - 1] == target:
                queue.append((r, c - 1))
            if c + 1 < cm and image[r][c + 1] == target:
                queue.append((r, c + 1))

        return image


if __name__ == "__main__":
    examples = [
        (([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        (([[0, 0, 0], [0, 0, 0]], 0, 0, 0), [[0, 0, 0], [0, 0, 0]]),
    ]
    solution = Solution()
    for example_input, example_output in examples:
        image, sr, sc, color = example_input
        result = solution.floodFill(image, sr, sc, color)
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] For: {example_input}")
        print(f"  {example_output} (Expected)")
        print(f"  {result} (Result)\n")
