# 113
# Tree 의 root로 부터 leaf까지의 sum이 targetSum이 되는 모든 path를 찾아서 return하여라
# 백트래킹으로 풀 수 있음, preorder로 모든 노드를 순회하면서 백트래킹
# 각 노드들의 연결을 모든 가능성 공간으로 보는 것임



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


class pathSum:
  def getPathes(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    if root is None:
      return []
    
    self._retList = []
    self._recurPathSum(root,targetSum,[]) 
  
    return self._retList
  
  def _recurPathSum(self, node:TreeNode, targetSum: int, crntList: List[int]):
    if node.left is None and node.right is None:
      if node.val == targetSum:
        crntList.append(node.val)
        self._retList.append(crntList.copy())
        crntList.pop()
      return
    
    
    newTargetSum = targetSum - node.val
    if node.left:
      crntList.append(node.val)
      self._recurPathSum(node.left,newTargetSum,crntList)
      crntList.pop()
    if node.right:
      crntList.append(node.val)
      self._recurPathSum(node.right,newTargetSum,crntList)
      crntList.pop()    
    return

pathSum = pathSum()
pathSum.getPathes(root,20)


###############################################################################

class SumPath:
  def solution(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    if root is None:
      return []

    self._results = []
    self._backTrackingPathSum(root, targetSum, [])
    return self._results
    

  def _backTrackingPathSum(self, node: TreeNode, partialSum: int, crtArray: List[int]):
    if node.val == partialSum:
      crtArray.append(node.val)
      self._results.append(crtArray.copy())   
      crtArray.pop()
      return 

    sum = partialSum - node.val

    if node.left:
      crtArray.append(node.val)
      self._backTrackingPathSum(node.left, sum, crtArray)
      crtArray.pop()      # 해당 노드는 루트 노드이기 때문에 재귀함수 호출 후에 그 루트노드를 팝해서 삭제해야함. 

    if node.right:
      crtArray.append(node.val)
      self._backTrackingPathSum(node.right, sum, crtArray)
      crtArray.pop()

    return          # 만약 노드 끝까지 갔는데 node.val == partialSum 이 아니라면 여기서 재귀호출을 리턴해야 그 전으로 돌아감