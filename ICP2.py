from stanfordcorenlp import StanfordCoreNLP

import nltk

# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)

# The sentence you want to parse
with open('input.txt') as f:
    lines = f.readlines()
for i in lines:
    sentence = i

    # POS
    print('POS：', nlp.pos_tag(sentence))

    # Tokenize
    print('Tokenize：', nlp.word_tokenize(sentence))

    # NER
    try:
        print('NER：', nlp.ner(sentence))
    except:
        print("No NER")
    try:
        print('Parser：')
        print(nlp.parse(sentence))
    except:
        print("No Parser")
    try:
        print(nlp.dependency_parse(sentence))
    except:
        print("No Dependency")

    # Parser
# Close Stanford Parser
nlp.close()