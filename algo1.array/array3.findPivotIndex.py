#leetcode 724
# 피봇 인덱스를 기준으로 왼쪽의 합과 오른쪽의 합이 같은 피봇 인덱스를 리턴 
from typing import List

def pivotIndx(nums: List[int]) -> int:
  total = sum(nums)
  leftSum = 0
  rightSum = 0

  last = 0
  for idx in range(len(nums)):
    num = nums[idx]
    leftSum += last
    rightSum += num

    if leftSum == (total - rightSum):
      return idx

    last = nums[idx]

  return -1