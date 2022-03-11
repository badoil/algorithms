# 139
# 문제: 주어진 string s를 wordDictionary 만으로 만들 수 있는지 판별하여라

# topDown
# 'nocope'라는 문자열과 ditionary = [e, no, cop] 가 주어짐
# 'nocope'라는 문자열은 n|ocope, no|cope, noc|ope, noco|pe, nocop|e, nocope| 요래 나눠질 수 있음
# n|ocope의 'ocope'는 o|cope, oc|ope, oco|pe, ocop|e, ocope| 다시 이렇게 나뉨
# WordBreak('nocope') = (Dict('n') && WordBreak('ocope')) || (Dict('no') && WordBreak('cope')) || (Dict('noc') && WordBreak('ope'))...
# 이때 WordBreak('ocope') = (Dict('o') && WordBreak('cope')) || (Dict('oc') && WordBreak('ope')) || (Dict('oco') && WordBreak('pe'))... 하위 문제로 나뉨
# WordBreak('cope'), WordBreak('ope') 등등이 반복됨을 알 수 있음. 이는 메모이제이션을 생각해야함을 의미

# 'nocope' 역순으로 진행, ditionary = [e, no, cop]
# WordBreak('e') = Dict('e') 이고 이는 True, [T]
# WordBreak('pe') = Dict('pe') || (Dict('p') && WordBreak('e')) 
#                 =>    F      || (   F      &&      T        ) 이고 고로 F, 즉 [F, T]
# WordBreak('ope') = Dict('ope') || (Dict('o') && WordBreak('pe')) || (Dict('op') && WordBreak('e')) 
#                  =>     F      || (    F     &&      F         ) || (    F      &&      T        ) 이고 고로 F, [F, F, T]
# WordBreak('cope') = Dict('cope') || (Dict('c') && WordBreak('ope')) || (Dict('co') && WordBreak('pe')) || (Dict('cop') && WordBreak('e')) 
#                   =>      F      || (    F     &&        F        ) || (     F     &&        F       ) || (     T      &&       T       ) 이고 고로 T, [T, F, F, T]
# 이런식으로 계속 진행하면 이 가지들 중에 [T, F, T, F, F, T]



# bottonUp 
# 디피어레이을 주어진 문자열에 해당하는 것으로 만든다
# 바텀-업 방법으로 디피어레이 인덱스까지의 부분 문자열을 주어진 dict로 만들 수 있는지 확인
# 'nocope'라는 문자열과 ditionary = [e, no, cop] 가 주어짐
#           [F,  F, F, F, F, F, F ]
#           ['', n, o, c, o, p, e ]
# dpArray = [T,  F, F, F, F, F, F ] -> 빈 문자열에 해당하는 첫 인덱스를 만들어줌, True를 넣어줌, 빈문자열은 주어진 dict에서 선택 안하면 만들 수 있기에 True
# 
# ['', n] 을 [e, no, cop] dict 로 만들 수 있나? e의 경우 문자열의 길이 1이므로 dpArray의 n 위치 인덱스에서 1을 빼준 인덱스의 값 T, 이때 현재 n과 dict의 e가 일치여부 체크 => F
#                                          no의 경우 문자열의 길이 2이므로 dpArray의 n 위치 인덱스에서 2을 빼준 값 없음 => F
#                                         cop의 경우 문자열의 길이 3이므로 dpArray의 n 위치 인덱스에서 3을 빼준 값 없음 => F, 즉 dpArray = [T,  F, F, F, F, F, F ]
# ['', n, o] 을 [e, no, cop] dict 로 만들 수 있나? e의 경우 문자열의 길이 1이므로 dpArray의 n 위치 인덱스에서 1을 빼준 인덱스의 값 F => F
#                                             no의 경우 문자열의 길이 2이므로 dpArray의 n 위치 인덱스에서 2을 빼준 값 T, 이때 현재 no와 dict의 no 일치여부 체크 => T
#                                            cop의 경우 문자열의 길이 3이므로 dpArray의 n 위치 인덱스에서 3을 빼준 값 없음 => F, 즉 dpArray = [T,  F, T, F, F, F, F ]
# 이런식으로 반복하면 [T, F, T, F, F, T, T]
# 맨 마지막이 T 이므로 T 리턴

# 걍 외우자

from typing import List

def bottomUpWordBreak(string: str, dict: List[str]) -> bool:
  wordSet = set()                 # 원소가 문자열이라 집합으로 바꿔줘야함
  for word in dict:
    wordSet.add(word)

  length = len(string)
  dpArray = [False] * (length+1)      # string 길이보다 1 더 큰 dp테이블 생성
  dpArray[0] = True                   # 빈 문자열에 해당하는 첫 인덱스는 True를 넣어줌, 빈문자열은 주어진 dict에서 선택 안하면 만들 수 있기에 True

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