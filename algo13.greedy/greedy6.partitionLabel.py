#leetcode 763
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

##############################################


def partition(s: str) -> List:
  mapping = {}
  for idx, c in enumerate(s):
    mapping[c] = idx

  maxIdx = 0
  beginIdx = 0
  results = []

  for idx, c in enumerate(s):
    lastCIdx = mapping[c]
    maxIdx = max(tmpIdx, lastCIdx)
    if idx == maxIdx:
      results.append(s[beginIdx:idx+1])
      beginIdx = idx + 1

  return results