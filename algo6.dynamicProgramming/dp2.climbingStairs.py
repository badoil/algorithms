# 70
# 문제: n개의 계단을 오르고자 한다. 한번에 1개 또는 2개씩의 계단을 오를수 있을때 총 몇가지 방벙으로 계단을 오를 수 있는가?

# F(0) = 0, F(1) = 1, F(2) = 2

from typing import List

dpArray = [0, 1, 2]
def topDownclimbingStairs(num: int) -> int:
  if num == 0:
    return 0
  elif num == 1:
    return 1
  elif num == 2:
    return 2

  fibo = topDownclimbingStairs(num-2) + topDownclimbingStairs(num-1)
  return fibo

def bottomUpClimbingStairs(num: int):
  dpArray = [0, 1, 2]

  if len(dpArray) > num:
    return dpArray[num]

  for i in range(3, num+1):
    fibo = dpArray[i-2] + dpArray[i-1]
    dpArray.append(fibo)

  return dpArray[num]


# 746
# 문제: i번째 계단을 오르는 비용이 cost[i]로 주어졌다. 계단을 한번에 한칸 혹은 두칸씩만 오를수 있을때, 전체 계단을 오르는 최소 비용은 얼마인가.
def minCostStairs(cost: List[int]) -> int:
    total_count = len(cost)
    min_cost = [0] * (total_count + 1)
    
    for i in range(2, total_count + 1):
      one_step = min_cost[i - 1] + cost[i - 1]
      two_step = min_cost[i - 2] + cost[i - 2]
      min_cost[i] = min(one_step, two_step)

    return min_cost[total_count]

stair_cost = [1,2,4,6,2,4,6,1]
print(minCostStairs(cost=stair_cost))

###############################################################
# 점화식 fibo = min((costs[i-2]+minCo[i-2]), (costs[i-1]+minCo[i-1]))
# 점화식은 그림을 그리면서 규칙성을 찾는 수 밖에 없음

# costs = [1,2,4,6,2,4,6,1]
# minCo = [0,0,1,2,5,7,7,11,12]

def bottomUpclimbingStairsByCost(costs: List[int]) -> int:
  count = len(costs)
  minimumCosts = [0] * (count+1)

  for i in range(2, count+1):
    fibo = min((costs[i-2]+minimumCosts[i-2]), (costs[i-1]+minimumCosts[i-1]))
    minimumCosts[i] = fibo

  return minimumCosts[-1]

