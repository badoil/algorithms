# 91
# 문제 : 숫자열을 디코딩 하는 방법의 갯수를 계산하여라
# 몇가지 방법이 있는가 와 같이 '몇가지' 이렇게 물어보면 대부분 dp 적용할 수 있음
# 포인트는 문제를 하위문제(서브 프라블럼)로 나눌 수 있는가임, 하위문제의 솔루션들의 합이 상위문제의 솔루션이 되는것

# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"

# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


# top-down
# [2, 1, 2, 3, 2, 5] -> 2|12325, 21|2325 : 요래 나눌 수 있는 것임
# 이를 다시 1|2325, 12|325 와 2|325, 23|25 이렇게 계속 나눠가는 것임
# 이때 325 의 경우 3|25, 32|5 로 나누는데, 이때 32|5 의 32는 해당하는 알파벳이 없으므로 해당 안됨
# 이런식으로 탑다운
# 여기서 중요한 점은 2325, 325...  등등이 중복되기 때문에 memoization 쓸 수 있고, 이는 아래의 바텀업 방법으로 점화식으로 누적적으로 게산할 수 있음을 의미

# bottom-up
# [2, 1, 2, 3, 2, 5] 의 경우 배열의 역방향에서 체크해줌
# [2, 5]를 보면 5는 한가지, 25는 2|5, 25 두가지로 만들 수 있기에 [2, 1]로 카운트됨
# [3, 2, 5]를 보면 32|5는 불가능, 3|25만 됨 이때 25가 2이므로, 앞에 3만 붙은 경우는 25의 2가 그대로 와서 2임 [2, 2, 1]로 카운트
# [2, 3, 2, 5]는 2|325, 23|25 나뉘는데, 이때 325가 2, 25도 2이므로 2+2, 4가 됨 [4, 2, 2, 1]로 카운트
# [1, 2, 3, 2, 5]은 1|2325 와 12|325로 나뉘고 2325가 4, 325가 2이므로 4+2, 6이되고 [6, 4, 2, 2, 1]
# [2, 1, 2, 3, 2, 5] 는 6 + 4, 10이고 [10, 6, 4, 2, 2, 1] 가 최종 카운트

# 여기서 처음으로 돌아가보자. [5]일때 [1]이고 [2, 5]일때 [2, 1]이다.
# 그런데 점화식이 F(n) = F(n+2) + F(n+1)이므로 [5]일때 [1, (1)] 즉 (1)이 있다고 쳐야한다, 즉 F(n+2)의 값을 (1)로 넣어주는 것
# 그래야 1+1, 2로 카운트해서 [2, 5]일때 [2, 1, (1)] 구하게 됨


# 디피 테이블을 역순으로 체크
# F(n) = F(n+2) + F(n+1), n이 인덱스 일때, 역순이기 때문에 n+2, n+1 이렇게 됨, 해당 인덱스 오른쪽과 그 오른쪽 카운트를 더해야함
# 따라서 디피테이블은 문자열의 갯수 + 1 있어야함.

def bottomUpDecodeWays(string: str) -> int:
  stringCount = len(string)
  if stringCount == 0:
    return 0

  decodeCounts = [0] * (stringCount+1)  # idx 가 stringCount-2 일때, 즉 배열의 끝에서 두번째일때, 점화식에 의하면 배열의 마지막과 그 마지막의 오른쪽 값이 필요하기에 string 길이보다 +1 해줌
  decodeCounts[-1] = 1                  # [2, 5]일때 [2, 1, (1)], (1)의 값을 이때 넣어주는 것

  lastChar = int(string[-1])
  if lastChar == 0:
    decodeCounts[stringCount-1] = 0   
  else:
    decodeCounts[stringCount-1] = 1   # [5]에 대해서 [1, (1)] 인 상황임, 1을 넣어준 것

  for idx in range(stringCount-2, -1, -1):  # F(n) = F(n+2) + F(n+1), n이 인덱스인 점화식을 구현하는 포문
    
    singleNumberCount = 0
    singleNumber = int(string[idx])
    if singleNumber > 0:                    
      singleNumberCount = decodeCounts[idx+1]  # 요놈이 F(n+1)

    doubleNumberCount = 0
    doubleNumber = int(string[idx:idx+2])
    if 10 <= doubleNumber <= 26:             
      doubleNumberCount = decodeCounts[idx+2]  # 요놈이 F(n+2)

    currentNumberCount = singleNumberCount + doubleNumberCount    # F(n) = F(n+2) + F(n+1)
    decodeCounts[idx] = currentNumberCount                      # F(n)을 디피테이블(decodeCounts)의 현재 인덱스로 최신화

  return decodeCounts[0]

