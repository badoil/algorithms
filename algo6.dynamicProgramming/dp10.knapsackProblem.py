# 무게제한 있는 배낭에 최대의 밸류를 넣을 수 있는 경우를 구하라

# 각 물건의 갯수가 n 일때 모든 경우의 수는 2의 n 제곱이기 때문에 최적화 해줘야 함
# 최적화는 다이나믹 프로그래밍을 의심해봐야함

# 문제를 하위문제로 나눠라
#            A   B   C   D
# value     30  20  40  10
# weight     1   2   3   4

# knapsack('ABCD', weight=5) 는 knapsack('ABC', weight=1) value = 10 과 knapsack('ABC', weight=5) value = 0 로 나눠짐
# 이때 knapsack('ABC', weight=5)가 5 그대로인 이유는 처음부터 'D'가 없었을 경우를 의미함 그래서 value는 안늘고 그대로 0

# knapsack('ABC', weight=1) value = 10 는 다시, 'c'를 선택한 경우 knapsack('AB', weight= 1-3 = -2) weight가 -2가 되어 해당 없음
# 그리고 'c'가 애초에 없었던 경우 knapsack('AB', weight=1)가 남음

# knapsack('ABC', weight=5) value = 0 은 다시, 'c'를 선택한 경우 knapsack('AB', weight=5-3=2) c의 value 인 40을 더해서, value = 40
# 그리고 'c'가 애초에 없었던 경우 knapsack('AB', weight=5)  value = 0 가 남음
# 이렇게 가지치기 반복

# 위의 가지치기 된 피라미드 꼴은 아래와 같은 점화식으로 표현
# knapsack(N, W) = max(knapsack((N-1, W-W[n]) + Val[n]), knapsack(N-1, W))
# knapsack(N, W) 에서 변수가 2개기 때문에 2차원 dp테이블이 필요함

# dpTable, 세로축이 N 물건, 가로축이 W 무게, 해당값은 value
#         0   1   2   3   4   5
# 0   ''  0   0   0   0   0   0
# 1    A  0  30  30  30  30  30
# 2   AB  0  30  30  50  50  50
# 3  ABC  0  30  30  50  70  70
# 4 ABCD  0  30  30  50  70  70
# 이때 우리가 알아야하는 값은 'ABCD'가 전부 있는 케이스 N=4, W=5 인 knapsack(4, 5)이고, 이는 디피테이블의 dpTable[4][5]
# dpTable[4][5] 값을 알아내기 위해서 탑다운, 바텀업 사용가능 
# 탑다운의 경우 knapsack(4, 5) = max(knapsack((N-1=3, W-W[n]=5-4=1) + Val[n])=10, knapsack(N-1=3, W=5)) 즉 max(knapsack((3, 1) + 10, knapsack(3, 5))
# 이런식으로 재귀적인 탑다운 방식이 반복된다. 그러므로 초기값 dpTable[N][0], dpTable[0][W] 을 미리 구해둠. 각 모두 0임, 왜냐하면 물건이 0이면 무게도 0이고 그 반대도 마찬가지이기 때문
# 바텀업의 경우 초기값으로부터 대각선으로 가는경우는 해당물건이 있었던 경우, 세로방향으로 가는경우는 해당물건이 없는 경우로, 둘 중 max 값 선택해서 디피테이블에 기입
# dpTable[4][5] = 70 이므로 이를 거꾸로 추적하면, 70이 세로에서 내려오니까 D는 없었고, N=3 일때 대각선에서 오므로 C는 있음. N=2일때 30은 세로에서 내려오므로 B는 없었음, N=1일때 A임
# 고로 A, C가 있고 최대 값은 70 임

# 시간복잡도 O(N * W), 공간복잡도 O(N * W)
# 그런데 이때 공간복잡도는 디피테이블의 값을 구하는데 바로 이전 행의 값들만 필요하므로 O(W)로 최적화 가능 O(W)


 
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