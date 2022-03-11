# 5
# 문제: 주어진 string s에서, 가장 긴 palindromic substring을 return하여라

# palindromic sub string: 거꾸로 읽어도 같은 알파벳인 문자열
# 두개의 포인터를 잡으면 O(n*n) 시간복잡도로 해결가능
# 다만 서브스트링이 홀수인 경우와 짝수인 경우를 나눠서 두 케이스를 한 포문안에 돌려야함 그래도 O(n*n)

# 그러나 이를 다이내믹 프로그래밍으로 볼 수도 있음
# 상위 배열이 palindromic이면 그것의 하위 배열도 palindromic함.
# 즉 하위배열에서 바텀-업 방식으로 상위 배열이 palindromic한지 체크하면서 진행할 수 있음
# 이를 위해서 1차원인 문자열을 2차원 디피 테이블로 만들어야함
# dpTwoDimension[n][m]은 문자열의 n번째부터 m번째 까지의 부분 문자열임
# 즉 현재 dpTwoDimension 이차원 배열의 위치는 문자열의 부분문자열을 나타냄

# palindromic하면 그 palindromic한 문자열의 길이를 해당 2차원 배열에 적어주면서 진행
# 초기화 작업으로 dpTwoDimension[n][n] = 1, 즉 문자열 하나는 길이 1인 palindromic한 문자열
# 두번째 초기화작업은 문자열 2개짜리가 palindromic한지 체크
# 다음으로 하위배열이 palindromic하면 체크하고자 하는 그 상위 배열의 시작문자와 끝문자가 동일한지만 체크하면 됨


def longestPalindrome(s: str) -> str:
  str_length = len(s)
  dp_table = [[0] * str_length for i in range(str_length)]
  
  for idx in range (str_length):
    dp_table[idx][idx] = 1
  
  for idx in range (str_length -1):
    start_char = s[idx]
    end_char = s[idx+1]
    if start_char == end_char:
      dp_table[idx][idx+1] = 2

  for idx in range (2, str_length):
    row = 0
    col = idx
    while col < str_length:        
      start_char = s[row]
      end_char = s[col]
      prev_count = dp_table[row+1][col-1]
      if start_char == end_char and prev_count != 0:
        dp_table[row][col] = prev_count + 2          
      row += 1
      col += 1
      
  
  max_length = 0
  start_idx = 0
  end_idx = 0
  for row in range (str_length):
    for col in range (str_length):
      crnt_length = dp_table[row][col]
      if max_length < crnt_length:
        max_length = crnt_length
        start_idx = row
        end_idx = col
        
  sub_str = s[start_idx:end_idx+1]

  return sub_str




##################################################################################################################
# 이를 위해서 1차원인 문자열을 2차원 디피 테이블로 만들어야함
# dpTwoDimension[n][m]은 문자열의 n번째부터 m번째 까지의 부분 문자열임
# 즉 현재 dpTwoDimension 이차원 배열의 위치는 문자열의 부분문자열을 나타냄

# [b, a, a, b, c] 의 초기화 상태

#    b a a b c
# b  1 0
# a    1 2
# a      1 0
# b        1 0
# c          1
# 이제 나머지 우측 상단 2차원 배열 공간을 채워야 함 

# 스트링과 이차원배열의 관계
# startChar = string[row]
# endChar = string[col]   요게 포인트

def longestPalind(string: str) -> str:
  stringLength = len(string)
  dpTwoDimension = [[0] * stringLength for _ in range(stringLength)]

  for idx in range(stringLength):       # 초기화 작업으로 dpTwoDimension[n][n] = 1, 즉 문자열 하나는 길이 1인 palindromic한 문자열
    dpTwoDimension[idx][idx] = 1

  for idx in range(stringLength-1):     # 두번째 초기화작업은 문자열 2개짜리가 palindromic한지 체크
    startChar = string[idx]             # 즉 [b, a, a, b, c] 라면, ba, aa, ab, bc 들을 체크 이중 aa만 palindromic함
    endChar = string[idx+1]
    if startChar == endChar:
      dpTwoDimension[idx][idx+1] = 2    # 문자열 길이가 2 이므로
    else:
      dpTwoDimension[idx][idx+1] = 0

  for idx in range(2, stringLength):    # 문자열의 길이가 3인 부분문자열에 대해서 조사하기 때문에 인덱스2부터 체크, 2차원 배열을 생각해야함    
    row = 0                           # 한 row에 대해서 초기화한 값 이후의 컬럼(2부터)에 대해 체크
    col = idx
    while stringLength > col:         # 컬럼이 2차원 배열 넘으면 안되기에
      startChar = string[row]
      endChar = string[col]
      lastSubStringLength = dpTwoDimension[row+1][col-1]    # 2차원 배열의 현재 체크하고자하는 문자열의 위치의 바로 왼쪽 대각선이 현재 문자열의 부분문자열에 해당하고 이것이 palindromic하다면 그 길이가 쓰여있음

      if lastSubStringLength != 0 and startChar == endChar:   # 그 부분 문자열이 0이 아니면 palindromic하다는 뜻이고, 현재 문자열의 시작문자와 끝문자만 체크하면 됨. 그 둘이 같으면 현재 문자열은 palindromic 함 
        dpTwoDimension[row][col] = lastSubStringLength + 2    # 그 부분 문자열보다 현재 부분 문자열이 startChar, endChar 두 문자 만큼 더 기니까 +2 해줌
      else:
        dpTwoDimension[row][col] = 0

      row += 1
      col += 1

  maxNum = 0
  startIdx = 0
  endIdx = 0
  for row in range(stringLength):     # 2차원 배열에서 제일 큰 숫자를 찾음, 부분문자열을 리턴해야해서 인덱스들도 알아야함
    for col in range(stringLength):
      num = dpTwoDimension[row][col]
      if num > maxNum:
        maxNum = num
        startIdx = row
        endIdx = col

  return string[startIdx: endIdx+1]
