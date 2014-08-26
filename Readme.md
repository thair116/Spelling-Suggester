Instructions
==========
* Run with `python main.py`
* Run tests with `python test_spell_suggester.py`

Attributions
==========

With special thanks given to:

Peter Norvig norvig.com/spell-correct.html
Kevin Stock bitbucket.org/teoryn/spell-checker/
Steve Hanov stevehanov.ca/blog/index.php?id=114
Vladimir Levenshtein en.wikipedia.org/wiki/Levenshtein_distance

For helping me build a spelling suggester while also teaching me more about tries and bloom filters :)

Questions
=======
1. How would the code perform if the size of the dictionary were 1 million words?

The benefit of this code over Norvig's algorithm is that by using a trie, we only check the permutations of letters which could possibly lead to a real word. With a sparse dictionary, the number of nodes is orders of magnitude smaller than the full set of permutations ((~54n + 25) ^ e, where n is word length and d is allowable distance). As the dictionary increases, the node density also increases, but it will always remain significantly lower than this upper bound ("wqx" will never exist in any word).

However, its important to note that the trie structure requires a large amount of instantaneous memory, so with large dictionaries the speed increase may not be worth the memory cost. Norwig's algorithm combined with Bloom filters for more space-efficient lookup could be a comparable option with large dictionary sizes (and small maximum edit distances).

2. How would the code perform with an edit distance of 3?
The edit distance is definitely the costliest variable in the algorithm. We saw above that the maximum number of permutations per edit is ~ (54n + 25). Since we looking at a significantly smaller set by traversing the trie instead of generating all permutations, our constant will be much smaller than this ('q' is typically only followed by 'u', for instance). Nonetheless, our algorithm still runs in O(n ^ e) time, so we would expect the time to increase significantly.

The Levenshtein algorithm is independent of edit distance, so it would be a good choice for higher edit distances. Its much slower with small allowable distances however, as it runs in O(n ^ 2 * s), where s is the dictionary size and n is still the word length.

3. How does the code perform on long queries versus short queries and why?
The computational time grows linearly with query length, as there are now more possible permutations. While "cat" has only 4 places to insert a new letter, "internationalization" has 21 unique spots for doing such. Unfortunately, all algorithms are at least O(n), so switching to a different algorithm would be unlikely to help us.





