# 1091
# 문제 : 주어진 graph의 왼쪽 위 에서 아랫쪽 끝까지의 shortest path의 길이를 return 하여라. path는 matrix cell의 8방향으로 이어져 있다.
# TC O(V+E), SC O(V)
# 여기서 조금 더 나가면 다익스트라 알고리즘

# 어레이 문제 같지만 2차원 매트릭스의 셀들을 베텍스로 보고 사방으로 연결되어 있다고 보면 그래프 문제가 된다
# 2차원 매트릭스 형태의 길찾기 문제는 그래프로 해결하면 된다는 것
# 최단거리 구하기니까 BFS
# 문제 풀이의 포인튼는 현재 위치에서 갈 수 있는 8방향의 위치에 해당하는 거리를 써주면서 단계를 진행하는것
# 모든 좌표에 그 거리를 적었다면 매트릭스의 맨 오른쪽 아래의 좌표에 적힌 거리 값이 해답

from typing import List
from collections import deque

class ShortestPath:
  def BFS(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    if rows == 0:
      return -1
    
    cols = len(grid[0])
    if cols == 0:
      return -1
    
    if grid[0][0] != 0:
      return -1
    
    self._rows = rows
    self._cols = cols
    self._grid = grid
    
    queue = deque()
    countQ = deque()
    seen = set()
    queue.append((0,0))
    countQ.append(1)
    seen.add((0,0))
    
    while queue:
      y, x = queue.popleft()
      count = countQ.popleft()
      self._grid[y][x] = count
      
      if y == self._rows-1 and x == self._cols-1:
        return count
      
      idx_pairs = [[y-1,x-1],[y-1,x],[y-1,x+1],[y,x+1],[y+1,x+1],[y+1,x],[y+1,x-1],[y,x-1]] #index candidates
      idx_pairs = list(filter(self._filter, idx_pairs)) #filtering
      
      for idx_pair in idx_pairs:
        next_y, next_x = idx_pair
        if (next_y, next_x) not in seen:
          queue.append((next_y, next_x))
          countQ.append(count+1)
          seen.add((next_y, next_x))
          
    return -1
          
          
  def _filter(self, idx2d ) -> bool:
    y, x = idx2d
    if y<0 or x<0 or self._rows<=y or self._cols<= x:
      return False    
    elif self._grid[y][x] == 0:
      return True
    return False
      
      
stp = ShortestPath()

matrix = [[0,1,0,0,0],[0,1,0,0,0],[1,0,0,1,0],[0,0,1,1,0]]

print(stp.BFS(matrix))



##################################################################


class ShotestPathBFS:
  def solution(self, matrix: List[List[int]]) -> int:
    row = len(matrix)
    col = len(matrix[0])
    if row == 0:
      return -1
    if col == 0:
      return -1
    if matrix[0][0] == 1:
      return -1


    positionQ = deque()
    countQ = deque()
    seen = set()
    self._row = row
    self._col = col
    self._matrix = matrix

    positonQ.append((0,0))
    countQ.append(1)
    seen.add((0,0))


    while positionQ:
      y, x = positionQ.popleft()     # 현재 좌표
      count = countQ.popleft()      # 현재 좌표까지의 거리
      self._matrix[y][x] = count    # 그 거리를 매트릭스에 적어준다

      if y==self._row-1 and x==self._col-1: # 현재 위치가 매트릭스의 맨 오른쪽 아래라면 그 값을 리턴하고 종료
        return self._matrix[y][x]

      nextPositions = [[y,x-1], [y+1, x-1], [y+1, x], [y+1, x+1], [y, x+1], [y-1, x+1], [y-1, x], [y-1, x-1]]   # 8방향 좌표들
      filteredNextPositions = list(filter(self._filter, nextPositions))    # 매트릭스 범위 안에 있는 필터링된 좌표들

      for filteredNextPosition in filteredNextPositions:
        y, x = filteredNextPosition
        if (y, x) not in seen:
          seen.add((y, x))          # 현재 좌표의 다음 좌표를 처리
          positionQ.append((y, x))
          countQ.append(count+1)

    return -1


  def _filter(self, nextPosition):
    y, x = nextPosition
    if y < 0 or x<0 or y>=self._row or x>=self._col:
      return False
    elif self._matrix[y][x]==0:
      return True
    return False