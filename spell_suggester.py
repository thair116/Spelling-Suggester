import operator
import csv
#
#
# import unittest
#
# class TestSpellSuggester(unittest.TestCase):
#
#     def setUp(self):
#         self.s = SpellSuggester()
#
#     def test_add_to_dict(self):
#         self.s.dict = {}
#         word, freq = ['test', 20]
#         self.s.add_to_dict(word,freq)
#         dict = {}
#         dict['test'] = 20
#         self.assertEqual(self.s.dict, dict)
#
#     def test_defined(self):
#         self.s.dict = {}
#         self.s.dict['test'] = 20
#         self.assertEqual(self.s.defined('test'), True)
#         self.assertEqual(self.s.defined('not'), False)
#
#     def test_splits(self):
#         word = 'test'
#         splits = [('', 'test'), ('t', 'est'), ('te', 'st'), ('tes', 't'), ('test', '')]
#         self.assertEqual(self.s.splits(word), splits)
#
#     def test_deletions(self):
#         splits = [('', 'test'), ('t', 'est'), ('te', 'st'), ('tes', 't'), ('test', '')]
#         deletions = ['est', 'tst', 'tet', 'tes']
#         self.assertEqual(self.s.deletions(splits), deletions)
#
#     def test_changes(self):
#         splits = [('', 'test'), ('t', 'est'), ('te', 'st'), ('tes', 't'), ('test', '')]
#         changes = ['aest', 'best', 'cest', 'dest', 'eest', 'fest', 'gest', 'hest', 'iest', 'jest', 'kest', 'lest', 'mest', 'nest', 'oest', 'pest', 'qest', 'rest', 'sest', 'uest', 'vest', 'west', 'xest', 'yest', 'zest', "'est", '-est', 'tast', 'tbst', 'tcst', 'tdst', 'tfst', 'tgst', 'thst', 'tist', 'tjst', 'tkst', 'tlst', 'tmst', 'tnst', 'tost', 'tpst', 'tqst', 'trst', 'tsst', 'ttst', 'tust', 'tvst', 'twst', 'txst', 'tyst', 'tzst', "t'st", 't-st', 'teat', 'tebt', 'tect', 'tedt', 'teet', 'teft', 'tegt', 'teht', 'teit', 'tejt', 'tekt', 'telt', 'temt', 'tent', 'teot', 'tept', 'teqt', 'tert', 'tett', 'teut', 'tevt', 'tewt', 'text', 'teyt', 'tezt', "te't", 'te-t', 'tesa', 'tesb', 'tesc', 'tesd', 'tese', 'tesf', 'tesg', 'tesh', 'tesi', 'tesj', 'tesk', 'tesl', 'tesm', 'tesn', 'teso', 'tesp', 'tesq', 'tesr', 'tess', 'tesu', 'tesv', 'tesw', 'tesx', 'tesy', 'tesz', "tes'", 'tes-']
#         self.assertEqual(self.s.changes(splits), changes)
#
#     def test_additions(self):
#         splits = [('', 'test'), ('t', 'est'), ('te', 'st'), ('tes', 't'), ('test', '')]
#         insertions = ['atest', 'btest', 'ctest', 'dtest', 'etest', 'ftest', 'gtest', 'htest', 'itest', 'jtest', 'ktest', 'ltest', 'mtest', 'ntest', 'otest', 'ptest', 'qtest', 'rtest', 'stest', 'ttest', 'utest', 'vtest', 'wtest', 'xtest', 'ytest', 'ztest', "'test", '-test', 'taest', 'tbest', 'tcest', 'tdest', 'teest', 'tfest', 'tgest', 'thest', 'tiest', 'tjest', 'tkest', 'tlest', 'tmest', 'tnest', 'toest', 'tpest', 'tqest', 'trest', 'tsest', 'ttest', 'tuest', 'tvest', 'twest', 'txest', 'tyest', 'tzest', "t'est", 't-est', 'teast', 'tebst', 'tecst', 'tedst', 'teest', 'tefst', 'tegst', 'tehst', 'teist', 'tejst', 'tekst', 'telst', 'temst', 'tenst', 'teost', 'tepst', 'teqst', 'terst', 'tesst', 'tetst', 'teust', 'tevst', 'tewst', 'texst', 'teyst', 'tezst', "te'st", 'te-st', 'tesat', 'tesbt', 'tesct', 'tesdt', 'teset', 'tesft', 'tesgt', 'tesht', 'tesit', 'tesjt', 'teskt', 'teslt', 'tesmt', 'tesnt', 'tesot', 'tespt', 'tesqt', 'tesrt', 'tesst', 'testt', 'tesut', 'tesvt', 'teswt', 'tesxt', 'tesyt', 'teszt', "tes't", 'tes-t', 'testa', 'testb', 'testc', 'testd', 'teste', 'testf', 'testg', 'testh', 'testi', 'testj', 'testk', 'testl', 'testm', 'testn', 'testo', 'testp', 'testq', 'testr', 'tests', 'testt', 'testu', 'testv', 'testw', 'testx', 'testy', 'testz', "test'", 'test-']
#         self.assertEqual(self.s.insertions(splits), insertions)


# unittest.main()



class SpellCheck:
    def __init__(self):
        self.root = {}
        self.dict = {}

    def add_word(self, word, freq):
        # add to the dictionary to store frequencies
        self.dict[word] = freq

        # add to the trie
        node = self.root
        for l in word:
            if l not in node:
                node[l] = {}
            node = node[l]
        node[None] = True

    def suggestions(self, word):
        corrections = set(self.find_similar(word,1) + self.find_similar(word,2))
        sorted_corrections = self.sort_by_freq(corrections)
        return  sorted_corrections

    def find_similar(self, word, max_dist = 2, node = None, built = ''):
        ret = []
        if max_dist < 0:
            return ret
        if not node:
            node = self.root
            # Inserts
        for l in node:
            if l:
                ret.extend(self.find_similar(word,max_dist-1,node[l],built+l))
            # Stop recursing if there are no more letters in word
        if not word:
            if None in node:
                ret.append(built)
            return ret
            # No edit
        if word[0] in node:
            ret.extend(self.find_similar(word[1:],max_dist,node[word[0]],built+word[0]))
            # Early exit when possible
        if max_dist == 0:
            return ret
            # Deletes
        ret.extend(self.find_similar(word[1:],max_dist-1,node,built))
        # Replaces
        for l in node:
            if l != word[0] and l:
                ret.extend(self.find_similar(word[1:],max_dist-1,node[l],built+l))
        return ret

    def sort_by_freq(self, candidates):
        corrections = {}
        for word in candidates:
            corrections[word] = self.dict[word]
        sorted_corrections = sorted(corrections.iteritems(), key=operator.itemgetter(1), reverse=True)
        return [k for k,v in sorted_corrections]

################ Testing code from here on ################

def spelltest(bias=None, verbose=False):
    t = SpellCheck()
    dict_name = "word_frequency.csv"
    query_name = "misspelled_queries.csv"

    with open(dict_name) as f:
        reader = csv.reader(f)
        for row in reader:
            word = row[0].lower()
            freq = row[1]
            t.add_word(word,freq)
    with open(query_name) as f:
        reader = csv.reader(f)
        for row in reader:
            word = row[0].lower()
            suggestions = t.suggestions(word)
            print "* " + word + ": " + str(suggestions)

spelltest()
# run()
