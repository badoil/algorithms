from collections import deque
from typing import List


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node4.right = node6
node6.left = node8
node5.right = node7
node7.right = node9

class TreeDiameter:
  def solution(self, root: TreeNode) -> int:
    if root is None:
      return 0
    
    self._diameter = 0    
    self._recursiveDepth(root)
    
    return self._diameter
  
  def _recursiveDepth(self, node: TreeNode) -> int:   
    
    left_depth = 0
    right_depth = 0
    if node.left:
      left_depth = self._recursiveDepth(node.left)
    if node.right:
      right_depth = self._recursiveDepth(node.right)
    
    node_diameter = left_depth+right_depth
    self._diameter = max(self._diameter,node_diameter)
    
    node_depth = max(left_depth,right_depth)
    return node_depth+1


##################################3

class TreeDiameter:
  def solution(self, node: TreeNode) -> int:
    if node is None:
      return 0

    self._diameter = 0
    self._getDeep()
    return self._diameter

  def _getDeep(self, node: TreeNode):
    leftDepth = 0
    rightDepth = 0

    if node.left:
      left = self._getDeep(node.left)
    if node.right:
      right = self._getDeep(node.right)

    nodeDepth = max(leftDepth, rightDepth)
    nodeDiameter = leftDepth + rightDepth

    self._dimeter = max(self._diameter, nodeDiameter)

    return nodeDepth + 1