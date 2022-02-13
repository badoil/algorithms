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

#####################################################


class Tries:
  def __init__(self):
    self._root = TrieNode()

  def _recurAdd(self, node: TrieNode, word: str) -> None:
    if len(word) == 0:
      node.isEnd = True
      return
    
    char = word[0]
    nextLinkNode = node.links.get(char)
    if nextLinkNode is None:
      node.links[char] = TrieNode()
      nextLinkNode = node.links[char]

    self._recurAdd(nextLinkNode, word[1:])

  def add(self, word:str):
    if len(word) == 0:
      return
    self._recurAdd(self._root, word)


  def _recurSearch(self, node: TrieNode, word:str) -> bool:
    if len(word) == 0:
      return node.isEnd

    char = word[0]
    if char == '.':
      keys = node.links.keys()
      for key in keys:
        nextLinkNode = node.links[key]
        result = self._recurSearch(nextLinkNode, word[1:])
        if result is True:
          return True
      return False

    else:
      nextLinkNode = node.links[char]
      if nextLinkNode:
        return self._recurSearch(nextLinkNode, word[1:])
      return False


  def search(self, word:str) -> bool:
    if len(word) == 0:
      return True

    return self._recurSearch(self._root, word)