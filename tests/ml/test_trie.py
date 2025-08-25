import unittest

from src.ml.trie import Trie


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        pass

    def test_trie_build_search(self):
        self.trie.insert("hello")
        self.trie.insert("book")
        self.trie.insert("04world78_")
        self.trie.insert("elephone")
        self.trie.insert("typo_word1203")

        self.assertFalse(self.trie.search("helpeR"))
        self.assertTrue(self.trie.search("04world78"))
        self.assertTrue(self.trie.search("typoWord1203"))

