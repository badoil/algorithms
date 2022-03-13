# 79
# 문제 : 주어진 2차원 배열 alphabet Matrix에서 연결되는 word가 있는지를 찾아라

# [[A B D],
# [B D C],
# [S A B]]

# 예제: word = [SBDCB]
# 답 :  True

# Example 1:
# Input: board = 
# [["A","B","C","E"],
#  ["S","F","C","S"],
#  ["A","D","E","E"]], 
# word = "ABCCED"
# Output: true

# Example 2:
# Input: board = 
# [["A","B","C","E"],
#  ["S","F","C","S"],
#  ["A","D","E","E"]], 
# word = "SEE"
# Output: true

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


from typing import List

class WordSearch:
  def find(self, matrix: List[List[str]], word: str) -> bool:
    if len(word) == 0:
      True
    rows = len(matrix)
    if rows == 0:
      return False
    cols = len(matrix[0])
    if cols == 0:
      return False
    
    #copy to member objects
    self.__word = word
    self.__matrix = matrix
    self.__mark = [[False for x in range(cols)] for y in range(rows)]
    
    for y in range(rows):
      for x in range(cols):
        ret = self.__bt(y,x,0)
        if ret == True:
          return True
      
    return False
  
  
  def __bt(self, y:int, x:int , idx:int):
    #exit conditions
    if idx == len(self.__word):
      return True
    elif y<0 or y==len(self.__matrix): #out of range
      return False
    elif x<0 or x==len(self.__matrix[0]): #out of range
      return False    
    elif self.__mark[y][x]==True: #marked elem
      return False
    elif self.__matrix[y][x] != self.__word[idx]: #not matched
      return False
    
    #process
    self.__mark[y][x]= True
    
    if self.__bt(y-1,x,idx+1):
      return True
    elif self.__bt(y,x+1,idx+1):
      return True
    elif self.__bt(y+1,x,idx+1):
      return True
    elif self.__bt(y,x-1,idx+1):
      return True   
  
    self.__mark[y][x]=False  #unmark
    
    return False

wrdSearch = WordSearch()


matrix = [['A','B','D'],['B','D','C'],['S','A','B']]
word = "SBDCB"

wrdSearch.find(matrix=matrix,word=word)




######################################################################################
# Example 1:
# Input: board = 
# [["A","B","C","E"],
#  ["S","F","C","S"],
#  ["A","D","E","E"]], 
# word = "ABCCED"
# Output: true

# 2차원 매트릭스에서 상하좌우 로 움직임


class WordSearching:
  def solution(self, wordsMatrix: List[List[int]], word: str) -> bool:
    rows = len(word)
    cols = len(word[0])
    
    if rows == 0:
      return False
    if cols == 0:
      return False
    if len(word) == 0:
      return True

    self._wordsMatrix = wordsMatrix
    self._word = word
    self._mark = [[False * (cols)] for _ in range(rows)]

    for row in range(rows):
      for col in range(cols):
        result = self._bt(row, col, 0)
        if result == True:
          return True
    return False

  def _bt(self, row: int, col: int, idx: int):
    if idx == len(self._word):    # 아패의 조건 다 해당안되면서 다음 재귀를 호출한 것이기 때문에 매치되는 문자열이 2차원 배열에 있다는 의미
      return True
    elif row < 0 or row == len(self._wordsMatrix):    # 2차원 배열 범위 벗어남
      return False 
    elif col < 0 or col == len(self._wordsMatrix[0]): # 2차원 배열 범위 벗어남
      return False
    elif self._mark[row][col] == True:        # 현재 탐색에서 이미 지나온 곳
      return False
    elif self._wordsMatrix[row][col] != self._word[idx]:  # 문자가 매치 안됨
      return False

    self._mark[row][col] = True   # 현재위치 문자 확인한 것으로 체크

    if self._bt(row+1, col, idx+1):   # 상하좌우 체크
      return True
    elif self._bt(row-1, col, idx+1):
      return True
    elif self._bt(row, col+1, idx+1):
      return True
    elif self._bt(row, col-1, idx+1):
      return True

    self._mark[row][col] = False    # 현재 탐색결과 매치되는 문자열 없었으므로, 다음 탐색을 위해서 다시 원위치 시킴
    return False

