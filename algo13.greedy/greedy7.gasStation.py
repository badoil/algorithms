from typing import List

def gasStation(gases: List[int], costs: List[int]) -> int:
  totalGas = 0

  for idx, gas in enumerate(gases):
    cost = cost[idx]
    diff = gas - cost

    totalGas += diff

  if totalGas < 0:
    return -1

  
  startIdx = 0
  totalGas = 0
  for idx, gas in enumerate(gases):
    cost = costs[idx]
    diff = gas - cost
    totalGas += diff
    if totalGas < 0:
      totalGas = 0
      startIdx = idx + 1
  return startIdx

  #########################################
  # 먼저 총 가스양이 비용보다 크거나 같은지 확인해야함, 만약 총 가스양이 총비용보다 적으면 어디서 출발해도 완주못함. 그 다음에 idx를 찾아야함
  # 그리고 총 가스량이 비용보다 크거나 같으면 무조건 해답이 있는 셈이고, 반복문에서 배열은 선형이고 문제의 경로는 사이클이지만
  # 사이클을 안 돌려도 totalGas < 0 이 되지 않는 즉 totalGas >= 0 이 되서 반복문이끝나고 남는 startIdx 가 정답임

def gasStations(gases: List[int], costs: List[int]) -> int:
  totalGas = sum(gases)
  totalCost = sum(costs)

  if totalGas < totalCost:
    return -1

  
  totalGas = 0
  startIdx = 0
  for idx, gas in enumerate(gases):
    cost = costs[idx]
    diff = gas - cost
    totalGas += diff
    if totalGas < 0:
      startIdx = idx + 1
      totalCost = 0

  return startIdx
