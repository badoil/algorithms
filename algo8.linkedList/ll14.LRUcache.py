# 146
# 문제 :   Least Recently Used (LRU) cache를 구현하여라
# 해시맵과 더블리 링크드 리스트 라는 두가지 자료형의 조합

# key: value, 형태로 저장되는 캐쉬를 만드는데
# maxSize 가 있어서 그걸 넘으면 오버플로우 발생하는 구조
# 캐시 오버 플로우가 났을때, 데이터를 지워주는 규칙이 Least Recently Used (LRU) 임
# 가장 과거에 사용된 데이터를 삭제
# put, get 모두 O(1) 이어야 함, 따라서 해시맵 
# 그런데 해시맵은 가장 과거에 사용된 데이터를 알아낼 수 없기에 이를 해결해야함
# 최근 사용한 데이터 순으로 정렬된 데이터구조 필요
# 더블리 링크드 리스트를 사용하면 사용한지 가장 오래된 데이터와, 가장 최근에 사용한 데이터에 head(past), tail(recent)로부터 O(1)로 접근 가능
# 이제 해시맵과 더블리 링크드 리스트에 구조를 정의하면 됨
# 
# 해시맵 구성은 key(노드의 값): value(노드)
# 더블리 링크드 리스트 구성은 노드의값(value), 해시맵의 키

# 해시맵을 통해서 검색한 그 노드는 가장 최근에 사용된 데이터이므로 더블리 링크드 리스트에서 최신으로 옮겨주는 정렬해줘야함
# 오버플로우가 났을떼, 오버플로우 체크하는 함수를 통해 링크드 리스트에서 헤드 다음 노드를 지워주고, 해시맵에서도 지워줌
# 해시맵에서 지워주기 위해, 링크드 리스트의 노드에는 노드의값(value)뿐만 아니라 그 노드의 해시맵의 키도 저장
# test


'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
''' 


class ListNode:
  def __init__(self, key:int, val: int):
    self.key = key
    self.val = val
    self.left = None
    self.right = None

class LRUCache:
  def __init__(self, capacity: int):
    self._max_cap = capacity
    self._hashmap = {}
    self._list_head = ListNode(-1,-1)
    self._list_tail = ListNode(-1,-1)
    self._list_head.right = self._list_tail
    self._list_tail.left = self._list_head

  def get(self, key: int) -> int:
    value_node = self._hashmap.get(key)
    if value_node:
      self._removeFromList(value_node)
      self._addBack(value_node)
      val = value_node.val
      return val

    else:
      return -1

  def put(self, key: int, value: int) -> None:
    value_node = self._hashmap.get(key)
    if value_node:
      value_node.val = value
      self._removeFromList(value_node)
      self._addBack(value_node)
      return
    value_node = ListNode(key,value)
    self._addBack(value_node)
    self._hashmap[key] = value_node
    
    if self._max_cap<len(self._hashmap):
      lru_node = self._list_head.right
      lru_key = lru_node.key
      self._removeFromList(lru_node)
      self._hashmap.pop(lru_key)

  
  def _addBack(self, node:ListNode):
    tail_left = self._list_tail.left
    
    tail_left.right = node
    node.left = tail_left
    
    self._list_tail.left = node
    node.right = self._list_tail
    
    
  def _removeFromList(self,node:ListNode):
    left_node = node.left
    right_node = node.right

    left_node.right = right_node
    right_node.left = left_node


lru_cache = LRUCache(4)
lru_cache.put(1,10)
lru_cache.put(2,20)
lru_cache.put(3,30)
lru_cache.put(4,40)
print(1,lru_cache.get(1)) #key 1 renew

lru_cache.put(5,50)
print(1,lru_cache.get(1))
print(2,lru_cache.get(2))
print(3,lru_cache.get(3))
print(4,lru_cache.get(4))
print(5,lru_cache.get(5))

'''
1 10
1 10
2 -1
3 30
4 40
5 50
'''