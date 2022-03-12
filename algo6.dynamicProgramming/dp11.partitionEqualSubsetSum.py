# 416
# 문제: 양의 정수만으로 이루어진 숫자들을 합이 같은 두 subset으로 분류가 가능한지 판별하여라. 
# 분류 가능 or 불가능을 boolean 으로 리턴
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
# 두 서브셋 각각은 totalSum/2의 값을 가지게 될 것
# 어떤 서브셋이 s = totalSum/2 값을 가지는지만 체크하면 됨
# 포인트는 각 원소들을 뽑는 경우와 뽑지 않는 경우로 나뉜다는 것. 이전 냅색 문제와 동일한 구조
# 이 때문에 브루트포스는 2의 n제곱 시간복잡도인데, dp 로 풀면 개선 가능

# [2, 1, 2, 3, 4] 의 경우 총합은 12이므로 그 반값인 6을 총합으로 가지는 서브어레이 찾는 문제로 볼 수 있음
# [2, 1, 2, 3, 4], 6 은 배열의 마지막 수 4에 대해서 [2, 1, 2, 3], 2와 [2, 1, 2, 3], 6 으로 나뉨
# 즉 4를 뽑는 경우와 그렇지 않는 경우임
# 이를 반복하면 합인 6이 0이 되는 지점에서 멈추고 그것이 해당 배열이 totalSum/2을 가지는 서브어레이가 존재한다는 뜻임
# 이렇게 이를 점화식으로 dp(nums, sum) = dp(nums-1, sum-nums[n]) or dp(nums-1, sum)
# 이를 디피테이블로 나타내면
# 
# dp(nums, sum) = dp(nums-1, sum-nums[n]) or dp(nums-1, sum) 이때 dp(rowIdx = nums, colIdx = sum)
# dpTable, 세로축이 nums 수들, 가로축이 sum 합계, 해당값은 boolean
#           0   1   2   3   4   5   6
# 0     ''  T   F   F   F   F   F   F
# 1      2  T   F   T   F   F   F   F
# 2     21  T   T   T   T   F   F   F
# 3    212  T   T   T   T   T   T   F
# 4   2123  T   T   T   T   T   T   T
# 5  21234  T   T   T   T   T   T   T

# dpTable(5, 6) 이 구하고자 하는 값

# 시간 복잡도와 공간복잡도 O(n*s), n은 주어진 정수집합이고 s는 totalSum/2



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
    crtNum = nums[prevIdx]   # 헷갈릴수 있는데, 현재 디피테이블은 0 row에 '' 빈값이다. 따라서 현재수를 지정하려면 rowIdx - 1 해줘야함

    for colIdx in range(1, len(dpTable[rowIdx])+1):
      noChoiceValue = dpTable[prevIdx][colIdx]
      lastColIdx = colIdx - crtNum      

      choiceValue = False
      if lastColIdx >= 0:
        choiceValue = dpTable[prevIdx][lastColIdx]

      dpTable[rowIdx][colIdx] = choiceValue or noChoiceValue

  return dpTable[-1][-1]
