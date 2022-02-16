# 91
# 문제 : 숫자열을 디코딩 하는 방법의 갯수를 계산하여라
# 몇가지 방법이 있는가 와 같이 '몇가지' 이렇게 물어보면 대부분 dp 적용할 수 있음

# 디피 테이블을 역순으로 체크
# F(n) = F(n+2) + F(n+1), n이 인덱스 일때, 역순이기 때문에 n+2, n+1 이렇게 됨, 해당 인덱스 오른쪽과 그 오른쪽 카운트를 더해야함
# 따라서 디피테이블은 문자열의 갯수 + 1 있어야함.

def bottomUpDecodeWays(string: str) -> int:
  stringCount = len(string)
  if stringCount == 0:
    return 0

  decodeCounts = [0] * (stringCount+1)  # idx 가 stringCount-2 일때, 즉 배열의 끝에서 두번째일때, 점화식에 의하면 배열의 마지막과 그 마지막의 오른쪽 값이 필요하기에 string 길이보다 +1 해줌
  decodeCounts[-1] = 1                  # 그리고 그 값에 1을 넣어주는 이유는 배열의 '끝에서 두번째수'+'마지막수'인 doubleNumber가 10 <= doubleNumber <= 26 조건에 맞을경우 카운트가 필요하기 때문임

  lastChar = int(string[-1])
  if lastChar == 0:
    decodeCounts[stringCount-1] = 0
  else:
    decodeCounts[stringCount-1] = 1

  for idx in range(stringCount-2, -1, -1):  # F(n) = F(n+2) + F(n+1), n이 인덱스인 점화식을 구현하는 포문
    
    singleNumberCount = 0
    singleNumber = int(string[idx])
    if singleNumber > 0:                    # 요놈이 F(n+1)
      singleNumberCount = decodeCounts[idx+1]

    doubleNumberCount = 0
    doubleNumber = int(string[idx:idx+2])
    if 10 <= doubleNumber <= 26:             # 요놈이 F(n+2)
      doubleNumberCount = decodeCounts[idx+2]

    currentNumberCount = singleNumberCount + doubleNumberCount    # F(n) = F(n+2) + F(n+1)
    decodeCounts[idx] = currentNumberCount                      # F(n)을 디피테이블(decodeCounts)의 현재 인덱스로 최신화

  return decodeCounts[0]

