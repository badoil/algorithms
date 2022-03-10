# 64
# 문제: 2d array로 길을 가기 위한 비용이 주어진다. 왼쪽 위에서 오른족 아래까지 도달하기 위한 최소 비용은 얼마인가?
# 최초 위치는 (0, 0), 진행방향은 아래 또는 오른쪽 뿐. 즉 (0, 0) -> (m, n)
# 시간복잡도 O(m*n), 공간복잡도 O(m*n) -> O(1) 최적화 가능, i라는 row의 최소비용을 구하기 위해서 i행, i-1행이라는 두 줄만 필요하기 때문 
# 점화식 minCost(rowIdx, colIdx) = cost(rowIdx, colIdx) + min(cost(rowIdx-1, colIdx), cost(rowIdx, colIdx-1))

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    minCost2d = a = [[0] * cols for i in range(rows)]
    
    #initialize 2d cost map
    minCost2d[0][0] = grid[0][0]
    for colIdx in range(1,cols):
      minCost2d[0][colIdx] = grid[0][colIdx] + minCost2d[0][colIdx-1]
    for rowIdx in range(1,rows):
      minCost2d[rowIdx][0] = grid[rowIdx][0] + minCost2d[rowIdx-1][0]
    
    #bottom up DP
    for rowIdx in range (1,rows):
      for colIdx in range (1,cols):
        prevCol = colIdx - 1
        prevRow = rowIdx - 1
        
        upCost = 0 if (prevRow < 0) else minCost2d[prevRow][colIdx]       # 포문의 범위가 1부터 시작하기에 0 이하로 내려갈 일이 없음, 불필요
        leftCost = 0 if (prevCol < 0 ) else minCost2d[rowIdx][prevCol]
        
        prevCost = min(upCost,leftCost)
        cost = prevCost + grid[rowIdx][colIdx]        
        minCost2d[rowIdx][colIdx] = cost
                
    minCost = minCost2d[rows-1][cols-1]    
    return minCost


grid = [[1,3,1,2],[2,4,5,2],[3,4,5,6],[1,5,6,2]]
print('minCost=',minPathSum(grid=grid))

minCost= 17




#########################################################################
# 점화식 minCost(rowIdx, colIdx) = cost(rowIdx, colIdx) + min(cost(rowIdx-1, colIdx), cost(rowIdx, colIdx-1))




def twoDimensionMinCostPath(costs: List[List[int]]) -> int:
  rowCount = len(costs)
  colCount = len(costs[0])

  minCosts = [[0] * colCount for i in range(rowCount)]
  minCosts[0][0] = costs[0][0]

  for i in range(1, colCount):                          # 점화식에 의하면 첫 행과 첫 열을 초기화해야함, 해당 수의 바로 왼쪽과 바로 위쪽의 최소값을 구해야 하기 때문에,
    minCosts[0][i] = minCosts[0][i-1] + costs[0][i]     # 초기화 안하면 colIdx < 0 or rowIdx < 0 될 수 있음
  for i in range(1, rowCount):
    minCosts[i][0] = minCosts[i-1][0] + costs[i][0]


  for rowIdx in range(1, rowCount):                     # 노코프 코드보다 걍 줄였음
    for colIdx in range(1, colCount):
      minCost = min(minCosts[rowIdx-1][colIdx], minCosts[rowIdx][colIdx-1])
      minCosts[rowIdx][colIdx] = costs[rowIdx][colIdx] + minCost

  return minCosts[rowCount-1][colCount-1]

