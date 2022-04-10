# 543
# *주어진* tree의 Diameter를 구하여라
# 노드 사이의 최대 거리(Diameter)를 구하는 문제
# 최대 길이를 구하기 위해서 꼭 루트 노드를 거칠 필요는 없다
# 루트노드를 거칠 필요가 없기 때문에 postOrder

# 리프 노드 간의 거리가 최대 길이가 된다는 것이 직관적으로 확실
# pre, in, post order 중에 postOrder 사용
# 이때 어떤 해당 노드의 left child 들의 뎁스와 right child 들의 뎁스를 합한 값이, 해당 노드의 max diameter
# 그리고 이 해당 노드의 부모 노드에는 이 둘의 뎁스 값 중에 큰 값(max(left child depth, right child depth)) + 1(부모에서 자신까지의 뎁스) 을 해준 값을 전달 -> 이 값이 부모 노드에서의 뎁스
# 즉 뎁스를 구하면 max diameter를 구할 수 있음

# recursive postOrder
# 결국 반복적으로 뎁스를 구하면서 max diameter 갱신해 주면 됨
# 재귀를 사용하면 리프까지 스택이 쌓이고 이 거기서부터 max diameter 갱신해주고 뎁스를 리턴하며 스택을 팝.
# 이를 반복하면  max diameter 구해짐

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

class Diameter:
  def solution(self, root: TreeNode) -> int:
    if root is None:
      return 0

    self._maxDiameter = 0
    self._recursiveDiameter(root)
    return self._maxDiameter
    

  def _recursiveDiameter(self, node: TreeNode):    # 재귀는 항상 스택의 마지막부터 생각해야함. 거기서 부터 스택을 팝하면서 반복적을 생각해야함
    leftDepth = 0
    rightDepth = 0

    if node.left:
      leftDepth = self._recursiveDiameter(node.left)
    if node.right:
      rightDepth = self._recursiveDiameter(node.right)

    crtDiameter = leftDepth + rightDepth                      # 이때 어떤 해당 노드의 left child 들의 뎁스와 right child 들의 뎁스를 합한 값이, 해당 노드의 max diameter
    self._maxDiameter = max(self._maxDiameter, crtDiameter)   # max diameter 를 갱신

    crtDepth = max(leftDepth, rightDepth)  # 이 해당 노드의 부모 노드에는 이 둘의 뎁스 값 중에 큰 값(max(left child depth, right child depth)) + 1(부모에서 자신까지의 뎁스) 을 해준 값을 전달 -> 이 값이 부모 노드에서의 뎁스
    return crtDepth + 1
    