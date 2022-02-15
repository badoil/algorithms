# 974 비슷한 문제

# 문제: 주어진 nums에서 subarray의 합이 k가 되는 모든 경우의 수를 구하여라
# 서브어레이가 포인트, 서브 어레이는 연속된 수들의 부분 집합

# 배열에 오직 양수만 있다면 슬라이딩 윈도우 풀이 생각해봐야함 O(n)
# 음수도 있으면 누적 배열과 해쉬로 풀자

# 포인트는 누적값의 부분배열의 합은, 누적값에서 구하고자하는 부분배열 이전까지의 누적값을 빼주면 된다는 것.

from typing import List  


def subarraySum(nums: List[int], k: int) -> int:        
    cml_sums = []
    tmp_sum = 0
    for num in nums:
      tmp_sum += num
      cml_sums.append(tmp_sum)
      
    table = {}
    count = 0
    table[0] = [-1]
    for idx, cml_sum in enumerate(cml_sums):
      target = cml_sum - k
      if target in table:
        count += len(table[target])
        
      if cml_sum not in table:
        table[cml_sum] = [idx]
      else:
        table[cml_sum].append(idx)    ## 사실 해시테이블에 누적수가 있다는게 중요하지 idx는 중요하지 않음. 그냥 continue 해줘도 무방할것임
  
    return count

subarraySum(nums=[6,3,2,5,3,-3],k=10)



###################################################################



def subArraySum(nums: List[int], sum: int) -> List[int]:
  accumNums = []
  tempNum = 0
  for num in nums:
    tempNum += num
    accumNums.append(tempNum)

  resultCount = 0
  hashTable = {}
  hashTable[0] = [-1]   # 만약 누적수가 sum 과 같다면, target = 0 이 되는데, 이를 위해 해쉬테이블에 0의 값을 넣어줘야함                
  for idx, accNum in enumerate(accumNums):
    target = accNum - sum
    if target in hashTable:
      resultCount += 1

    if hashTable.get(accNum) is None:     # elif 가 아니라 if 인 것에 주목, 위의 if 문과 별개임. 위 조건문에도 걸리고 이 조건문에도 걸리는 것
      hashTable[accNum] = [idx]
    else:
      continue   # 사실 해시테이블에 누적수가 있다는게 중요하지 idx는 중요하지 않음. 그냥 continue 해줘도 무방할것임
                # 하지만 만약 resultCount가 아니라 서브어레이 자체를 리턴하라고 하면 노코프처럼 해야할 것임

  return resultCount

subArraySum(nums=[6,3,2,5,3,-3],sum=10)