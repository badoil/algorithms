# 그래프란 vertex, edge 로 이루어진 자료구조
# 문제에서는 vertex가 노드 즉 도시, edge가 길을 나타냄
# 이때 엣지들이 방향성 있거나 없거나, 비용이 있거나 없거나, 싸이클이 있거나 없거나 할 수 있음
# tree는 방향성이 있는 graph의 일종

# 그래프는 배열, 해쉬맵, 2차원 매트릭스 등으로 나타낼 수 있음
# 그 자체로도 많이 나오고 greedy 랑 결합하여 문제가 나옴

# dfs, bfs 는 graph traverse 방법임
# depth first DFS는 stack을 이용하므로 recursive, iterative 둘다 구현 가능
# breadth first BFS는 queue를 이용, 문제에서 보통 가장 짧은 거리를 구할 때 사용
# 이들의 TC O(V+E), SC O(V)

# leecode 841
# 문제 : 각 Room 마다 다른 room을 위한 key들이 준비되어있다. Room 0번에 접근 할 수 있을때 모든 Room에 접근할수있는지 T/F로 return 하여라
# 이 문제는 방향성이 있는 그래프 문제임
# 방이 vertex, 방 열쇠가 edge 임
# 모든 방에 접근 가능한지 물어보는 문제기 때문에 DFS, BFS 둘다 사용 가능

# 여기서는 총 3가지 풀이법, recurDFS, iterDFS, iterBFS 로 풀것임

from typing import List
from collections import deque

class VisitAllRooms:
  def recurDFS(self, rooms: List[List[int]]) -> bool:
    self._rooms = rooms
    self._seen = set()
    
    self._recurDFS(0)   
    
    if len(self._rooms) == len(self._seen):
      return True    
    else:
      return False
  
  def _recurDFS(self, room_idx:int) -> None:
    print(room_idx, end=' ')
    self._seen.add(room_idx)
    keys = self._rooms[room_idx]
    
    for key in keys:
      if key not in self._seen:
        self._recurDFS(key)


  def iterDFS(self, rooms: List[List[int]]) -> bool:
    seen = set()
    stack = []    
    stack.append(0)
    seen.add(0)
    print(0, end=' ')

    while stack:
      room_idx = stack.pop()
      keys = rooms[room_idx]
      for key in keys:
        if key not in seen:
          stack.append(key)
          seen.add(key)
          print(key, end=' ')
          
    if len(rooms) == len(seen):
      return True    
    else:
      return False

  def BFS(self, rooms: List[List[int]]) -> bool:    
    seen = set()
    queue = deque()    
    queue.append(0)
    seen.add(0)
    print(0, end=' ')

    while queue:
      room_idx = queue.popleft()
      keys = rooms[room_idx]
      for key in keys:
        if key not in seen:
          queue.append(key)
          seen.add(key)
          print(key, end=' ')
          
    if len(rooms) == len(seen):
      return True    
    else:
      return False
      

visitAllRooms = VisitAllRooms()


#######################################################################



class KeysToRooms:
  def dfsRecurSolution(self, rooms: List[List[int]]) -> bool:
    self._rooms = rooms
    self._seen = set()
    
    self._recurDfs(0)

    if len(self._rooms) == len(self._seen):
      return True
    else:
      return False

  def _recurDfs(self, roomIdx: int) -> None:    # 재귀함수인데 종료조건이 없는 이유는 주어진 문제가 포문이라는 유한한 갯수에 대해서 돌아가고 있기 때문임. 언젠간 알아서 끝남
    self._seen.add(roomIdx)                     # self._seen의 값이 최종 구하고자 하는 값
    roomKeys = self._rooms[roomIdx]

    for key in roomKeys:
      if key not in self._seen:
        self._recurDfs(key)


  
  def iterDfsSolution(self, rooms: List[List[int]]) -> bool:
    seen = set()
    stack = []

    stack.append(0)
    seen.add(0)
    while stack:                      # 포인트는 현재 스택에서 팝한 값을 대상으로 프로세싱하고 그 프로세싱한 값들을 스택에 넣는것, 
      roomIdx = stack.pop()           # 프로세스 진행하면 이 팝 때문에 스택이 결국 비게되는 것임
      roomKeys = rooms[roomIdx]
      for key in roomKeys:
        if key not in seen:
          seen.add(key)               # 구하고자 하는 최종값
          stack.append(key)

    if len(rooms) == len(seen):
      return True
    else:
      return False


  def iterBfsSolution(self, rooms: List[List[int]]) -> bool:
    seen = set()
    q = deque()

    q.append(0)
    seen.add(0)
    while q:                          # 포인트는 현재 큐에서 팝한 값을 대상으로 프로세싱하고 그 프로세싱한 값들을 큐에 넣는것, 
      roomIdx = q.popleft()           # 프로세스 진행하면 이 팝 때문에 큐가 결국 비게되는 것임
      roomKeys = rooms[roomIdx]
      for key in roomKeys:
        if key not in seen:
          seen.add(key)               # 구하고자 하는 최종값
          q.append(key)
          

    if len(rooms) == len(seen):
      return True
    else:
      return False