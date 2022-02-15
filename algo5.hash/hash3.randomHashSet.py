# 380 좋은 문제임
# O(1)의 insert, remove, random return 구현
# 문제: O(1) Insert, Remove, Random Return을 지원하는 hash Set을 구현하여라
# 해쉬를 이용하므로 O(1) 시간복잡도
# 랜덤 초이스 때문에 배열도 이용해야하고, 해쉬테이블과 배열을 맞춰주면서 가야함

import random

class InsertRemoveRandom:
  def __init__(self):
    self._hashTable = {}
    self._array = []          # 여기서 배열을 쓰는 이유는 랜덤 초이스를 해줘야하기 때문, 그래서 insert, remove에서 해쉬테이블과 배열을 맞춰주면서 가야함


  def insert(self, val: int) -> bool:
    idx = self._hashTable.get(val)
    if idx is not None:
      return False

    idx = len(self._array)      # 새로운 수가 들어갈 곳은 기존 배열의 마지막
    self._hashTable[val] = idx  # 여기서 idx는 배열의 길이, 즉 배열에 추가될 수의 인덱스
    self._array.append(val)     # 배열의 마직막에 수 추가, 이러면 해쉬테이블의 idx와 배열의 실제 인덱스가 맞춰짐 
    return True

  def remove(self, val: int) -> bool:
    idx = self._hashTable.get(val)
    if idx is None:
      return False

    lastVal = self._array[-1]   # 배열의 마지막 수
    self._array[idx] = lastVal  # 지우고자 하는 수를 배열의 마지막 수로 바꿈
    self._hashTable[lastVal] = idx

    self._array.pop()
    self._hashTable.pop(val)    # 해쉬테이블의 팝 방법
    return True

  def getRandom(self) -> int:
    return random.choice(self._array)
    
