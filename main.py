import csv
from spell_suggester import SpellSuggester

def main():
    t = SpellSuggester()
    dict_name = "word_frequency.csv"
    query_name = "misspelled_queries.csv"
    outfile_name = "suggestions.txt"

    with open(dict_name) as f:
        reader = csv.reader(f)
        for row in reader:
            word = row[0].lower()
            freq = row[1]
            t.add_word(word,freq)
    with open(query_name) as f:
        with open(outfile_name, 'wb') as out:
            reader = csv.reader(f)
            for row in reader:
                word = row[0].lower()
                suggestions = t.suggestions(word, max_dist = 2)
                out.write("* " + word + ": " + str(suggestions) + "\n")

if __name__ == '__main__':
    main()
