class TrieNode:
    def __init__(self):
        self.nodes = {}  # map char to TrieNode
        self.is_leaf = False

    def insert_many(self, words: list[str]):
        for word in words:
            self.insert(word)

    def insert(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def find(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def delete(self, word: str):
        def _delete(curr: 'TrieNode', word: str, i: int):
            # base case
            if i == len(word):  # fixed = to ==
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0

            char = word[i]
            char_node = curr.nodes.get(char)
            if not char_node:
                return False

            delete_curr = _delete(char_node, word, i + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0

            return False

        _delete(self, word, 0)


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        trie = TrieNode()
        trie.insert_many(strs)

        # traverse down the trie while only one branch and not a leaf
        prefix = ""
        curr = trie
        while len(curr.nodes) == 1 and not curr.is_leaf:
            char = next(iter(curr.nodes))
            prefix += char
            curr = curr.nodes[char]

        return prefix