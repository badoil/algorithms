# 문제 : 주어진 DAG(Directed Acyclic Graph)를 Topological Order로 출력하여라
# TC O(V+E), SC O(V)

# Topological Order란 DAG(directed acyclic graph)를 linear 하게 표현
# 이는 dependency 가 없는 버텍스를 먼저 쓰고, 엣지의 방향들이 마지막을 가리키는 버텍스를 끝에 쓴다

# indegree: 해당 버텍스에 들어오는 엣지의 갯수, 이를 알기위해서 각 버텍스 갯수만큼의 배열을 만들고 각 인덱스(버텍스 해당)마다 엣지가 향하는 배열의 인덱스에 기입해주면 됨
# 이때 indegree 값이 0인 인덱스가 그 그래프의 처음
# outdegree: 해당 버텍스에 나가는 엣지의 갯수

# indegree 어레이를 만들어놓고 이를 기준으로 0인 인덱스를 deque에 넣어주고 이 deque을 레프트 팝한 버텍스의 엣지를 indegree 어레이 인덱스 값에서 -1 하면서 업뎃하고
# 여기서 값이 0인 애를  deque에 넣어주고 위의 동작을 반복
# 이때 레프트팝한 값들을 리턴

# 응용문제로 leetcode 269 alien dictionary 같은 유형의 문제, 함 풀어보라


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



###################################################################3



def topologicalOrderBfs(graph: List[List[int]]) -> List[int]:
  indegree = [0] * len(graph)
  
  for vertex in range(len(graph)):
    edges = graph[vertex]
    for edge in edges:
      indegree[edge] += 1
      

  indeg = deque()
  for idx in range(len(indegree)):
    if indegree[idx] == 0:
      indeg.append(idx)

  results = []

  while indeg:
    vertex = indeg.popleft
    results.append(vertex)
    
    connVertex = graph[vertex]
    for idx in connVertex:
      indegree[idx] -= 1
      if indegree[idx] == 0:
        indeg.append(idx)

  return results
