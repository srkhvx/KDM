from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2Vec
import pandas as pd
import sklearn as sk
import math




# creating spark session
spark = SparkSession.builder .appName("Ngram Example").getOrCreate()

lines=[]

for i in range(5):
        with open('Doc_'+str(i+1)+'.txt') as f:
                lines.append(f.readlines()[0].replace("'","").replace("(","").replace(")","").replace(",","").replace(",",""))

# load up our sample sentences
first = lines[0]
second = lines[1]
third = lines[2]
fourth = lines[3]
fifth = lines[4]
# split so each word have their own string
first = first.split(" ")
second = second.split(" ")
third=third.split(" ")
fourth=fourth.split(" ")
fifth=fifth.split(" ")


total = set(first).union(set(second)).union(set(third)).union(set(fourth)).union(set(fifth))
print(total)
wordDictA = dict.fromkeys(total, 0)
wordDictB = dict.fromkeys(total, 0)
wordDictC = dict.fromkeys(total, 0)
wordDictD = dict.fromkeys(total, 0)
wordDictE = dict.fromkeys(total, 0)

for word in first:
    wordDictA[word] += 1

for word in second:
    wordDictB[word] += 1

for word in third:
    wordDictC[word] += 1

for word in fourth:
    wordDictD[word] += 1

for word in fifth:
    wordDictE[word] += 1

# put them in a dataframe and then view the result:
print(pd.DataFrame([wordDictA, wordDictB, wordDictC,wordDictD, wordDictE]))

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict
#running our sentences through the tf function:
tfFirst = computeTF(wordDictA, first)
tfSecond = computeTF(wordDictB, second)
tfThird = computeTF(wordDictC, third)
tfFourth = computeTF(wordDictD, fourth)
tfFifth = computeTF(wordDictE, fifth)
#Converting to dataframe for visualization
print(pd.DataFrame([tfFirst, tfSecond,tfThird, tfFourth, tfFifth]))


# creating the log portion of the Excel table we saw earlier
def computeIDF(docList):
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))

    return idfDict


# inputing our sentences in the log file
idfs = computeIDF([wordDictA, wordDictB,wordDictC,wordDictD,wordDictE])


# The actual calculation of TF*IDF from the table above:
def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf


# running our two sentences through the IDF:
idfFirst = computeTFIDF(tfFirst, idfs)
idfSecond = computeTFIDF(tfSecond, idfs)
idfThird = computeTFIDF(tfThird, idfs)
idfFourth = computeTFIDF(tfFourth, idfs)
idfFifth = computeTFIDF(tfFifth, idfs)
# putting it in a dataframe
idf = pd.DataFrame([idfFirst, idfSecond,idfThird, idfFourth, idfFifth])

max_words={}
final_dict={}
for i in range (len(idf.columns)):
    max_words[idf.columns[i]]=idf[idf.columns.values[i]].max()
for i in range(5):
    final_dict[max(max_words.__iter__(), key=lambda k: max_words[k])]=max_words.pop(max(max_words.__iter__(), key=lambda k: max_words[k]),None)
print(final_dict)

# Input data: Each row is a bag of words from a sentence or document.
documentDF = spark.createDataFrame([
    (first, ),
    (second, ),
    (third, ),
    (fourth, ),
    (fifth, )
], ["text"])


# Learn a mapping from words to Vectors.
word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
model = word2Vec.fit(documentDF)
result = model.transform(documentDF)

for row in result.collect():
    text, vector = row
    #printing the results
    print("Text: [%s] => \nVector: %s\n" % (", ".join(text), str(vector)))

# showing the synonyms and cosine similarity of the word in input data
for key in final_dict:
    print(key)
    synonyms = model.findSynonyms(key, 5)   # its okay for certain words , real bad for others
    synonyms.show(5)


#closing the spark session
spark.stop()