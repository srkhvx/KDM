import nltk
with open('input.txt') as f:
    lines = f.readlines()
import numpy

for i in lines:
    tokenized = nltk.sent_tokenize(i)
    for j in tokenized:
        # Word tokenizers is used to find the words
        # and punctuation in a string
        wordsList = nltk.word_tokenize(j)

        # removing stop words from wordList
        wordsList = [w for w in wordsList]

        #  Using a Tagger. Which is part-of-speech
        # tagger or POS-tagger.
        tagged = nltk.pos_tag(wordsList)
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(j))):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk))
print(tagged)

# import spacy
# nlp = spacy.load('en')
#
# # Add neural coref to SpaCy's pipe
# import neuralcoref
# neuralcoref.add_to_pipe(nlp)
#
# # You're done. You can now use NeuralCoref as you usually manipulate a SpaCy document annotations.
# doc = nlp(u'My sister has a dog. She loves him.')
#
# doc._.has_coref
# doc._.coref_clusters