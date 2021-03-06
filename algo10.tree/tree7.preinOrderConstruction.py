# 105
# 문제:  preOrder list와 inOrder List가 주어졌을때 두개의 Lists를 기반으로 Tree를 구성하여라

# preorder = [1,3,7,5,2,4]
# inorder = [7,3,1,2,5,4]

# 하나의 preOrder list 만들어질 수 있는 트리는 다양한 경우의 수가 있기 때문에 inOrder List도 필요
# preorder의 첫번째 값이 root, 이 root를 기준으로 inorder에성 좌우를 나눌 수 있음
# 즉 하나의 프라블럼을 두개의 서브 프라블럼으로 나눔, 이것은 recursive로 만들면 된다고 생각할 수 있음

# 재귀함수에서 항상 잊지말아야할 것은 일단 끝까지 간다음에 거기서 결과값을 쌓아올리는 과정이라는 것임.
# 여기 트리로 생각하면, 리프까지 가서 그 리프가 부모노드에 연결되서 리턴되면서 최상위 부모노드로 가는 과정인 것임

# 재귀함수를 만들때는, 

# 풀이법1: TC O(n*n), SC O(depth)
# 풀이법2(hash): TC O(n), SC O(n)


from collections import deque
from platform import node
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

class MakingTree:
  def solution(self, preorderNodeA: List[int], inorderNodeB: List[int]) -> TreeNode:
    if len(preorderNodeA) is None: 
      return

    result = self._recur(preorderNodeA, inorderNodeB)
    return result

    
  def _recur(self, nodeA: List[int], nodeB: List[int]):
    if len(nodeA) == 0:
      return

    val = nodeA[0]
    centerIdx = nodeB.index(val)    # 이 함수가 O(n)이 걸리고 이거 때문에 모든 노드를 순회 O(n)하는 재귀함수에, 워스트 케이스 O(n*n)이 나올 수 있음

    crtNode = TreeNode(val)
    
    leftInorder = nodeB[0:centerIdx]
    leftCount = len(leftInorder)
    leftPreorder = nodeA[1: leftCount+1]

    rightInorder = nodeB[centerIdx+1:]
    rightPreorder = nodeA[leftCount+1:]

    leftResult = self._recur(leftPreorder, leftInorder)
    rightResult = self._recur(rightPreorder, rightInorder)

    crtNode.left = leftResult
    crtNode.right = rightResult

    return crtNode


class MakingTreeByHash:
  def solution(self, preorderNodeA: List[int], inorderNodeB: List[int]) -> TreeNode:
    if len(preorderNodeA) == 0:
      return None

    self._preorderIdx = 0
    self._preorderNodeA = preorderNodeA
    self._inorderNodeB = inorderNodeB
    self._hash = {}
    for idx, val in enumerate(inorderNodeB):
      self._hash[val] = idx

    count = len(preorderNodeA)
    result = self._recur(0, count-1)
    return result

  def _recur(self, leftIdx: int, rightIdx: int) -> TreeNode:
    if leftIdx > rightIdx:
      return None

    val = self._preorderNodeA[self._preorderIdx]
    centerIdx = self._hash[val]         # 해쉬맵은 O(1), 모든 노드를 순회 하는 재귀함수 O(n), 즉 O(n)
    self._preorderIdx += 1              # 이놈이 함수 바깥에서 preorderNodeA 인덱스를 하나씩 오른쪽으로 이동하면서 매번 첫번째 값을 구하는 것임

    leftResult = self._recur(leftIdx, centerIdx-1)
    rightResult = self._recur(centerIdx+1 ,rightIdx)

    crtNode = TreeNode(val)
    crtNode.left = leftResult
    crtNode.right = rightResult

    return crtNode