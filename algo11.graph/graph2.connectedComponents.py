

from typing import List

def countComponents(n: int, edges: List[List[int]]) -> int:
  vertices = [[] for _ in range(n)]
  
  #build a graph
  for edge in edges:
    v0, v1 = edge
    vertices[v0].append(v1)
    vertices[v1].append(v0)
  
  #Process
  visited = set()   
  comp_count = 0
  for idx in range(n):
    if idx not in visited:
      comp_count = comp_count + 1
              
      #DFS
      seen = set()
      stack = [idx]
      seen.add(idx)
      
      while stack:        
        crnt_idx = stack.pop()
        visited.add(crnt_idx)
        next_vertices = vertices[crnt_idx]
        for next_idx in next_vertices:
          if next_idx not in seen:
            seen.add(next_idx)
            stack.append(next_idx)
                  
        
  return comp_count


################################################################
# 323
# 문제 : 주어진 graph의 Connected Components의 갯수를 구하여라. 여기서 graph는 vertex의 갯수와 edge로만 주어진다
# TC O(V+E), SC O(V)
# 이 문제는 주어진 vertex의 갯수 num과 edges를 이용해서 먼저, 연결 그래프를 만들어야함.

def countConnectedComponents(num: int, edges: List[List[int]]) -> int:      # 버텍스의 갯수 num, 연결 정보 edges
  matrix = [[] for _ in range(num)]       # 제대로된 그래프 정보는 2차원 매트릭스로 표현됨, 각 배열에 그 배열의 인덱스 버텍스가 연결되고 있는 버텍스 넘버 정보 가짐
  
  for edge in edges:            # 연결정보 이용해서 그래프 생성
    vStart, vEnd = edge
    matrix[vStart].append(vEnd)
    matrix[vEnd].append[vStart]

  visited = set()                     # visited는 덩어리(component) 체크용
  componentCount = 0
  for idx in range(num):              # 해당 버텍스에 대해 모든 연결 노드를 방문해야함
    if idx not in visited:
      componentCount += 1             # visited 에 없다는 뜻은 새로운 덩어리(component)라는 뜻임
      
      seen = set()                    # seen은 해당 노드의 연결노드 체크용, 아래처럼 없어도 무방
      seen.add(idx)
      stack = []
      stack.append(idx)
      while stack:                        # 해당 노드의 연결노드 모두 방문하면 그 노드들이 한 덩어리(component)라고 볼 수 있음.
        crtIdx = stack.pop()
        visited.add(crtIdx)               # 이 방문한 노드를 기록하면 그 노드들을 포문에서 체크할 필요 없음
        connectedNodes = matrix[crtIdx]
        for node in connectedNodes:
          if node not in seen:
            seen.add(node)
            stack.append(node)

  return  componentCount


# 아래처럼 seen = set() 을 없애도 무방함

def countComponentsV2(num: int, edges: List[List[int]]) -> int:      # 버텍스의 갯수 num, 연결 정보 edges
  matrix = [[] for _ in range(num)]       # 제대로된 그래프 정보는 2차원 매트릭스로 표현됨, 각 배열에 그 배열의 인덱스 버텍스가 연결되고 있는 버텍스 넘버 정보 가짐
  
  for edge in edges:            # 연결정보 이용해서 그래프 생성
    vStart, vEnd = edge
    matrix[vStart].append(vEnd)
    matrix[vEnd].append[vStart]

  visited = set()                     # visited는 덩어리(component) 체크용
  componentCount = 0
  for idx in range(num):              # 해당 버텍스에 대해 모든 연결 노드를 방문해야함
    if idx not in visited:
      componentCount += 1             # visited 에 없다는 뜻은 새로운 덩어리(component)라는 뜻임
      

      stack = []
      stack.append(idx)
      while stack:                        # 해당 노드의 연결노드 모두 방문하면 그 노드들이 한 덩어리(component)라고 볼 수 있음.
        crtIdx = stack.pop()
        visited.add(crtIdx)               # 이 방문한 노드를 기록하면 그 노드들을 포문에서 체크할 필요 없음
        connectedNodes = matrix[crtIdx]
        for node in connectedNodes:
          if node not in visited:
            stack.append(node)

  return  componentCount





################################################################
# 200 나중에 풀어보자