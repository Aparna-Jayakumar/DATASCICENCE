def gen_ngrams(text,WordsToCombine):
    words = text.split()
    output = []
    for i in range(len(words) - WordsToCombine +1):
        output.append(words[i:i + WordsToCombine])
    return  output
x = gen_ngrams(
    text= 'Python is a computer programming language',
    WordsToCombine = 3)
print(x)