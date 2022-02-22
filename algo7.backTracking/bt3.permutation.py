# 46

# 문제: nums로 주어진 숫자로 만들수 있는 모든 permutation들을 return 하여라
# 유니크한 양수만 주어짐

# 재귀를 사용하는 이유는 하나의 레벨에 대한 함수 정의만 하면 되기 때문에 코드가 간결 


from typing import List

class Perm:
  def permute(self, nums: List[int]) -> List[List[int]]:

    self._nums = nums
    self._perms = []
    self._BT([])
    return self._perms  
  
  def _BT(self, crnt_sets):
    if len(crnt_sets) == len(self._nums):
      self._perms.append(crnt_sets.copy())
      return  

    for num in self._nums:
      if num in crnt_sets:
        continue
        
      crnt_sets.append(num)
      self._BT(crnt_sets)
      crnt_sets.pop()

perm = Perm()
perm.permute(nums=[1,2,3])


##################################################################



class Permutation:
  def solution(self, nums: List[int]) -> List[List[int]]:
    
    self._nums = nums
    self._results = []

    self._bt([])
    return self._results

  def _bt(self, crtArray: List[int]):
    if len(crtArray) == len(self._nums):
      self._results.append(crtArray.copy())
      return

    for num in self._nums:
      if num in crtArray:     # 전 레벨에서 선택된 숫자는 이번에 선택될 수 없다
        continue

      crtArray.append(num)
      self._bt(crtArray)
      crtArray.pop()

    