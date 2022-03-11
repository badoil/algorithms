# 152
# 문제: 주어진 Array에서 최대곱 Maximum Subarray를 계산하여라

# 이전 maxSubArraySum 과 같은 형태의 문제
# 다만 곱하기이다보니까 dp 테이블을 두가지, 즉 dpMinArray와 dpMaxArray 가 필요
# min(crtNum, crtMinNum, crtMaxNum), max(crtNum, crtMinNum, crtMaxNum)
# 즉 crtMinNum에서 최대값이, crtMaxNum에서 최소값이 나올 수도 있는것(-1, 0을 곱하게 될 때도 있기 때문)
# 그래서 최소값을 디피 테이블에 걔속 최신화해줘야함. 그 최소값이 음수고 현재값이 -1이 된다면 이게 최대값이 되기도 하기 때문

from typing import List

def maxProduct(nums: List[int]) -> int:
  max_dp = [nums[0]]
  min_dp = [nums[0]]
  
  for idx in range(1,len(nums)):
    prev_idx = idx - 1
    
    num = nums[idx]
    cand0 = num
    cand1 = max_dp[prev_idx] * num
    cand2 = min_dp[prev_idx] * num
    
    max_val = max(num,cand1,cand2)
    min_val = min(num,cand1,cand2)
    
    max_dp.append(max_val)
    min_dp.append(min_val)
  
  max_product = max(max_dp)
  return max_product

print(maxProduct(nums=[3,-2,1,0,-8,-9]))


############################################################################



def maxSubArrayProduct(nums: List[int]) -> int:
  if len(nums) == 0:
    return 0

  if len(nums) == 1:
    return 1

  dpMinArray = []       # 곱하기이다보니까 dp 테이블을 두가지, 즉 dpMinArray와 dpMaxArray 가 필요
  dpMaxArray = []

  dpMinArray[0] = nums[0]   # 첫번째 수는 넣어주고
  dpMaxArray[0] = nums[0]

  for idx in range(1, len(nums)):
    crtNum = nums[idx]
    lastMinNum = dpMinArray[idx-1]
    lastMaxNum = dpMaxArray[idx-1]

    crtMinNum = crtNum * lastMinNum
    crtMaxNum = crtNum * lastMaxNum

    dpMinArray[idx] = min(crtNum, crtMinNum, crtMaxNum)   # crtMinNum에서 최대값이, crtMaxNum에서 최소값이 나올 수도 있는것(-1, 0을 곱하게 될 때도 있기 때문)
    dpMaxArray[idx] = max(crtNum, crtMinNum, crtMaxNum)   # 그래서 최소값을 디피 테이블에 걔속 최신화해줘야함. 그 최소값이 음수고 현재값이 -1이 된다면 이게 최대값이 되기도 하기 때문


  maxNum = max(dpMaxArray)
  return maxNum