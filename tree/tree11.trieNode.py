# 208 구현 

# 211
# 단어가 존재하면 True, 없으면  False를 Return하여라. 여기서 word안의 . 은 모든 letter와 대응 된다.
# 트라이 노드 구현과 트라이노드 서치 문제

# 트라이 노드란 검색어 자동 완성처럼, 각 노드에 알파벲을 할당하여 단어를 트리 노드로 구현하는 것
# 이때 각 노드는 다음 노드의 알파벳에 해당하는 노드를 가지고 있고, 그 단어가 그 노드에서 끝나는지 여부를 알려주는 불리언을 가진다.
# 다음 노드의 알파벳에 해당하는 노드를 해쉬맵으로 설정
# 현재 노드의 다음노드가 단어의 마지막이라면, 현 노드는 다음 노드의 알파벳을 해쉬맵에 가지고 있고, 다음 노드는 isEnd = True 값을 가지게 됨


class TrieNode:
  def __init__(self):
    self.isEnd = False
    self.links = {}


class Trie:
  def __init__(self):
    self._root = TrieNode()   
    
  def _recurAdd(self,node:TrieNode, word:str) -> None:
    if len(word) == 0:
      node.isEnd = True
      return
    
    ch = word[0]
    next_link = node.links.get(ch)
    if next_link is None:      
      node.links[ch] = TrieNode()
      next_link = node.links[ch]
    self._recurAdd(next_link,word[1:])
    

  def add(self, word: str) -> None:
    if len(word) == 0:
      return
    
    self._recurAdd(self._root,word)
    
    
  def _recurSearch(self, node:TrieNode, word: str) -> bool:    
    if len(word) == 0:
      isEnd = node.isEnd
      return isEnd
    
    ch = word[0]
    if ch == '.':
      letters = node.links.keys()
      for key in letters:
        ret = self._recurSearch(node.links[key],word[1:])
        if ret is True:
          return True
      return False       
      
    else:
      next_link = node.links.get(ch)
      if next_link:
        return self._recurSearch(next_link,word[1:])
      return False


  def search(self, word: str) -> bool:
    if len(word) == 0:
      return True
    
    return self._recurSearch(self._root,word)


trie = Trie()
trie.add('baby')
trie.add('ball')
trie.add('tree')
trie.add('trie')

print('baby',trie.search('baby'))
print('ba..',trie.search('ba..'))
print('.ree',trie.search('.ree'))
print('nocope',trie.search('nocope'))

###################################################################


class TrieNode:
  def __init__(self):
    self.isEnd = False
    self.nextCharNode = {}


class Trie:
  def __init__(self):
    self.root = TrieNode()          # 입력한 모든 단어들의 루트 노드, 이 아래에 모든 단어들이 연결되어 있음

  def add(self, node: TrieNode, word: str):
    if len(word) == 0:
      return

    self._recurAdd(self.root, word)

  def _recurAdd(self, node: TrieNode, word: str):
    if len(word) == 0:
      node.isEnd = True
      return

    c = word[0]
    nextNode = node.nextCharNode.get(c)
    if nextNode is None:
      node.nextCharNode[c] = TrieNode()
      nextNode = node.nextCharNode[c]
    self._recurAdd(nextNode, word[1:])


  def search(self, node: TrieNode, word: str) -> bool:
    if len(word) == 0:
      return True

    return self._recurSearch(self.root, word)

  def _recurSearch(self, node: TrieNode, word: str) -> bool:
    if len(word) == 0:
      isEnd = node.isEnd
      return isEnd

    
    c = word[0]
    if c == '.':      # ba.. 이런식으로 와일드 카드가 들어왔을때
      letters = node.nextCharNode.keys()    # 모든 다음 노드들의 키를 가져와서
      for c in letters:                   # 반복문 돌림
        result = self._recurSearch(node.nextCharNode.get(c), word[1:])   # 각 노드에 대해 재귀적으로 호출, 현재 확인한 알파벳의 다음 알파벳부터 word 입력
        if result is True:
          return True
      return False

    else:         # baby 처럼 와일드 카드 아닐때 
      nextNode = node.nextCharNode.get(c)
      if nextNode:
        return self._recurSearch(nextNode, word[1:0])
      return False    # 다음 앞바벳에 대응하는 노드가 없으면 찾는 단어가 없으니 False 리턴
    
    