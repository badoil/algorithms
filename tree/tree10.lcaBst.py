from collections import deque
from typing import List


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

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

def sortedArrayToBST(nums: List[int]) -> TreeNode:
  length = len(nums)
  if length == 0:
    return None

  center_idx = length//2
  left_nums = nums[0:center_idx]    #slicing, no deep copy
  right_nums = nums[center_idx+1:length]

  value = nums[center_idx]
  node = TreeNode(value)

  left = sortedArrayToBST(left_nums)
  right = sortedArrayToBST(right_nums)

  node.left = left
  node.right = right

  return node
    
root = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10])
treeLevelPrint(root)

def LCA_BST(node: TreeNode, p: int, q: int) -> TreeNode:
  value = node.val
  
  if value <p and value < q:
    ret_node = LCA_BST(node.right,p,q)
    return ret_node
  
  if p <value and q < value:
    ret_node = LCA_BST(node.left,p,q)
    return ret_node
  
  return node
    

lca_node = LCA_BST(root, 7, 10 )
print(lca_node.val) 

##########################################

def sortedArrToBst(nums: List[int]) -> TreeNode:
  length = len(nums)
  if length == 0:
    return None

  centerIdx = length//2

  leftNums = nums[0:centerIdx]
  rightNums = nums[centerIdx+1:length]

  leftNode = sortedArrToBst(leftNums)
  rightNode = sortedArrToBst(rightNums)

  node = TreeNode(nums[centerIdx])
  node.left = leftNode
  node.right = rightNode

  return node


def lcaToBst(node: TreeNode, targetA: int, targetB: int) -> TreeNode:
  val = node.val

  if val < targetA and val < targetB:
    retRight = lcaToBst(node.right, targetA, targetB)
    return retRight

  if val > targetA and val > targetB:
    retLeft = lcaToBst(node.left, targetA, targetB)
    return retLeft
  
  return  node