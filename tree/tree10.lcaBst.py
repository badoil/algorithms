
# height balanced BST 란 외쪽 서브트리와 오른쪽 서브트리의 뎁스 차가 1 이하인 트리


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



########################################################################
# 108
# sorted Array에서 height balanced BST를 만들어라


def sortedArrayHBBST(nums: List[int]) -> TreeNode:
  if len(nums) == 0:
    return None

  count = len(nums)
  centerIdx = count//2
  
  left = nums[0:centerIdx]
  right = nums[centerIdx+1:]

  leftResult = sortedArrayHBBST(left)
  rightResult = sortedArrayHBBST(right)

  crtNode = TreeNode(nums[centerIdx])
  crtNode.left = leftResult
  crtNode.right = rightResult

  return crtNode


########################################################################
# 235
# 주어진 BST의 LCA를 찾아라
# BST에서 해당 노드가 LCA 라면 targetA < node.val < targetB 일것. 이 조건을 만족하는 노드를 찾으면 됨

def lowestCommonAncestorBinarySearchTree(node: TreeNode, targetA: int, targetB: int) -> TreeNode:
  if node is None:
    return None

  val = node.val

  if targetA > val and targetB > val:     # 타겟 A, B가 해당 노드 값보다 크면, 해당 노드의 오른쪽 자식 노드들만 탐색
    result = lowestCommonAncestorBinarySearchTree(node.right, targetA, targetB)
    return result

  if targetA < val and targetB < val:     # 타겟 A, B가 해당 노드 값보다 작으면, 해당 노드의 왼쪽 자식 노드들만 탐색
    result = lowestCommonAncestorBinarySearchTree(node.left, targetA, targetB)
    return result

  return node       # 위 조건문에 걸리지 않는 노드는 targetA < node.val < targetB 일것. 해당 노드 리턴