import operator
import csv

class SpellSuggester:
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
        corrections = set(self.find_similar(word,3))
        sorted_corrections = self.sort_by_freq(corrections)
        return  sorted_corrections

    def sort_by_freq(self, candidates):
        corrections = {}
        for word in candidates:
            corrections[word] = self.dict[word]
        sorted_corrections = sorted(corrections.iteritems(), key=operator.itemgetter(1), reverse=True)
        return [k for k,v in sorted_corrections]

    # modified version of code written by Kevin Stock
    # bitbucket.org/teoryn/spell-checker/
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

