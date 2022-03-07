# 힙은 바이너리 트리로 구현됨

from typing import List

#make parent node largest
def swap(arr:List[int], rootIdx:int):
  largeIdx = rootIdx 
  leftChild = 2 * rootIdx + 1   
  rightChild = 2 * rootIdx + 2

  if leftChild < len(arr) and arr[largeIdx] < arr[leftChild]:
    largeIdx = leftChild

  if rightChild < len(arr) and arr[largeIdx] < arr[rightChild]:
    largeIdx = rightChild

  if largeIdx != rootIdx:
    arr[rootIdx], arr[largeIdx] = arr[largeIdx], arr[rootIdx]

    # recursive call to child
    swap(arr,largeIdx)

def heapify(arr:List[int]):
  for idx in range(len(arr)//2,-1,-1):
    swap(arr=arr,rootIdx=idx)

arr = [1,3,5,7,9,4,6]
heapify(arr)
print(arr)

#################################

def swap(arr: List, rootIdx: int):
  largestIdx = rootIdx
  leftChildIdx = rootIdx * 2 + 1
  rightChildIdx = rootIdx * 2 + 2

  if len(arr) > leftChildIdx and arr[leftChildIdx] > arr[largestIdx]:
    largestIdx = leftChildIdx
  
  if len(arr) > rightChildIdx and arr[rightChildIdx] > arr[largestIdx]:
    largestIdx = rightChildIdx

  if largestIdx != rootIdx:
    arr[largestIdx], arr[rootIdx] = arr[rootIdx], arr[largestIdx]
    swap(arr, largestIdx)

def heapify(arr: List):
  length = len(arr)
  for idx in range(length, -1, -1):
    swap(arr, idx)