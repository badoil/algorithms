# 322
# 문제: 주어진 동전 coins로 금액의 합 amount를 만들기 위한 최소한의 동전의 갯수는 몇개인가?

# 포인트는 배열에 idx원을 만들기 위한 최소한의 동전 갯수가 들어감,
# 점화식 F(n) = min(F(n-coin1), F(n-coin2), F(n-coin3)) + 1
# +1 은 동전 하나가 추가되어야 하니까

# 이 문제는 어떤 경우 그리디로 풀 수 있는데, 이때 로컬 솔루션이 글로벌 솔루션이 되는 조건이어야함
# 하지만 이 문제는 로컬이 글러벌 솔루션이 못 되기에 dp 로 풀어야함

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
  MAX_COST = 999999999
  dp_array = [-1] * (amount+1)
  dp_array[0] = 0
        
  for idx in range(amount+1):
    if dp_array[idx] != -1:
      continue
    
    crnt_min = MAX_COST
    for coin in coins:
      last_idx = idx - coin
      if last_idx < 0:
        continue
      last_cost = dp_array[last_idx]
      if last_cost == -1:
        continue
      cost = last_cost + 1
      crnt_min = min(cost,crnt_min)
      
    dp_array[idx] = -1 if crnt_min==MAX_COST else crnt_min
      
  return dp_array[amount]

print(coinChange(coins=[2,3,5], amount = 10))




##################################################################################
# F(sum) = min(F(sum-coin1), F(sum-coin2), F(sum-coin3)) + 1
# 현재 인덱스 idx원에 대해서 주어진 동전들로 만들 수 있는 최소 갯수를, minCoinCounts의 idx에 업데이트 하면서 진행
# 반복문은 F(sum) = min(F(sum-coin1), F(sum-coin2), F(sum-coin3)) + 1 중에서 min(F(sum-coin1), F(sum-coin2), F(sum-coin3)) 값을 구하는 과정



def minCoinChange(coins: List[int], sum: int) -> int:
  MIN = 999999999
  minCoinCounts = [-1] * (sum+1)    # 이 배열에 idx원을 만들기 위한 최소한의 동전 갯수가 들어감, 주어진 동전들로 sum을 못 구하면 -1 리턴, sum원을 구해야 하기 때문에 마지막 인덱스가 sum이 되는 배열 필요 고로 길이가 sum+1인 배열 필요
  minCoinCounts[0] = 0                  # 인덱스2를 

  for idx in range(sum+1):        # 현재 인덱스 idx원에 대해서 동전들을 프로세싱
    if minCoinCounts[idx] != -1:  # 반복문은 F(sum) = min(F(sum-coin1), F(sum-coin2), F(sum-coin3)) + 1 중에서 min(F(sum-coin1), F(sum-coin2), F(sum-coin3)) 값을 구하는 과정
      continue

    crtMinCount = MIN
    for coin in coins:          
      lastIdx = idx - coin      # 현재의 인덱스가 idx원이기 때문에 해당 코인값을 빼주면 lastIdx원이 됨
      if lastIdx < 0:
        continue

      if minCoinCounts[lastIdx] == -1:    # minCoinCounts[lastIdx]는 lastIdx원을 만드는데 필요한 최소한의 동전 개수, -1이면 lastIdx원을 만드는 방법이 없다는 뜻
        continue
      
      lastCoinCount = minCoinCounts[lastIdx] + 1
      crtMinCount = min(crtMinCount, lastCoinCount)

    if crtMinCount == MIN:       # min(F(n-coin1), F(n-coin2), F(n-coin3)) 값이 없다는 뜻
      minCoinCounts[idx] = -1
    else:
      minCoinCounts[idx] = crtMinCount

  return minCoinCounts[sum]