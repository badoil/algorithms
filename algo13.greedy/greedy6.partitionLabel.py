#leetcode 763
# 문제: 주어진 문자열을 최대한 많은 partition으로 나누어라. 이때 각 알파벳은 하나의 파티션에만 포함되어야 한다.
# TC는 해쉬맵 만드는데 O(n) + 파티션 만드는 순회 O(n) 따라서 전체 O(n)
# SC는 O(26) 즉 O(1)

#알파벳이 나오는 마지막 idx 값만 알면 된다는 아이디어



from typing import List

from typing import List  

def partitionLabels(S: str) -> List[int]:
  last_idxs = {}
  for idx, c in enumerate(S):
    last_idxs[c] = idx
      
  tmp_idx = 0
  part_begin = 0
  partitions = []
  
  for idx, c in enumerate(S):
    last_idx = last_idxs[c]
    tmp_idx = max(tmp_idx, last_idx)
    if idx == tmp_idx:
      partitions.append(S[part_begin:idx+1])
      part_begin = idx + 1                  
    
  return partitions

partitionLabels(S="acacdfehdehjkj")

###########################################################
# 안보고 쳐본거
# 알파벳이 나오는 마지막 idx 값만 알면 되기에 해쉬맵에 저장


def partition(s: str) -> List:
  mapping = {}
  for idx, c in enumerate(s):
    mapping[c] = idx

  maxIdx = 0
  beginIdx = 0
  results = []

  for idx, c in enumerate(s):
    lastCIdx = mapping[c]             
    maxIdx = max(maxIdx, lastCIdx)    # 'acac' 이런경우 maxIdx가 세번째 인덱스에서 3(a) -> 4(c) -> 3(a) 바뀔 우려가 있음 a가 다시 나오기때문. 이를 4(c)로 고정하기 위해 max 씀
    if idx == maxIdx:
      results.append(s[beginIdx:idx+1])
      beginIdx = idx + 1

  return results


#############################################################
#요거는 내가 푼 방법


from typing import List  

def partitioning(s: str) -> List[List[int]]:
  if len(s) == 0:
    return []


  hash = {}
  for idx, char in enumerate(s):
    hash[char] = idx

  results = []
  startIdx = 0
  lastIdx = 0
  lastChar = ''
  for idx, c in enumerate(s):
    crtCharLastIdx = hash.get(c)
    
    if lastChar != c and lastIdx <= crtCharLastIdx:  # 'acac' 이런경우 maxIdx가 세번째 인덱스에서 3(a) -> 4(c) -> 3(a)으로 바뀔 우려가 있음 a가 다시 나오기때문. 이를 4(c)로 고정하기 위해 조건 필요
      lastChar = c                                   # lastChar != c 이 조건은 사실 필요 없음, 이 조건문 전체가 max 함수 이용하는게 나음
      lastIdx = crtCharLastIdx

    if idx == lastIdx:
      part = s[startIdx: idx+1]
      results.append(part)
      startIdx = idx+1


  return results
      
partition(s="acacdfehdehjkj")