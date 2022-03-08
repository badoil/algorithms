# 134
# 문제 : 주유소와 길에 대한 Array들이 주어진다. Gas[i]는 i번째 주유소에서 채울수있는 기름의 양이고, cost[i]는 i번째 주유소에서 i+1번째 주유소까지 가는데 필요한 기름의 양이다.
# 기름이 빈 차량에서 몇번째 주유소에서 출발해야, 시계방향으로 한바퀴 돌수있는지 return 하여라. 만약 불가능하다면 -1를 return 하여라.

# 브루트 포스로 풀면 매 출발지마다 싸이믈을 돌리기 때문에 O(n^2)
# 그런데 첫번째에서 출발해서 세번째까지 가고 실패라면 3번째 부터 탐색하면 된다는 것이 포인트
# 왜냐하면 두번째는 첫번째에서 출발할때 보다 기름의 양이 적을 것이기 때문(세번째도 마찬가지)
# 그러면 O(n) 으로 풀 수 있음


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

  # 총 가스양이 마지막으로 음수가 나오는 바로 다음 인덱스가, 한 사이클 완주할 수 있는 출발 인덱스임
  # 왜냐면 totalGas >= totalCost 가 보장된다면, 위의 인덱스가 충분한 양의 가스를 가지고 있는 것으로 볼 수 있기 때문

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
      totalGas = 0

  return startIdx
