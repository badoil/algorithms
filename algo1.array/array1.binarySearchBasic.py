# 배열의 기본 소팅 함수는 O(nlogn) 시간 복잡도임
# stable, unstable 한 정렬 방식이 있음

# search 시간복잡도는 O(n)
# sorted array 는 시간복잡도는 O(log(n))  

# leetcode 704 O(log n) 시간복잡도인 이진탐색 구현
from typing import List

def binarySearch(nums: List[int], target: int) -> int:
  left = 0
  right = len(nums)-1

  while left < right:
    pivot = (left + right) // 2

    if nums[pivot] == target:
      return pivot

    elif nums[pivot] > target:
      right = pivot-1
    
    else:
      left = pivot+1

  return -1