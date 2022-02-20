# 139
# 문제: 주어진 string s를 wordDict 만으로 만들 수 있는지 판별하여라
# 디피어레이을 주어진 문자열에 해당하는 것으로 만든다
# 바텀-업 방법으로 디피어레이 인덱스까지의 부분 문자열을 주어진 dict로 만들 수 있는지 확인

# 솔직히 잘 모르겠음 걍 외우자

from typing import List

def wordBreak(string: str, dict: List[str]) -> bool:
  wordSet = set()                 # 원소가 문자열이라 집합으로 바꿔줘야함
  for word in dict:
    wordSet.add(word)

  length = len(string)
  dpArray = [False] * (length+1)      # string 길이보다 1 더 큰 dp테이블 생성
  dpArray[0] = True                   # 빈 문자열에 해당하는 첫 인덱스는 True를 넣어줌, 빈문자열은 주어진 dict에서 선택 안하는 것으로 만들 수 있다는 의미

  for idx in range(1,length+1):
    for word in wordSet:
      wordLength = len(word)
      prevIdx = idx - wordLength

      if prevIdx < 0:
        continue

      if dpArray[prevIdx] != True:    # 참,거짓은 체크하고자하는 단어 바로 전 인덱스인 dpArray[prevIdx] 값을 체크
        continue
      
      if string[prevIdx: idx] == word:   # 단어 체크하는 부분. dpArray가 길이가 1 더 길기 때문에 dpArray[prevIdx-1]에 해당하는 문자가 string[prevIdx]이다
        dpArray[idx] = True

  return dpArray[-1]