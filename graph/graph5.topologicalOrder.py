# leetcode 269 alien dictionary 같은 유형의 문제, 함 풀어보라

from typing import List
from collections import deque

def topologicalOrder(graph: List[List[int]]) -> List[int]:
  vertex_num = len(graph)
  indegs = [0]* vertex_num
  for vertex in graph:
    for to_idx in vertex:
      indegs[to_idx] += 1 
  
  deg0s = deque()

  for idx,in_deg in enumerate(indegs):
    if in_deg == 0:
      deg0s.append(idx)

  topo_order = []

  while deg0s:
    vtx0indeg = deg0s.popleft()
    topo_order.append(vtx0indeg)
    vertex = graph[vtx0indeg]
    for to_idx in vertex:
      indegs[to_idx] -= 1 
      if indegs[to_idx]==0:
        deg0s.append(to_idx)

  return topo_order

graph = [[1,3],[2,5],[],[2],[1],[]]
print(topologicalOrder(graph))

########################################

def topologicalOrder(graph: List[List[int]]) -> List:
  vortexNum = len(graph)
  indegree = [0] * vortexNum

  #
  for idx in range(vortexNum):
    toIdxs = graph[idx]
    for toIdx in toIdxs:
      indegree[toIdx] = indegree[idx]+1

  # deque에 넣기
  queue = deque()
  for idx in range(vortexNum):
    if indegree[idx] == 0:
      queue.append(idx)

  orderArr = []

  # process

  while queue:
    vortex = queue.popleft()
    orderArr.append(vortex)
    toIdxs = graph[vortex]
    for toIdx in toIdxs:
      indegree[toIdx] -= 1
      if indegree[toIdx] == 0:
        queue.append(toIdx)

  return orderArr