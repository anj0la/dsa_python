class TrieNode:
    def __init__(self) -> None:
        self.children = [None for _ in range(26)]
        self.is_end_of_word = False
        
        
class Trie:
    def __init__(self) -> None:
        self.root = None
        
        
    def insert(self, word: str) -> None:
        if not self.root:
            self.root = TrieNode()
            
        node = self.root
        
        for char in word:
            i = ord(char) - ord('a')
            if node.children[i] is None:
                node.children[i] = TrieNode()
                
            node = node.children[i]
        
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            i = ord(char) - ord('a')
            if node.children[i] is None:
                return False # The node doesn't exist for the current character
            
            node = node.children[i]
            
        return node.is_end_of_word
    
    def delete(self, word: str) -> bool:
        self._delete_recursive(self.root, word, 0)
    
    def _delete_recursive(self, node: TrieNode, word: str, depth: int = 0) -> bool:
        if node is None:
            return False
        
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            return self._node_has_no_children(node)
        
        char = word[depth]
        i = ord(char) - ord('a')
        child = node.children[i]
        
        should_delete = self._delete_recursive(child, word, depth + 1)
        if should_delete:
            node.children[i] = None
            return self._node_has_no_children(node)
        
        return False
        
    def _node_has_no_children(self, node: TrieNode) -> bool:
        return all(child is None for child in node.children) and not node.is_end_of_word
    
    
if __name__ == '__main__':
    trie = Trie()
    trie.insert('cat')
    trie.insert('car')
    trie.insert('can')
    trie.insert('cattle')
    trie.insert('camel')
    trie.insert('dog')
    trie.insert('dot')
    trie.insert('dots')
    trie.insert('dodge')
    trie.insert('doodle')
    
    print(f'cattle in trie: {trie.search('cattle')}')
    print(f'fries in trie: {trie.search('fries')}')
    print(f'doodle in trie: {trie.search('doodle')}\n')
    
    print('Deleting cattle...')
    trie.delete('cattle')
    print(f'cattle in trie: {trie.search('cattle')}\n')
    
    print('Deleting fries...')
    trie.delete('fries')
    print(f'fries in trie: {trie.search('fries')}\n')
    
    print('Deleting dot...')
    trie.delete('dot')
    print(f'dot in trie: {trie.search('dot')}')
    print(f'dots in trie: {trie.search('dots')}')


