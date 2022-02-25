# 51
# 문제 : 주어진 n을 기반으로 n * n size의 matrix board가 만들어진다. 이 board에 n개의 Queen이 서로를 공격하지 못하는 상태를 모두 return 하여라
# 모든 방법을 구하는 문제라 bt로 풀어봄

# n=1, 2, 3... 각각의 케이스들을 생각해보는게 좋음

# 잘 이해가 안감


from typing import List


class NQueens:
  def solve(self, n: int) -> List[List[str]]:
    self.__results = []
    self.__col_set = set()  #column duplicates
    self.__diag_set1 = set() #row-col duplicates
    self.__diag_set2 = set() #row+col duplicates
    self.__n = n  #length
    
    for x in range(n):
      self.__bt(0,x,[])
    
    return self.__results
    
  #python str is immutable
  def __create_str_row(self, col:int) -> str:    
    str_list = ['.']* self.__n
    str_list[col] = 'Q'    
    return ''.join(str_list)  
  
  def __bt(self, row:int, col:int, board:List[str]):    
    #exit conditions
    if row==self.__n or col==self.__n:
      return
    if col in self.__col_set:
      return
    diag1_info = row-col
    diag2_info = row+col
    if diag1_info in self.__diag_set1:
      return
    if diag2_info in self.__diag_set2:
      return 
    
    #process
    str_line = self.__create_str_row(col)
    board.append(str_line)
    
    if len(board) == self.__n:
      self.__results.append(board.copy())
      board.pop()
      return
    
    #duplicates sets
    self.__col_set.add(col)
    self.__diag_set1.add(diag1_info)
    self.__diag_set2.add(diag2_info)
    
    #recursive calls
    for x in range(self.__n):
      self.__bt(row+1,x,board)      
    
    #duplicates sets pop
    self.__diag_set2.remove(diag2_info)
    self.__diag_set1.remove(diag1_info)
    self.__col_set.remove(col)
    board.pop()

nQsolver = NQueens()

nQsolver.solve(6)


[['.Q....', '...Q..', '.....Q', 'Q.....', '..Q...', '....Q.'],
 ['..Q...', '.....Q', '.Q....', '....Q.', 'Q.....', '...Q..'],
 ['...Q..', 'Q.....', '....Q.', '.Q....', '.....Q', '..Q...'],
 ['....Q.', '..Q...', 'Q.....', '.....Q', '...Q..', '.Q....']]



##################################################################

class Queen:
  def solution(self, num: int):
    self._results = []
    self._num = num

    self._colSet = set()
    self._diagonalMinus = set()
    self._diagonalPlus = set()

    for col in range(num):
      self._bt(0, col, [])

    return self._results


  def _stringMaker(self, col: int):
    crtRow = ['.'] * (self._num)
    crtRow[col] = 'Q'
    return ''.join(crtRow)


  def _bt(self, row: int, col: int, board: List[str]):
    if row == len(self._num) or col == len(self._num):
      return
    if col in self._colSet:
      return
    
    diaInfo1 = row-col
    diaInfo2 = row+col
    if diaInfo1 in self._diagonalMinus:
      return
    if diaInfo2 in self._diagonalPlus:
      return


    crtRow = self._stringMaker(col)
    board.append(crtRow)

    if len(board) == self._num:
      self._results.append(board.copy())
      board.pop()
      return


    self._colSet.add(col)
    self._diagonalMinus.add(diaInfo1)
    self._diagonalPlus.add(diaInfo2)

    for col in range(self._num):
      self._bt(row+1, col, board)


    self._colSet.remove(col)
    self._diagonalMinus.remove(diaInfo1)
    self._diagonalPlus.remove(diaInfo2)
    board.pop()