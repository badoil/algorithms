# 1578
# 문제 : string s와 i번째 문자를 지우기 위한 cost[i]가 주어진다. 연속되는 알파벳을 지우기 위한 최소비용은 몇인가?
# 각 문자열을 지우기 위한 코스트가 있음.

# 스택에 비슷한 문제가 있었음. 그런데 그 문제는 연속된 중복문자를 모두 삭제했으나 이 문제는 하나 남겨야됨. 그래서 스택 쓸 필요 없음

# 포인트는 동일한 문자들의 연속을 하나의 세트로 보고, 그 세트에서 최대 비용을 제외한 비용들을 더해주면 그것이 최소비용임
# 이를 위해 문자와 비용을 순회하면서 지난번것과 지금것을 비교하며 최소비용을 구함
# 크게 지난문자와 지금 문자가 다른 경우와 같은 경우로 나누고
# 두 문자가 같은 경우는 지난 문자의 비용과 지금 문자의 비용을 비교해서 나눔

# 배열의 값들을 비교하면서 진행하기 때문에, 순간 순간의 최적해를 더해주면서 진행
# 이것이 그리디한 접근임



from typing import List

def minCost(s: str, cost: List[int]) -> int:
  if len(cost) <= 1:
    return 0
  
  last_char = ""
  max_cost = 0
  total_cost = 0
  
  for idx,nth_cost in enumerate(cost):
    nth_char = s[idx]      
    if nth_char != last_char:
      last_char = nth_char
      max_cost = nth_cost
    
    else: #nth_char == s[idx]
      if nth_cost <= max_cost:
        total_cost += nth_cost             
      else: #max_cost < nth_cost
        total_cost += max_cost
        max_cost = nth_cost
        
  return total_cost


s= "abaac"
cost = [1,2,3,4,5]
print(minCost(s=s,cost=cost))

s= "bbbaaac"
cost = [3,1,2,1,5,3,2]
print(minCost(s=s,cost=cost))
          


################################################################


def minimumCost(s: str, costs: List[int]) -> int:
  if len(costs) <= 1:
    return 0

  lastChar = ''
  lastMaxCost = 0
  costSum = 0

  for idx,  crtCost in costs:
    crtChar = s[idx]
    if lastChar != crtChar:         # 크게 지난문자와 지금 문자가 다른 경우, 새로운 문자집합의 시작
      lastChar = crtChar
      lastMaxCost = crtCost

    else:                           # 크게 지난문자와 지금 문자가 같은 경우
      if lastMaxCost <= crtCost:    # 지난번 비용이 더 작은 경우
        costSum += lastMaxCost      # 더 적은 비용을 총비용에 더해줌
        lastMaxCost = crtCost

      else:                         # 현재 비용이 더 작은 경우
        costSum += crtCost          # 더 적은 비용을 총비용에 더해줌

  return costSum