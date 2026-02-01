"""
DFS Function

- We need to explore all paths? yes
- We need to backtrack to explore different branches? yes

"""

def maxDepth(root):
  if root == None:
    return 0
  left_depth = maxDepth(root.left)
  right_depth = maxDepth(root.right)
  return 1 + max(left_depth, right_depth)
