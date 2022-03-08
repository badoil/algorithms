# 1029
# 이 문제는 솔직히 문제 자체가 이해안되는 구린 문제지만 일단 풀이는 간단함.


from typing import List

def twoCity(costs: List[List[int]]) -> int:
  costs.sort(key=lambda x:x[1]-x[0], reverse=True)

  length = len(costs)
  halfCount = int(length/2)
  totalCost = 0
  
  for idx in range(0, halfCount):
    totalCost += costs[idx][0]

  for idx in range(halfCount, length):
    totalCost += costs[idx][1]

  return totalCost



  ################################
