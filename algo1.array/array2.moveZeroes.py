#leetcode 283
# 주어진 배열의 0을 배열의 끝 부분에 위치시키기
from typing import List

def moveZeroes(nums: List[int]) -> List:
  crtIdx = 0
  count = len(nums)

  for idx in range(count):
    print(idx)
    if nums[idx] != 0:
      nums[crtIdx], nums[idx] = nums[idx], nums[crtIdx]
      crtIdx += 1

  print(nums)
  return nums



moveZeroes([324030])
