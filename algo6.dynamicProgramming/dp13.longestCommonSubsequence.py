# 1143
# 문제: text1과 text2의 longest common subsequence의 길이를 구하여라
# subarray는 원소들이 연속적이지만 subsequence는 꼭 연속적일 필요 없음 
# 이 문제는 스크린샷 이미지를 봐야함

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.


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




###########################################################################
# 상위문제와 하위문제로 나누자
# 더 작게 쪼개기 위해서 문자열의 마지막 알파벳에 집중하고, 더 작은 문제는 무엇일지 고민하며 점화식을 만들어야함
# dp 문제는 가장 끝 원소를 보면서 문제를 쪼개나가야함
# DP(m, n) = if A[m] == B[n]: DP(m-1, n-1) + 1  else: max(DP(m-1, n), DP(m, n-1))
# 각각의 누적 문자열로 이루어진 2차원 배열을 만들어야함

# [abdcg, bdag]
# dp(abdcg, bdag) = max( dp(abdc, bda) + 1, dp(abdc, bdag), dp(abdcg, bda) ) 요 세개 중에 만약 
# dp(abdc, bda) + 1 는 if A[m] == B[n]: DP(m-1, n-1) + 1 를 표현한 것, 즉 양 문자열의 끝 알파벳이 같을 때, 여기서는 g로 같은 것을 선택했을때 나머지 둘 보다 이것이 더 큰 값이다. +1 들어가기 때문
# 고로 나머지 둘의 케이스는 더 안봐도 됨. 다만 여기서 g로 동일하기 때문에 이는 공통된 문자열이고 +1을 해주는 것임
# dp(abdc, bda) = max( dp(abd, bd) + 1, dp(abd, bda), dp(abdc, bd) ) 일때, if A[m] == B[n] 이  c != a 이므로 dp(abd, bda), dp(abdc, bd) 이 둘로 선택해서 내려가야함
# 이것이 가능한 이유는 subsequence를 구하는 문제게 때문임. 연속되지 않아도 되기에 공통되지 않은 알파벳을 빼줘버린 것임, 그리고 이때 공통된 알파벳이 없기에 +0 임

# DP(m, n) = if A[m] == B[n]: DP(m-1, n-1) + 1  else: max(DP(m-1, n), DP(m, n-1))
# dpTable, 세로축이 stringA, 가로축이 stringB, 해당값은 common subsequence 길이
#             0   (b)  b(d)  bd(a)  bda(g)  
# 0     ''    0    0     0      0       0
# 1      (a)  0    0     0      1       1
# 2     a(b)  0    1     1      1       1
# 3    ab(d)  0    1     2      2       2 
# 4   abd(c)  0    1     2      2       2 
# 5  abdc(g)  0    1     2      2       3 

# 두 문자열의 길이가 각각 m, n 일때 O(m*n) 시간복잡도



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