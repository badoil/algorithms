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


class BuildTree:
  def build(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if len(preorder)== 0:
      return None
    
    root = self._recurTree(preorder,inorder)
    return root   
    
    
  def _recurTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if len(preorder) == 0:
      return None
    
    val = preorder[0]
    idx_center = inorder.index(val)    
    
    left_inorder = inorder[0:idx_center]
    left_count = len(left_inorder)
    left_preorder = preorder[1:left_count+1]
    
    right_inorder = inorder[idx_center+1:]
    right_preorder = preorder[left_count+1:]
    
    crnt_node = TreeNode(val)
    
    left_tree = self._recurTree(left_preorder,left_inorder)
    right_tree = self._recurTree(right_preorder,right_inorder)
    
    crnt_node.left = left_tree
    crnt_node.right = right_tree   
    
    
    return crnt_node

buildTree = BuildTree()

preorder = [1,3,7,5,2,4]
inorder = [7,3,1,2,5,4]

root = buildTree.build(preorder, inorder)
treeLevelPrint(root)



class BuildTreeHash:
  def build(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if len(preorder)== 0:
      return None
    self._inorder = inorder
    self._preorder = preorder
    self._inorder_map = {}
    for idx, val in enumerate(inorder):
      self._inorder_map[val] = idx
    self._preorderIdx = 0
    
    tree = self._recurTree(0,len(preorder)-1)
    return tree
    
    
    
  def _recurTree(self, leftIdx:int, rightIdx:int) -> TreeNode:

    if leftIdx > rightIdx:
      return None
    
    val = self._preorder[self._preorderIdx]
    self._preorderIdx = self._preorderIdx+1
    idx_center = self._inorder_map[val]
   
    
    crnt_node = TreeNode(val) 
    left_tree = self._recurTree(leftIdx,idx_center-1)
    right_tree = self._recurTree(idx_center+1,rightIdx)
    crnt_node.left = left_tree
    crnt_node.right = right_tree   
    
    
    return crnt_node

buildTreeHash = BuildTreeHash()
preorder = [1,3,7,5,2,4]
inorder = [7,3,1,2,5,4]

root = buildTreeHash.build(preorder, inorder)
treeLevelPrint(root)


#############################################

class BuildTree:
  def build(self, preorder:List[int], inorder:List[int]) -> TreeNode:
    if preorder is None:
      return None

    result = self._recurBuild()

  def _recurBuild(self, preorder:List[int], inorder:List[int]) -> TreeNode:
    if preorder is None:
      return None

    val = preorder[0]
    centerIdx = inorder.index(val)

    inorderLeft = inorder[0: centerIdx]
    inorderRight = inorder[centerIdx+1:]

    leftCount = len(inorderLeft)
    preorderLeft = preorder[1:leftCount]
    preorderRight = preorder[leftCount+1:]

    crtNode = TreeNode(val)

    leftTree = self._recurBuild(preorderLeft, inorderLeft)
    rightTree = self._recurBuild(preorderRight, inorderRight)

    crtNode.left = leftTree
    crtNode.right = rightTree

    return crtNode

class BuildTreeHash:
  def build(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if preorder is None:
      return None

    self._preorder = preorder
    self._inorder = inorder
    self._preorderIdx = 0

    self._inorderHash = {}
    for idx, val in enumerate(self._inorder):
      self._inorderHash[val] = idx
      
    result = self._recurTree(0, len(preorder)-1)
    return result

  def _recurTree(self, leftIdx: int, rightIdx: int) -> TreeNode:
    if leftIdx > rightIdx:
      return None
    
    val = self._preorder[self._preorderIdx]
    centerIdx = self._inorderHash[val]
    self._preorderIdx += 1

    crtNode = TreeNode(val)

    leftTree = self._recurTree(leftIdx, centerIdx-1)
    rightTree = self._recurTree(centerIdx+1, rightIdx)

    crtNode.left = leftTree
    crtNode.right = rightTree

    return crtNode


    