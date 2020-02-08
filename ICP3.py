import json
from stanfordcorenlp import StanfordCoreNLP

# Preset
host = 'http://localhost'
port = 9000
nlp = StanfordCoreNLP(host, port=port,timeout=30000)

#nlp=StanfordCoreNLP("http://localhost:9000/")
s='A rare black squirrel has become a regular visitor to a suburban garden'
s1='Brack Obama was born in Hawaii'
output = nlp.annotate(s, properties={"annotators":"tokenize,ssplit,pos,depparse,natlog,openie",
                                "outputFormat": "json",
                                 "openie.triple.strict":"true",
                                 "openie.max_entailments_per_clause":"1"})
a = json.loads(output)
print("The subject, object and verb/relation of the given sentence are")
print(a["sentences"][0]["openie"],'\n')
result = [a["sentences"][0]["openie"] for item in a]
for i in result:
    for rel in i:
        relationSent=rel['relation'],rel['subject'],rel['object']
        print('The triplet of the given sentence is')
        print(relationSent)


#WORDNET
# importing the library
from nltk.corpus import wordnet

# lets use word paint as an exqmple
syns = wordnet.synsets("paint")

# An example of a synset:
print(syns[0].name())
print('\n')
# Just the word:
print(syns[0].lemmas()[0].name())
print('\n')

# Definition of that first synset:
print(syns[0].definition())
print('\n')
# Examples of the word in use in sentences:
print(syns[0].examples())
print('\n')

#HYPONYM AND HYPERNYM of Tree
tree = wordnet.synset('Tree.n.01')
hypo = lambda s: s.hyponyms()
hyper = lambda s: s.hypernyms()
print("Hyponyms of Tree are: ",list(tree.closure(hypo)))
print("Hypernyms of Tree are: ",list(tree.closure(hyper)))
print("Partial Meronyms of Tree are: ",list(tree.part_meronyms()))
print("Substance Meronyms of Tree are: ",list(tree.substance_meronyms()))
print("Holonym of Tree are: ",list(tree.part_holonyms()))
print("Holonym of Tree are: ",wordnet.synset('kitchen.n.01').part_holonyms())
print("Entailment of Snore is: ", wordnet.synset('snore.v.01').entailments())

# synonyms and antonyms using wordnet using word
synonyms = []
antonyms = []

for syn in wordnet.synsets("worse"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print('The synonyms of worse are: ')
print(set(synonyms))
print('\n')
print('The antonyms of worse are: ')
print(set(antonyms))
print('\n')



# comparison/ similarity score between 2 words
w1 = wordnet.synset('goat.n.01')
w2 = wordnet.synset('sheep.n.01') # n denotes noun
print("The similarity score betwee ship and boat is =",w1.wup_similarity(w2))

######################################################################################
######################################################################################

import os
#os.environ['CLASSPATH'] = "D:\spring 2020\Knowledge Discovery\ICP 3\stanford-parser-full-2018-10-17"

java_path = "C:/Program Files/Java/jdk1.8.0_241/bin/java.exe"
os.environ['JAVAHOME'] = java_path
os.environ['STANFORD_PARSER'] = "D:\spring 2020\Knowledge Discovery\ICP 3\stanford-parser-full-2018-10-17"
os.environ['STANFORD_MODELS'] = "D:\spring 2020\Knowledge Discovery\ICP 3\stanford-parser-full-2018-10-17"

from nltk.parse.stanford import StanfordParser
from nltk.tree import ParentedTree, Tree

parser = StanfordParser()

# Parse the example sentence
sent = 'A rare black squirrel has become a regular visitor to a suburban garden'

t = list(parser.raw_parse(sent))[0]
print(t)
t = ParentedTree.convert(t)
#t.pretty_print()


# Breadth First Search the tree and take the first noun in the NP subtree.
def find_subject(t):
    for s in t.subtrees(lambda t: t.label() == 'NP'):
        for n in s.subtrees(lambda n: n.label().startswith('NN')):
            return (n[0], find_attrs(n))


# Depth First Search the tree and take the last verb in VP subtree.
def find_predicate(t):
    v = None

    for s in t.subtrees(lambda t: t.label() == 'VP'):
        for n in s.subtrees(lambda n: n.label().startswith('VB')):
            v = n
    return (v[0], find_attrs(v))


# Breadth First Search the siblings of VP subtree
# and take the first noun or adjective
def find_object(t):
    for s in t.subtrees(lambda t: t.label() == 'VP'):
        for n in s.subtrees(lambda n: n.label() in ['NP', 'PP', 'ADJP']):
            if n.label() in ['NP', 'PP']:
                for c in n.subtrees(lambda c: c.label().startswith('NN')):
                    return (c[0], find_attrs(c))
            else:
                for c in n.subtrees(lambda c: c.label().startswith('JJ')):
                    return (c[0], find_attrs(c))


def find_attrs(node):
    attrs = []
    p = node.parent()

    # Search siblings of adjective for adverbs
    if node.label().startswith('JJ'):
        for s in p:
            if s.label() == 'RB':
                attrs.append(s[0])

    elif node.label().startswith('NN'):
        for s in p:
            if s.label() in ['DT', 'PRP$', 'POS', 'JJ', 'CD', 'ADJP', 'QP', 'NP']:
                attrs.append(s[0])

    # Search siblings of verbs for adverb phrase
    elif node.label().startswith('VB'):
        for s in p:
            if s.label() == 'ADVP':
                attrs.append(' '.join(s.flatten()))

    # Search uncles
    # if the node is noun or adjective search for prepositional phrase
    if node.label().startswith('JJ') or node.label().startswith('NN'):
        for s in p.parent():
            if s != p and s.label() == 'PP':
                attrs.append(' '.join(s.flatten()))

    elif node.label().startswith('VB'):
        for s in p.parent():
            if s != p and s.label().startswith('VB'):
                attrs.append(' '.join(s.flatten()))

    return attrs


print (find_subject(t))
print (find_predicate(t))
print (find_object(t))