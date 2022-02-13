from collections import deque
from typing import List

class TreeNode:
  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(7)
node2n = TreeNode(-2)
node5 = TreeNode(5)
node3 = TreeNode(3)
node15 = TreeNode(15)
node8 = TreeNode(8)
node5n = TreeNode(-1)

root.left = node2n
root.right = node5
node2n.left = node3
node2n.right = node15
node5.left = node8
node5.right = node5n


def printTreeNode(node: TreeNode):
  if node is None:
    return 
  
  q = deque()
  q.append(node)

  while len(q)>0:
    count = len(q)

    for _ in range(0, count):
      crtNode = q.popleft()
      print(crtNode.val, end=' ')
      if crtNode.left:
        q.append(crtNode.left)
      if crtNode.right:
        q.append(crtNode.right)
    
    print('')

printTreeNode(root)


class Path:
  def getPathes(self, root: TreeNode, sum: int) -> List[List[int]]:
    if root is None:
      return []

    self._resultArray = []
    self._getSum(root, sum, [])

    return self._resultArray

  def _getSum(self, node: TreeNode, targetSum: int, crtList: List):
    if node.left is None and node.right is None:
      if node.val == targetSum:
        crtList.append(node.val)
        self._resultArray.append(crtList.copy())
        crtList.pop()
      return

    newSum = targetSum - node.val
    if node.left:
      crtList.append(node.val)
      self._getSum(node.left, newSum, crtList)
      crtList.pop()
    if node.right:
      crtList.append(node.val)
      self._getSum(node.right, newSum, crtList)
      crtList.pop()

    return

    
path = Path()

path.getPathes(root, 20)
