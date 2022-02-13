# 선캑정렬
# 순서대로 선택한 인덱스를 기준으로, 그 오른쪽에서 가장 작은 값과 기준값을 계속해서 스왑해주는 것이 선택 정렬
# O(log n*n) 알고리즘으로 알고만 넘어가자
# 언스테이블 소팅임


from re import I
from typing import List

def selectionSort(nums: List) -> List:
  for idx in range(0, len(nums)):      # 배열의 첫 원소를 기준으로 오르쪽에서 최소값 찾아야함
    crtNum = nums[idx]
    minNum = crtNum
    minIdx = idx
    for i in range(idx, len(nums)):    # idx 포함한 오른쪽 에서 최소값 찾기
      if minNum > nums[i]:
        minNum = nums[i]
        minIdx = i
    nums[idx], nums[minIdx] = nums[minIdx], nums[idx]    # 찾은 최소값을 현재 idx 의 값과 스왑

  return nums

print(selectionSort(nums=[9,3,5,7,1]))

  # unstable

def unstableSelectionSort(numsString: List) -> List:
  for idx in range(0, len(numsString)):
    
    minNum = numsString[idx][0]
    minIdx = idx
    for i in range(idx, len(numsString)):
      if minNum > numsString[i][0]:
        minNum = numsString[i][0]
        minIdx = I
    numsString[idx], numsString[minIdx] = numsString[minIdx], numsString[idx]

  return numsString

unstableSelectionSort([(3, 'c'), (5, 'a'), (5, 'b'), (7, 'b'), (7, 'a')])
