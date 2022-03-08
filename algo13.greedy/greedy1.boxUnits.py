# 그리디 문제가 어려운 이유는 로컬 솔루션이 글러벌 솔루션으로 착각할 수 있기 때문
# 즉 로컬 솔루션이 글로벌 솔루션이 되는 문제인 경우에 그리디 알고리즘 풀이법을 적용할 수 있음
# 그리디 풀이법을 적용할 수 있는 문제인지 아닌지 판별할 수 있는 감각이 중요함, 이 감각은 많이 풀어봐야 기를 수 있음

# 예를 들어 coin change 문제를 생각해보자
# 동전들 사이에 배수 관계가 성립할때 그리디 방법의 해가 글로벌 솔루션이 되지만
# 배수 관계가 성립하지 않으면 그리디의 해는 로컬 솔루션일뿐 글로벌 솔루션이 아니다

# 1710
# 문제 : 한개의 truck에 실을수 있는 최대 장난감의 갯수는 몇개인가? 
# truck에는 k개의 box를 실을수 있고, box 정보는 2D array로 주어진다. boxTypes[i] = [해당 박스의 갯수, 해당 박스안에들어있는 장난감의 갯수]
# 쉽게 생각해서 가장 많은 장난감이 들어있는 박스부터 실어보는 것, 이때 박스의 갯수 k가 제한되어 있음
# 장난감 갯수를 기준으로 내림차순으로 정렬 O(nlog n), 공간복잡도 O(1)



from typing import List

def maxBoxUnits(boxUnits: List[List[int]], maxBoxes: int) -> int:
  boxUnits.sort(key=lambda x:x[1], reverse=True)

  unitsCount = 0
  leftBoxes = maxBoxes
  for boxCount, units in boxUnits:
    if leftBoxes >= boxCount:
      unitsCount += (boxCount * units)
      leftBoxes -= boxCount

    else:
      unitsCount += (leftBoxes * units)
      leftBoxes -= leftBoxes

    if leftBoxes == 0:
      return unitsCount

  return unitsCount



  ###################################################################################


