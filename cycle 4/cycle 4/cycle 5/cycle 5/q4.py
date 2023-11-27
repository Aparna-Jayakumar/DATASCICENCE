from nltk import ngrams
sentences = 'Natural Language Processing'
n=3
unigrams = ngrams(sentences.split(),n)
for grams in unigrams:
    print(grams)