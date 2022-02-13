from collections import deque
import math

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)
node1 = TreeNode(1)
node6 = TreeNode(6)
node14 = TreeNode(14)
node4 = TreeNode(4)
node7 = TreeNode(7)
node13 = TreeNode(13)

root.left = node3
root.right = node10

node3.left = node1
node3.right = node6

node10.right = node14

node6.left = node4
node6.right = node7

def treeLevelPrint(node):
  if node is None:
    return
  q = deque()
  q.append(node)
  while 0<len(q):
    level_count = len(q)
    for _ in range(level_count):
      crnt_node = q.popleft()
      print(crnt_node.val, end = ' ')
      if crnt_node.left:
        q.append(crnt_node.left)
      if crnt_node.right:
        q.append(crnt_node.right)
    print('')

treeLevelPrint(root)

def isBST(root: TreeNode) -> bool:

  def recurIsBST(node, min: int, max: int) -> bool:
    if node is None:
      return True

    value = node.val
    if value <= min:
      return False

    if max <= value:
      return False

    left_ret = recurIsBST(node.left, min, value)
    right_ret = recurIsBST(node.right, value, max)

    return left_ret and right_ret


  ret = recurIsBST(root, -math.inf, math.inf)
  return ret

print(isBST(root))

###############################

def bst(node:TreeNode) -> bool:

  def bstCheck(node, min:int, max:int) -> bool:
    if node is None:
      return False

    val = node.val
    if val <= min:
      return False

    if val >= max:
      return False

    
    leftCheck = bstCheck(node, min, val)
    rightCheck = bstCheck(node, val, max)

    if leftCheck and rightCheck:
      return True

  result = bstCheck(node, -math.inf, math.inf)
  return result


