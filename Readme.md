Design
==========
The goal is to implement a spelling suggester that returns a set of appropriate suggested words, sorted by descending frequency.

Suggested words:
* must have a Levenshtein distance of 1 or 2 from the misspelled word
* must exist in the provided dictionary

Algorithms
-------

Four possible algorithms were found:

* Levenshtien - O(n^2 * s)
* Norwig - O(n^d)
* Levenshtein Automata - O(n * s)
* Norwig combined with trie - O(n * t)

n = maximum word length
s = dictionary size
d = max allowable Levenshtein distance
t = number of nodes in Trie data structure (as determined by the dictionary size)

Also, the trie algorithm has greater memory requirements.

For this scenario, we have a dictionary size of about 11k, a maximum word length of 17 characters, and a max allowable distance of 2. Although the Levenshtien approach would be simplest to implement, it really is not practical unless we are dealing with very high allowable distances and a small dictionary.

The Automata is superior, but beyond the scope of this task due to its complex implementation.

The trie approach is more complex and requires significantly more memory, so we don't want to do that either.

Assuming this was used for a real language, we would have a much larger dictionary. The Norwig approach is the only one unaffected by the dictionary size.

We can also cache the results into a query -> suggestions map to speed up future queries. Keep often-requested queries in this cache, and clear the rare ones.


Instructions
==========

Attributions
==========

Thanks to http://norvig.com/spell-correct.html
https://bitbucket.org/teoryn/spell-checker/src/tip/spell_checker.py
http://stevehanov.ca/blog/index.php?id=114

Questions
=======
1. How would the code perform if the size of the dictionary were 1 million words?
Fine. The norwig approach stores the dictionary in a hash table with constant time lookup. Although the execution time grows with distance and word length, it is independent of the dictionary time (with the exception of initial startup.)

2. How would the code perform with an edit distance of 3?
The cod would perform roughly an order of magnitude slower. To handle a higher edit distance, we would want to switch to the trie approach.

3. How does the code perform on long queries versus short queries and why?
A query twice as long will take about 4 times longer to run with an edit distance of 2. The Norwig approach generates all possible 2-distance strings, and the number of permutations increases as the length of the string increases.
