# 39
# 문제 : 주어진 array의 합이 sum이 되는 모든 combination 조합을 찾아라
# 유니크한 양수 주어짐
# 같은수를 여러번 사용 가능
# 시간복잡도 블라블라, 찾아봐야할듯, 복잡함
# 공간복잡도 O(sum/m), m은 주어진 배열 중에 가장 작은 수, 이 값이 주어진 디시전 스페이스의 깊이(레벨)임

# dp 에서 무제한 동전 바꾸기랑 비슷함. 그때는 조합의 갯수를, 여기서는 그 조합 자체를 리턴해야함
# 모든 조합, 즉 디시전 스페이스를 탐색하는 문제이기 때문에 백트래킹으로 보는 거임
# 항상 피라미드에서 가지치기를 생각하라

from typing import List

class CombSum:
  def solution(self, in_list: List[int], target: int) -> List[List[int]]:
    if len(in_list)==0:
      return []

    #set init member Vars
    self.__result = []
    self.__in_list = in_list
    comb = []
    self.__bt(0,target,comb) #backtracking
    return self.__result


  def __bt(self, prevIdx:int, targetSum:int, comb:List[int]):
    #exit conditions
    if targetSum==0:
      self.__result.append(comb.copy())
    elif targetSum < 0:
      return
    
    #process(candidates filtering)
    for idx in range(prevIdx,len(self.__in_list)):
      num = self.__in_list[idx] 

      #recusion call
      comb.append(num)       
      self.__bt(idx,targetSum-num,comb)
      comb.pop()
    return          # 나랑 리턴을 다르게 했음. 하지만 결과는 같음

combSum = CombSum()
combSum.solution(in_list=[1,2,3],target=5)



#################################################################################




class CombinationSum:
  def solution(self, givenArray: List[int], target: int) -> List[List[int]]:
    
    self._givenArray = givenArray
    self._target = target
    self._results = []

    self._bt(0, crtArray = [], targetSum = self._target)
    return self._results

  def _bt(self, prevIdx: int, crtArray: List[int], targetSum: int):
    if targetSum == self._target:
      self._results.append(crtArray)
      return                        # 노코프는 리턴을 다르게 했음. 하지만 결과는 같음
    elif targetSum < 0:
      return

    for idx in range(prevIdx, len(self._givenArray)):       # 조합이라 중복을 제거하기 위해서, 재귀함수를 호출할 때마다 다음 반복문은 다음 인덱스에서 시작함. 그래서 그 전 인덱스에 해당하는 수를 배제
      num = self._givenArray[idx]

      crtArray.append(num)
      self._bt(idx, crtArray, targetSum-num)
      crtArray.pop()