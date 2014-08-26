import unittest
from spell_suggester import SpellSuggester

class TestSpellSuggester(unittest.TestCase):

    def setUp(self):
        self.s = SpellSuggester()
        self.s.dict = {}
        word, freq = ['test', 20]
        self.s.add_word(word,freq)
        word, freq = ['tents', 30]
        self.s.add_word(word,freq)
        word, freq = ['bats', 35]
        self.s.add_word(word,freq)

    def test_add_word(self):
        self.setUp()
        dict = {}
        dict['test'] = 20
        dict['tents'] = 30
        dict['bats'] = 35
        self.assertEqual(self.s.dict, dict)

    def test_trie(self):
        self.setUp()
        root = {}
        root['t'] = {}
        root['b'] = {}
        root['t']['e'] = {}
        root['t']['e']['s'] = {}
        root['t']['e']['n'] = {}
        root['t']['e']['s']['t'] = { None: True }
        root['t']['e']['n']['t'] = {}
        root['t']['e']['n']['t']['s'] = { None: True }
        root['b']['a'] = {}
        root['b']['a']['t'] = {}
        root['b']['a']['t']['s'] = { None: True }
        self.assertEqual(self.s.root, root)

    def test_sort(self):
        self.setUp()
        suggestions = ['test', 'tents', 'bats']
        sorted = self.s.sort_by_freq(suggestions)
        self.assertEqual(sorted,['bats', 'tents', 'test'])

    def test_find(self):
        self.setUp()
        corrections = set(self.s.find_similar('tests'))
        self.assertEqual(corrections, set(['test', 'tents']))
        corrections = set(self.s.find_similar('batsss'))
        self.assertEqual(corrections, set(['bats']))
        corrections = set(self.s.find_similar('batssss'))
        self.assertEqual(corrections, set([]))
        corrections = set(self.s.find_similar('tts'))
        self.assertEqual(corrections, set(['bats', 'tents', 'test']))
        corrections = set(self.s.find_similar('tets',1))
        self.assertEqual(corrections, set(['tents']))
        corrections = set(self.s.find_similar('tets',2))
        self.assertEqual(corrections, set(['test', 'tents', 'bats']))
        corrections = set(self.s.find_similar('asdfasdfasdfas',2))
        self.assertEqual(corrections, set([]))

if __name__ == '__main__':
    unittest.main()
