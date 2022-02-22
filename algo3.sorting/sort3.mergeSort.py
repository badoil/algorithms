# merge sort, stable 한 정렬
# 재귀가 구현이 쉬워서 재궈로 함
# 주어진 배열을 다 쪼개고 다시 각각을 비교해서 상향식으로 합쳐줌
# 쪼갤때 재귀적으로 쪼개고 쪼갠 놈을 합치면서 스택을 마무리하는 과정

from typing import List


def mergeSort(nums:List[int]) -> List[int]:

  #split
  length = len(nums)
  if length == 1:
    return nums

  mid = length//2

  left_nums = nums[:mid]
  right_nums = nums[mid:]

  sorted_left = mergeSort(nums=left_nums)
  sorted_right = mergeSort(nums=right_nums)


  #merge,  Swap approach is memory friendly. But..
  #For the easy code, new array sorted_nums is created 
  sorted_nums = []   
  idx_l = 0
  idx_r = 0
  while idx_l<len(sorted_left) or idx_r < len(sorted_right):
    if idx_l == len(sorted_left):
      sorted_nums.append(sorted_right[idx_r])
      idx_r += 1
      continue

    if idx_r == len(sorted_right):
      sorted_nums.append(sorted_left[idx_l])
      idx_l += 1
      continue

    if sorted_right[idx_r] <= sorted_left[idx_l]:
      sorted_nums.append(sorted_right[idx_r])
      idx_r += 1
    else:
      sorted_nums.append(sorted_left[idx_l])
      idx_l += 1

  return sorted_nums

  
mergeSort(nums=[5,7,9,3,1,2,4])


########################################################


def mergeSorting(nums: List[int]) -> List[int]:
  count = len(nums)

  if count == 1:
    return nums

  mid = count//2
  numsLeft = nums[:mid]
  numsRight = nums[mid:]

  leftSortedNum = mergeSorting(nums=numsLeft)
  rightSortedNum = mergeSorting(nums=numsRight)

  mergeResult = []
  leftIdx = 0
  rightIdx = 0

  # 병합하는 부분
  while leftIdx < len(leftSortedNum) or rightIdx < len(rightSortedNum):   # 둘 중 하나의 쪼개진 배열의 인덱스를 넘지 않는 동안
    if leftIdx == len(leftSortedNum):                                     # 두 배열 중 한 배열의 원소들을 다 합쳐주었다면
      lastRightNum = rightSortedNum[rightIdx]                                       # 남은 다른 배열의 원소를 합쳐줌
      mergeResult.append(lastRightNum)
      rightIdx += 1
      continue

    if rightIdx == len(rightSortedNum):                                  # 두 배열 중 한 배열의 원소들을 다 합쳐주었다면
      lastLeftNum = leftSortedNum[leftIdx]                                        # 남은 다른 배열의 원소를 합쳐줌
      mergeResult.append(lastLeftNum)
      leftIdx += 1
      continue

    if leftSortedNum[leftIdx] < rightSortedNum[rightIdx]:     # 두배열의 각각의 원소를 비교해서 작은 값을 새 배열에 넣어줌
      leftNum = leftSortedNum[leftIdx]
      mergeResult.append(leftNum)
      leftIdx += 1

    else:                                                     # 두배열의 각각의 원소를 비교해서 작은 값을 새 배열에 넣어줌
      rightNum = rightSortedNum[rightIdx]
      mergeResult.append(rightNum)
      rightIdx += 1

  return mergeResult                                          # 리턴해줘야 스택이 마무리되면서 더 큰 부분 배열들을 합칠 수 있음