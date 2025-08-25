###################################################################
# A generic trie class to store a collection of words (dict) into
# a binary tree format
# 1 .support alphabetic and numeric characters only
# 2. case-insensitive comparison (e.g. AB123456789 = ab123456789)
###################################################################

class Trie:
    def __init__(self):
        # support both alphabetic (0-25) and numeric (26-35)
        self.children = [None] * 36
        self.is_end = False

    def insert(self, word):
        word = word.lower()
        node = self
        for c in word:
            if c.isalpha():
                idx = ord(c) - ord('a')
            elif c.isdigit():
                idx = ord(c) - ord('0') + 26
            # skip for other special characters
            else:
                continue
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]

        node.is_end = True

    def search(self, word):
        word = word.lower()
        node = self
        for c in word:
            if c.isalpha():
                idx = ord(c) - ord('a')
            elif c.isdigit():
                idx = ord(c) - ord('0') + 26
            # skip for other special characters
            else:
                continue
            if node.children[idx] is None:
                return False
            node = node.children[idx]

        return node.is_end
