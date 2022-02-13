# 배열 안의 피크 숫자 [3,5,3,2,2,7,1]이면 5(or 7)의 인덱스를 리턴하는 문제
# 피크가 여러개면 그중 하나만 리턴하면 됨
# 배열을 2차원 xy 그래프에 그리서 생각하면 쉬움.
# 배열의 모든 값을 순회하면서 양옆 값을 비교해서 하면 O(n)
# 하지만 이진탐색 binary search 를 이용하면 O(log n)으로 해결 가능
# left right 인덱스값이 만나는 그 값이 피크 값임
# 피크가 있다면 순서대로 leftIdx, pivot=leftIdx+1, rightIdx=pivot+1 인 지점을 찾게되고 각 인덱스가 0, 1, 2 이라면
# 다음으로 leftIdx 와 pivot은 0, rightIdx = 1 상황이 되서, 조건문에 의해 leftIdx = pivot+1이 되어 1이 되고 이는 leftIdx=rightIdx 경우가 반드시 생김
# 이때 반복문은 탈출하고 leftIdx or rightIdx 값을 리턴하면 됨 

from typing import List


from typing import List

def findPeak(nums: List[int]) -> int:
  if len(nums) <= 1:
    return 0  
  
  left = 0
  right = len(nums)-1
  
  while left < right:
    pivot = int ((left+right)/2)
    num = nums[pivot]
    nextNum = nums[pivot+1]
    
    if num < nextNum:
      left = pivot+1
    else:
      right = pivot
  
  return left

###############################################

def findPeakElement(nums: List[int]) -> int:
  if len(nums) <= 2:
    return 0

  leftIdx = 0
  rightIdx = len(nums)-1

  while leftIdx < rightIdx: 
    pivot = (leftIdx+rightIdx)//2
    if nums[pivot] < nums[pivot+1]: # 피봇값 보다 피봇 다음값이 더 크면 피크는 오른쪽에 있음
      leftIdx = pivot+1

    else:
      rightIdx = pivot  

  return leftIdx
  # return right 도 상관없음, 결국 left=right 되는 순간 반목문은 종료되고 그 값이 피크 값임

  # print('peakIdx',findPeakElement([1,2,4,5,6,7,8])) 이 값은 원소가 8인 6 인덱스를 리턴