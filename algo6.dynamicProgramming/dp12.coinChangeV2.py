# 518
# 문제: coins에 들어있는 종류의 갯수가 무제한 있을때, amount를 만들수있는 조합의 갯수를 구하여라

# 냅색 문제의 일종
# 이런 dp 문제를 푸는것은, 공식을 외우는 것도 중요하지만 제대로 상위문제와 하위문제를 나누는 것이 제일 중요
# DP(n, s) = DP(n-1, s) + DP(n, s-coin)
# 경우의 수를 구하는 것이기 때문에 두 하위 문제의 솔루션을 더해준 것이 상위문제의 해답임
# 한 코인이 선택 안받은 경우 해당 코인을 제외하고 s는 그대로, 선택받은 경우 코인이 무제한이기때문에 그 코인 포함해서 남아있고 만들어야할 금액은 s-coin

from typing import List

def coinChange(amount: int, coins: List[int]) -> int:
  dp_table = [[0]*(amount+1) for j in range(len(coins)+1)]
  
  for rowIdx in range(len(dp_table)):
    dp_table[rowIdx][0] = 1
    
  for rowIdx in range(1,len(dp_table)):
    coin = coins[rowIdx-1]
    prev_row = rowIdx - 1
    for colIdx in range(1,len(dp_table[rowIdx])):
      dp0 = 0
      prev_col = colIdx-coin
      if 0 <= prev_col:
        dp0 = dp_table[rowIdx][prev_col]
      dp1 = dp_table[prev_row][colIdx]

      dp = dp0 + dp1
      dp_table[rowIdx][colIdx] = dp
  
  return dp_table[-1][-1]  #return last dp table elem 


#############################################################



def coinChangeV2(nums: List[int], target: int) -> int:
  coinCount = len(nums)
  dpTable = [[0]*(target+1) for _ in range(coinCount+1)]

  for rowIdx in range(len(dpTable)):
    dpTable[rowIdx][0] = 1

  for rowIdx in range(1, len(dpTable)):
    for colIdx in range(1, len(dpTable[rowIdx])):
      prevIdx = rowIdx - 1
      crtNum = nums[prevIdx]

      noChoiceValue = dpTable[prevIdx][colIdx]

      choiceValue = 0
      remainAmount = colIdx - crtNum
      if remainAmount >= 0:
        choiceValue = dpTable[rowIdx][remainAmount]        # 동전이 무제한이기 때문에 동전을 선택했으면 동전이 남아 있다. 그래서 rowIdx-1 이 아니라 rowIdx

      dpTable[rowIdx][colIdx] = noChoiceValue + choiceValue

  return dpTable[-1][-1]

print(coinChangeV2(nums=[1,2,3], target=5))