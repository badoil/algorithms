# 51
# 문제 : 주어진 n을 기반으로 n * n size의 matrix board가 만들어진다. 이 board에 n개의 Queen이 서로를 공격하지 못하는 상태를 모두 return 하여라
# 모든 방법을 구하는 문제라 bt로 풀어봄

# Example 1:
# Input: n = 4
# Output: [[". Q . .",
#           ". . . Q",
#           "Q . . .",
#           ". . Q ."],

#          [". . Q .",
#           "Q . . .",
#           ". . . Q",
#           ". Q . ."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Constraints:
# 1 <= n <= 9



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


[['. Q . . . .', 
  '. . . Q . .', 
  '. . . . . Q', 
  'Q . . . . .', 
  '. . Q . . . ', 
  '. . . . Q .'],

 ['..Q...', '.....Q', '.Q....', '....Q.', 'Q.....', '...Q..'],
 ['...Q..', 'Q.....', '....Q.', '.Q....', '.....Q', '..Q...'],
 ['....Q.', '..Q...', 'Q.....', '.....Q', '...Q..', '.Q....']]





#########################################################################
# 체스판에 퀸1을 놓는 모든 경우 n^2, 각 경우에 대해서
# 퀸2를 퀸1과 서로 공격하지 못하게 놓는 경우 탐색
# 한 레벨 더 가지치면 위 레벨의 한 경우에 대해서 다음 레벨은 n^2 경우가 생김
# 퀸n을 다른 퀸들과 서로 공격하지 못하게 놓는 경우 탐색

# 퀸의 특성상 같은 row 에 있을 수 없음 
# 각 row에 하나의 퀸만 올 수 있음
# 그러면 한 레벨에서 퀸을 놓을 수 있는 경우의 수는 한 row에 대해서 퀸을 놓을 수 있는 경우의 수를 의미하고 이는 n

# 그런데 이때 row 는 이미 각 row에 하나의 퀸만 두면서 진행했기에 체크 안해도됨
# col과 대각방향 체크해야함



class Queen:
  def solution(self, num: int):
    self._results = []
    self._num = num

    self._colSet = set()          # 퀸의 위치가 column 에서 겹치는지 확인하기위해, 기존 퀸들의 컬럼 위치 저장
    self._diagonalMinus = set()   # 퀸의 위치가 좌상~우하 방향으로 겹치는지 확인하기위해, 기존 퀸들의 대각위치 저장, hashset으로 만들기 때문에 O(1) 시간복잡도 
    self._diagonalPlus = set()    # 퀸의 위치가 우상~좌하 방향으로 겹치는지 확인하기위해, 기존 퀸들의 대각위치 저장

    for col in range(num):    # 한 row 에 대해서 각 컬럼을 체크, 
      self._bt(0, col, [])    # row=0, col=0 이라면, 이에 대해서 다음 레벨을 탐색

    return self._results


  def _stringMaker(self, col: int):
    crtRow = ['.'] * (self._num)
    crtRow[col] = 'Q'
    return ''.join(crtRow)


  def _bt(self, row: int, col: int, board: List[str]):
    if row == len(self._num) or col == len(self._num):    # 체스판 넘어버림
      return
    if col in self._colSet:
      return                    # 이런 리턴이 백트래킹을 하는 부분임. 해당사항 없으니까 다시 위 레벨로 돌아가 탐색 계속 진행
    
    diaInfo1 = row-col    # 좌상~우하 방향에서 겹치는 확인용, 이 값이 이미 있으면 대각방향으로 공격가능한 기존 퀸이 있다는 의미
    diaInfo2 = row+col    # 우상~좌하 방향에서 겹치는 확인용, 이 값이 이미 있으면 대각방향으로 공격가능한 기존 퀸이 있다는 의미
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

    for col in range(self._num):      # 다음 퀸을 놓을 다음 row 탐색
      self._bt(row+1, col, board)


    self._colSet.remove(col)              # row=0, col=0 에 대해서 탐색했는데, 이때 n개의 퀸을 놓을 수 있는 경우가 없었다면 이때 저장했었던 정보들을 다 지워야함
    self._diagonalMinus.remove(diaInfo1)  # 그래야 다음 탐색이 제로베이스에서 다시 시작
    self._diagonalPlus.remove(diaInfo2)
    board.pop()