# 알고리즘의 꽃, key:value, insertion/find, 정렬은 안됨
# O(1) 으로 해시화 해서 찾을 수 있지만 해쉬테이블 만드는 시간은 O(n) 임
# 해시 충돌이 일어나도 충돌난 것은 몇개 안되기 때문에 빠르게 O(1)으로 find


# 문제: 양수로 주어진 nums중에서 두 수의 합이 target이 되는 index들을 return하여라
# 배열의 수들을 해쉬 테이블에 넣고 포문 속의 현재수와 더해서 타겟이 되는 수를 해쉬테이블에서 찾아서 그 인덱스들을 리턴
# 시간복잡도 O(n)

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  hash_table = {}  
  
  for idx,num in enumerate(nums):   # 해쉬테이블에 값을 넣는것과 찾는 것을 포문 안에서 동시에 진행
    match_num = target - num        # 이렇게 해도 되는 이유는, 현재 num에 대한 match_num이 없더라도, 나중에 이 match_num이 차례가 됐을때 이 num은 있기 때문임
    match_idx = hash_table.get(match_num)
    
    if match_idx is not None:
      return [idx,match_idx]     
    
    hash_table[num] = idx       # 해쉬테이블에 매칭되는 값 없으면 걍 테이블에 넣기

indices = twoSum(nums = [13,7,5,1,3,2],target=10)
print(indices)



##################################################################



# 결과는 같지만 노코프 방식이 더 깔끔, 포문도 하나만 쓰고

def twoSumHash(nums: List[int], targetSum: int) -> List[int]:
  
  hashTable = {}
  for idx, num in enumerate(nums):
    hashTable[num] = idx

  results = []
  for idx, num in enumerate(nums):
    n = targetSum - num
    targetIdx = hashTable.get(n)
    if targetIdx is not None:
      results.append((idx, targetIdx))

  if len(results) == 0:
    return None

  return results