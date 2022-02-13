# 퀵 소트는 unstable
# best case: O(nlog n)
# worst case: O(n*n)
# avg case: O(nlog n)

# 바로 이전에 퀵 셀렉트에 기반해서 구현
# 이 방법은 in place memory sorting, 즉 새로운 배열을 생성하지 않는다는 점도 포인트

from typing import List
import random


#in place memory sorting
def quickSort(nums:List[int], beginIdx:int, lastIdx:int)->List[int]:
  length = lastIdx-beginIdx+1  
  if length <= 1:
    return nums

  pivotIdx = random.randrange(beginIdx,lastIdx+1)
  nums[pivotIdx],nums[lastIdx] = nums[lastIdx],nums[pivotIdx]
  leftIdx = beginIdx
  rightIdx = lastIdx-1
  pivot = nums[lastIdx]
  while leftIdx <= rightIdx:
    if nums[leftIdx] <= pivot:
      leftIdx += 1
      continue
    
    if pivot < nums[rightIdx]:
      rightIdx -= 1
      continue
    
    if pivot < nums[leftIdx] and nums[rightIdx] <= pivot:
      nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
      continue
  nums[leftIdx],nums[lastIdx] = nums[lastIdx],nums[leftIdx]

  quickSort(nums=nums, beginIdx=leftIdx+1,lastIdx = lastIdx)
  quickSort(nums=nums, beginIdx=beginIdx, lastIdx = leftIdx-1) 

  return nums

nums = [5,7,9,3,1,5,5,2,4]
quickSort(nums=nums,beginIdx=0,lastIdx=len(nums)-1)
print(nums)


#####################################################################



def quickSort(nums: List[int], beginIdx: int, lastIdx: int) -> List[int]:
  length = lastIdx - beginIdx + 1

  if length <= 1:
    return nums

  pivotIdx = random.randrange(beginIdx, lastIdx+1)
  nums[pivotIdx], nums[lastIdx] = nums[lastIdx], nums[pivotIdx]

  leftIdx = beginIdx
  rightIdx = lastIdx-1
  pivotNum = nums[lastIdx]

  while leftIdx <= rightIdx:
    leftNum = nums[leftIdx]
    rightNum = nums[rightIdx]
    
    if leftNum <= pivotNum:
      leftIdx += 1
      continue

    elif rightNum > pivotNum:
      rightIdx -= 1
      continue

    elif leftNum > pivotNum and rightNum <= pivotNum:
      nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
  
  nums[leftIdx], nums[lastIdx] = nums[lastIdx], nums[leftIdx]

  quickSort(nums, beginIdx, leftIdx-1)
  quickSort(nums, leftIdx+1, lastIdx)

  return nums