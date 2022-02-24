# 문제 : 주어진 2차원 배열 alphabet Matrix에서 연결되는 word가 있는지를 찾아라
#예제: word = [SBDCB]
# [[A B D],
# [B D C],
# [S A B]]
# 답 :  True

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


##################################################################

class WordSearching:
  def solution(self, wordsMatrix: List[List[int]], word: str) -> bool:
    rows = len(word)
    cols = len(word[0])
    
    if rows == 0:
      return 0
    if cols == 0:
      return 0
    if len(word) == 0:
      return 0

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
    if idx == len(self._wordsMatrix):
      return True
    elif row < 0 or row == len(self._wordsMatrix):
      return False 
    elif col < 0 or col == len(self._wordsMatrix[0]):
      return False
    elif self._mark[row][col] == True:
      return False
    elif self._wordsMatrix[row][col] != self._word[idx]:
      return False

    self._mark[row][col] = True

    if self._bt(row+1, col, idx+1):
      return True
    elif self._bt(row-1, col, idx+1):
      return True
    elif self._bt(row, col+1, idx+1):
      return True
    elif self._bt(row, col-1, idx+1):
      return True

    self._mark[row][col] = False
    return False

