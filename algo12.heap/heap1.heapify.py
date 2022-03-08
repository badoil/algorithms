# 힙은 일종의 우선순위큐 인 것이다.
# 힙은 바이너리 트리로 구현됨
# maxHeap 의 경우 부모가 자식노드들보다 항상 큰 complete binary tree(위에서 왼쪽으로 차있는 모양) 형태를 가짐
# 젤 큰 값은 root 노드 위치에 있기에 이를 O(1) 으로 찾을 수 있음

# add: 힙에 새로운 원소를 넣을 경우, 트리의 오른쪽 끝에 들어가고 이것이 부모 노드보다 크면 스왑, 이를 반복 O(log(n))
# delete: 힙에 팝을 할 경우 루트노드를 팝하고, complete binary tree 오른쪽 끝에 있는 노드를 루트로 스왑한 후 자식노드와 비교해서 스왑 혹은 멈춤 고로 O(log(n))
# build heap: O(n) 그냥 외워

# 파이썬에서 heapq.heapify 는 최소힙

# 힙의 complete binary tree이기 때문에 array로도 표현 가능
# [9, 7, 5, 1, 3]의 경우
# parentIdx = (leftChildIdx-1)/2
# leftChildIdx = (parentIdx * 2) + 1
# rightChildIdx = (parentIdx * 2) + 2


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



##############################################################
# 배열의 중간 인덱스부터 0번째 인덱스로 내려가면서(즉 트리상으로는 올라가면서) 그 자식노드들과 비교하며 스왑
# 배열의 중간 인덱스 다음으로는 트리상에서 자식노드가 없는 노드이기 때문에 생략, 어차피 이들의 부모노드들과 비교될 거임
# 스왑한 후 그 자식 노드의 자식노드끼도 다시 비교해야 하기 때문에 재귀적으로 호출


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
    swap(arr, largestIdx)        # 스왑한 후 그 자식 노드의 자식노드끼도 다시 비교해야 하기 때문에 재귀적으로 호출

def heapify(arr: List):
  halfLength = len(arr)//2
  for idx in range(halfLength, -1, -1): # 배열의 중간 인덱스부터 0번째 인덱스로 내려가면서(즉 트리상으로는 올라가면서) 그 자식노드들과 비교하며 스왑
    swap(arr, idx)                      # 배열의 중간 인덱스 다음으로는 트리상에서 자식노드가 없는 노드이기 때문에 생략, 어차피 이들의 부모노드들과 비교될 거임
