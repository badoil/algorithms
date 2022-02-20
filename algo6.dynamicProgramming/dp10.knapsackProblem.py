# 무게제한 있는 배낭에 최대의 밸류를 넣을 수 있는 경우를 구하라

# 각 물건의 갯수가 n 일때 모든 경우의 수는 2의 n 제곱이기 때문에 최적화 해줘야 함
# 최적화는 다이나믹 프로그래밍을 의심해봐야함

# 

from typing import List

class ObjectVal:
  def __init__(self, weight:int, value:int):
    self.weight = weight
    self.value = value

class KnapSack:
  def __init__(self, objects:List[ObjectVal]):
    self._objects = objects

  def _initDPTable(self,object_count:int, weight_limit:int):
    #init dp table
    self._dp = [[None for i in range(weight_limit+1)] for j in range(object_count+1)]
    for rowIdx in range(len(self._dp)):
      self._dp[rowIdx][0] = 0

    for colIdx in range(weight_limit+1):      
      self._dp[0][colIdx] = 0 

  def topDown(self, weight_limit:int) -> int:
    obj_endIdx = len(self._objects)
    self._initDPTable(obj_endIdx,weight_limit)    
    max_val = self._recurTopDown(obj_endIdx,weight_limit)
    return max_val    

  def _recurTopDown(self,object_idx:int,weight_limit:int) -> int:
    if object_idx < 0 or weight_limit < 0:
      return 0
    dp_val = self._dp[object_idx][weight_limit]
    if dp_val is None:
      prev_obj_idx = object_idx - 1
      not_taking_val = self._recurTopDown(prev_obj_idx,weight_limit)

      weight = self._objects[object_idx-1].weight
      value = self._objects[object_idx-1].value
      taking_val = self._recurTopDown(prev_obj_idx,weight_limit-weight)+value

      max_value = max(not_taking_val,taking_val)
      self._dp[object_idx][weight_limit] = max_value
      return max_value
    return dp_val    
    

  def bottomUp(self, weight_limit:int) -> int:
    obj_endIdx = len(self._objects)
    self._initDPTable(obj_endIdx,weight_limit)

    for rowIdx in range(1,len(self._dp)):
      for colIdx in range(1,weight_limit+1):      
        prev_obj_idx = rowIdx - 1
        not_taking_val = self._dp[prev_obj_idx][colIdx]
        
        weight = self._objects[rowIdx-1].weight
        value = self._objects[rowIdx-1].value
        print('weight', weight)
        print('value', value)
        
        taking_val = 0
        prev_weight_limit = colIdx-weight
        if prev_weight_limit<0:
          taking_val = 0
        else:
          taking_val = self._dp[prev_obj_idx][prev_weight_limit] + value
        
        print('self._dp[prev_obj_idx][prev_weight_limit]', self._dp[prev_obj_idx][prev_weight_limit])


        max_val = max(not_taking_val,taking_val)
        self._dp[rowIdx][colIdx] = max_val

    return self._dp[obj_endIdx][weight_limit]     


objects = [ObjectVal(1,30),ObjectVal(2,20),ObjectVal(3,40),ObjectVal(4,10)]
knapSack = KnapSack(objects)
print(knapSack.topDown(5))
print(knapSack.bottomUp(5))


#########################################################################################



class ObjectVal:
  def __init__(self, weight:int, value:int):
    self.weight = weight
    self.value = value


class KnapSack:
  def __init__(self, objects: List[ObjectVal]):
    self._objects = objects

  def _initDpTable(self, rows:int, weightCol: int):
    self._dpTable = [[None for _ in range(weightCol+1)] for _ in range(rows+1)]
    
    for rowIdx in range(len(self._dpTable)):
      self._dpTable[rowIdx][0] = 0

    for colIdx in range(weightCol+1):
      self._dpTable[0][colIdx]


  def bottomUpKnapSack(self, weightLimit: int) -> int:
    endRowIdx = len(self._objects)
    self._initDpTable(endRowIdx, weightLimit)
    
    for rowIdx in range(1, len(self._dpTable)):
      for colIdx in range(1, weightLimit+1):
        prevRowIdx = rowIdx - 1
        noChoiceCaseValue = self._dpTable[prevRowIdx][colIdx]

        prevWeight = self._objects[prevRowIdx].weight   # 현재 무게와 밸류를 알려면 self._objects의 현재 인덱스인 rowIdx가 아니라 prevRowIdx 로 조회해야함
        prevValue = self._objects[prevRowIdx].value     # 디피테이블은 0 인 경우도 추가해 놓았기 때문임
        
        choiceCaseValue = 0
        choiceCaseWeight = colIdx - prevWeight
        if choiceCaseWeight < 0:
          choiceCaseValue = 0

        else:
          choiceCaseValue = self._dpTable[prevRowIdx][choiceCaseWeight] + prevValue

        maxValue = max(noChoiceCaseValue, choiceCaseValue)
        self._dpTable[rowIdx][colIdx] = maxValue

    return self._dpTable[endRowIdx][weightLimit]