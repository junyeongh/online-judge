# 226. Invert Binary Tree
from __future__ import annotations
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree_node(values: Optional[List[int]]) -> Optional[TreeNode]:
        if not values:
            return None

        # it = iter(values)
        # root = TreeNode()
        # cur = root
        # queue = []

        # while (v := next(it, None)) is not None:
        #     l = next(it, None)
        #     r = next(it, None)

        #     cur.val = v
        #     if l is None:
        #         break
        #     cur.left = TreeNode(val=l)
        #     queue.append(cur.left)
        #     if r is None:
        #         break
        #     cur.right = TreeNode(val=r)
        #     queue.append(cur.right)

        #     # cursor to next
        #     if len(queue) != 0:
        #         cur = queue.pop(0)
        #     else:
        #         break

        it = iter(values)
        root = TreeNode(val=next(it))
        queue = [root]

        for node in queue:
            left_val = next(it, None)
            if left_val is not None:
                node.left = TreeNode(val=left_val)
                queue.append(node.left)
            right_val = next(it, None)
            if right_val is not None:
                node.right = TreeNode(val=right_val)
                queue.append(node.right)

        return root

    @staticmethod
    def tree_node_to_list(values: Optional[TreeNode]) -> List[Optional[int]]:
        if values is None:
            return []

        queue: List[Optional[TreeNode]] = [values]
        result: List[Optional[int]] = []
        for node in queue:
            if node is None:
                result.append(None)
                continue
            result.append(node.val)
            if node.left is not None or node.right is not None:
                queue.append(node.left)
                queue.append(node.right)

        # strip trailing Nones
        while result and result[-1] is None:
            result.pop()

        return result


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = [root]
        for node in queue:
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
            node.left, node.right = node.right, node.left

        return root


if __name__ == "__main__":
    examples = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        ([1, 2], [1, None, 2]),
    ]
    solution = Solution()
    for example_input, example_output in examples:
        # ei = TreeNode.list_to_tree_node(example_input)
        # print(ei)
        # print(TreeNode.tree_node_to_list(ei))
        # result = TreeNode.tree_node_to_list(solution.invertTree(TreeNode.list_to_tree_node(example_input)))
        result = TreeNode.tree_node_to_list(solution.invertTree(TreeNode.list_to_tree_node(example_input)))
        status = "PASS" if result == example_output else "FAIL"
        print(f"[{status}] For: {example_input}")
        print(f"  {example_output} (Expected)")
        print(f"  {result} (Result)\n")
