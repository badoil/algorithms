# 215
# 주어진 배열에서 n 번째로 큰 수를 리턴하라
# sort 함수로 정렬 후 뒤에서 n 번째 수를 리턴하면 O(nlog n)
# heap 자료구조를 이용하면 O(nlog k) -> 안해봄, 해볼것
# O(nlog k) 보다 빠른 알고리즘이 퀵 셀렉트
# 피봇과 파티셔닝 써야함

from typing import List
import random

def quickSelect(nums:List[int],k:int) -> int:
  length = len(nums)
  if length == 1:
    return nums[0]

  pivotIdx = random.randrange(length)
  lastIdx = length-1

  nums[pivotIdx],nums[lastIdx] = nums[lastIdx],nums[pivotIdx]
  leftIdx = 0
  rightIdx = length-2
  pivot = nums[-1]
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
  if leftIdx == length - k:
    return nums[leftIdx]
  elif leftIdx < length-k:
    #list slicing creates copy. 
    return quickSelect(nums=nums[leftIdx+1:],k=k)
  elif length-k < leftIdx:
    #list slicing creates copy.
    return quickSelect(nums=nums[:leftIdx],k=k-(length-leftIdx)) 


quickSelect(nums=[5,7,9,3,1,2,4],k=2)

###########################################################################



def quickSelection(nums: List[int], nth: int) -> int:
  length = len(nums)
  if length == 1:   # 주어진 리스트가 길이가 1이면 하나뿐인 그 원소를 리턴
    return nums[0]

  pivotIdx = random.randrange(length)  # 피봇 인덱스를 랜덤으로 선택
  lastIdx = length-1
  nums[pivotIdx], nums[lastIdx] = nums[lastIdx], nums[pivotIdx]  # 피봇값을 배열의 마지막 값과 자리 바꿈

  leftIdx = 0
  rightIdx = length-2

  while leftIdx <= rightIdx:     # 피봇값이 리스트의 마지막에 오고, leftIdx 와 rightIdx 두개의 포인터가 엇갈리지 않는 동안
    pivotNum = nums[lastIdx]
    leftNum = nums[leftIdx]
    rightNum = nums[rightIdx]
    if leftNum <= pivotNum:      # 피봇값보다 작은 수는 다음 인덱스로 넘어가고
      leftIdx += 1
      continue
    
    elif rightNum > pivotNum :   # 피봇값보다 큰 수는 다음 인덱스로 넘어가고
      rightIdx -= 1
      continue
    
    elif leftNum > pivotNum and rightNum <= pivotNum:    # 왼쪽값이 피봇값보다 크고 오른쪽 값이 피봇값보다 작으면, 두 수를 스왑
      nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]

  nums[leftIdx], nums[lastIdx] = nums[lastIdx], nums[leftIdx] 

  # 반복문을 마치면 leftIdx가 피봇값의 들어가야할 위치, 즉 그 배열의 length-leftIdx 번째 로 큰 위치를 가리킨다. nth=length-leftIdx 를 찾을때까지 함수를 재귀적으로 호출
  # 따라서 length-nth 는 찾고자하는 n번째로 큰 수의 위치를 가리키는 인덱스이고 이 인덱스가 leftIdx와 같으면 바로 그 값이 n번째로 큰 수임
  if leftIdx == length-nth:
    return nums[leftIdx]

  elif leftIdx < length-nth:        # 이 경우 n번째로 큰 수가 오른쪽에 있기 오른쪽 배열에 대해서 다시 퀵 셀렉션 함수 재귀적으로 호출
    return quickSelection(nums[leftIdx+1:], nth)

  elif leftIdx > length-nth:        # 이 경우 n번째로 큰 수가 왼쪽에 있기 왼쪽 배열에 대해서 다시 퀵 셀렉션 함수 재귀적으로 호출
    return quickSelection(nums[:leftIdx], nth-(length-leftIdx))  # 왼쪽에 있으니까 leftIdx 이하 잘라버림(length-leftIdx 번째부터 다 잘라버림)

  
