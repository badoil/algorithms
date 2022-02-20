# 1143
# 문제: text1과 text2의 longest common subsequence의 길이를 구하여라
# 이 문제는 스크린샷 이미지를 봐야함

# 상위문제와 하위문제로 나누자
# dp 문제는 가장 끝 원소를 보면서 문제를 쪼개나가야함
# DP(m, n) = if A[m] == B[n]: DP(m-1, n-1) + 1  else: max(DP(m-1, n), DP(m, n-1))
# 각각의 누적 문자열로 이루어진 2차원 배열을 만들어야함

# 두 문자열의 길이가 각각 m, n 일때 O(m*n) 시간복잡도

def longestCommonSubsequence(text1: str, text2: str) -> int:
  dp_table = [[0]*(len(text1)+1) for j in range(len(text2)+1)]
  
  for rowIdx in range(1,len(dp_table)):
    prev_row = rowIdx - 1
    char2 = text2[rowIdx-1]
    for colIdx in range(1,len(dp_table[rowIdx])):
      prev_col = colIdx-1
      char1 = text1[colIdx-1]
      
      dp = 0
      if char1 == char2:
        dp = dp_table[prev_row][prev_col] + 1
      else:
        dp = max(dp_table[prev_row][colIdx], dp_table[rowIdx][prev_col])        
      dp_table[rowIdx][colIdx] = dp
  return dp_table[-1][-1]  #return last dp table elem 


print(longestCommonSubsequence(text1='abdcg',text2='bdag'))


  #########################################################################




def lngCommonSubsequence(stringA: str, stringB: str) -> int:
  dpTable =[[0]*(len(stringB)+1) for _ in range(len(stringA)+1)]      # 어떤 문자열을 행에, 아니면 열에 배치할지 정하기
                                                                      # 0번째 행과 열이 모두 0이기 때문에 디피테이블 만드는 것이 초기화도 포함된 셈
  for rowIdx in range(1, len(dpTable)):                           # 초기화된 0번째 행과 열 다음인 1번째 부터 시작
    for colIdx in range(1, len(dpTable[rowIdx])):
      prevRowIdx = rowIdx-1
      prevColIdx = colIdx-1

      charA = stringA[prevRowIdx]         
      charB = stringB[prevColIdx]


      dpValue = 0
      if charA == charB:    # 두 단어가 같기 때문에 공통된 단어가 1개 있는 셈, +1 해주는 거임
        dpValue = dpTable[prevRowIdx][prevColIdx] + 1

      else:
        dpValue = max(dpTable[rowIdx][prevColIdx], dpTable[prevRowIdx][colIdx])     # 점화식 중에 max(DP(m-1, n), DP(m, n-1))인 부분. 2차원 배열에서 구하고자하는 위치 바로 왼쪽 칸과 바로 위칸의 값들

      dpTable[rowIdx][colIdx] = dpValue

  return dpTable[-1][-1]

print(lngCommonSubsequence(stringA='abdcg',stringB='bdag'))