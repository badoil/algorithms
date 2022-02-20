# 416
# 문제: 양의 정수만으로 이루어진 숫자들을 합이 같은 두 subset으로 분류가 가능한지 판별하여라. 
# positive integer

# 두 서브셋 각각은 totalSum/2의 값을 가지게 될 것
# 어떤 서브셋이 s = totalSum/2 값을 가지는지만 체크하면 됨
# 포인트는 각 원소들을 뽑는 경우와 뽑지 않는 경우로 나뉜다는 것. 이전 냅색 문제와 동일한 구조
# 이 때문에 브루트포스는 2의 n제곱 시간복잡도인데, dp 로 풀면 개선 가능

# 시간 복잡도와 공간복잡도 O(n*s), n은 주어진 정수집합이고 s는 totalSum/2

from typing import List

def canPartition( nums: List[int]) -> bool:
  total = sum(nums)
  if total % 2 == 1:
    return False
  
  half_sum = int(total/2)
  
  dp_table = [[False]*(half_sum+1) for j in range(len(nums)+1)]
  
  for rowIdx in range(len(dp_table)):
    dp_table[rowIdx][0] = True
    
  for rowIdx in range(1,len(dp_table)):
    nth_num = nums[rowIdx-1]
    prev_row = rowIdx - 1
    for colIdx in range(1,len(dp_table[rowIdx])):
      dp0 = False
      prev_col = colIdx-nth_num
      if 0 <= prev_col:
        dp0 = dp_table[prev_row][prev_col]
      dp1 = dp_table[prev_row][colIdx]
      
      dp = dp0 or dp1
      dp_table[rowIdx][colIdx] = dp
      
      
  return dp_table[-1][-1]  #return last dp table elem

print(canPartition(nums=[2,1,2,3,4]))


######################################################################



def equalSubSetSum(nums: List[int]) -> bool:
  total = sum(nums)
  if total%2 == 1:
    return False

  halfSum = total/2
  dpTable = [[False for _ in range(halfSum+1)] for _ in range(len(nums)+1)]

  for rowIdx in range(len(dpTable)):
    dpTable[rowIdx][0] = True

  for rowIdx in range(1, len(dpTable)+1):
    prevIdx = rowIdx - 1
    crtNum = nums[prevIdx]

    for colIdx in range(1, len(dpTable[rowIdx])+1):
      noChoiceValue = dpTable[prevIdx][colIdx]
      lastColIdx = colIdx - crtNum

      choiceValue = False
      if lastColIdx >= 0:
        choiceValue = dpTable[prevIdx][lastColIdx]

      dpTable[rowIdx][colIdx] = choiceValue or noChoiceValue

  return dpTable[-1][-1]
