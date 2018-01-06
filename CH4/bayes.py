def loadDataSet():
	postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'], ['maybe', 'not', 'take', 'him', 'to', 'dog','park', 'stupid'], ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'], ['stop', 'posting', 'stupid', 'worthless', 'garbage'], ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'], ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
	classVec = [0, 1, 0, 1, 0, 1]
	return postingList, classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document)
	return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "the word: %s is not in my Vocabulary!" % word
	return returnVec