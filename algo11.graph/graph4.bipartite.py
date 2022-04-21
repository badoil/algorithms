# 785
# 문제 : 주어진 graph가 bipartite인지 체크하여라
# bipartite란 그래프의 모든 노드가 두개의 파티션으로 나눠진다는 뜻
# 즉 연결되있는 모든 노드들이 서로 상반되는 색깔이면 bipartite 한 것임
# DFS, BFS 이용해서 인접한 노드들이 다른 색인지, 모든 노드에대해서 체크해주면 됨
# 여기서는 구현이 쉬운 DFS로 했음
# TC O(V+E), SC O(V)

# 응용문제로는 기어(톱니바퀴) 문제가 있음, 주어진 톱니바퀴들이 잘 맞물려서 돌아가냐 아니냐 뭐 이런 문제


from platform import node
from typing import List

def isBipartiteDFS(graph: List[List[int]]) -> bool:
  vertex_num = len(graph)
  colors = [0] * vertex_num       #0:None, 1:GroupA, -1:GroupB 
  seen = set()
      
  for start_idx in range(vertex_num):
    if start_idx in seen:
      continue
    
    stack = []
    stack.append(start_idx)
    seen.add(start_idx)
    colors[start_idx] = 1
    
    while stack:
      idx = stack.pop()
      conn_idxs = graph[idx]
      color = colors[idx]

      for conn_idx in conn_idxs:
        if conn_idx not in seen:
          seen.add(conn_idx)
          stack.append(conn_idx)
          colors[conn_idx] = -1 * color
          continue

        if colors[conn_idx] * color != -1:
          return False
      
  return True

print(isBipartiteDFS([[1,3],[0,2],[1,3],[0,2]]))
print(isBipartiteDFS([[1,2,3],[0,2],[0,1,3],[0,2]]))


#################################################################

def bipartiteDfs(graph: List[List[int]]) -> bool:
  vertexCount = len(graph)
  if vertexCount == 0:
    return False

  colors = [0] * vertexCount
  seen = set()                          # 여기서 포문 시작하기 전에 스택, 컬러, 신 모두 초기값 할당하고 포문을 두번째 부터 돌려도 될 것임

  for nodeIdx in range(vertexCount):
    if nodeIdx in seen:
      continue

    stack = []
    stack.append(nodeIdx)
    seen.add(nodeIdx)
    colors[nodeIdx] = 1


    while stack:
      vertex = stack.pop()
      connectedVertex = graph[vertex]
      for conVertex in connectedVertex:
        if conVertex not in seen:
          stack.append(conVertex)
          seen.add(conVertex)
          colors[conVertex] = -1 * colors[vertex]
          continue    # seen 에 없으면 color 도 없기 때문에 다음 조건문을 확인할 필요 없이, 다음 순번으로 포문 이동

        if colors[conVertex] == colors[vertex]:
          return False

    return True
        