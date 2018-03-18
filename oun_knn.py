import csv
import random
import math
import operator

import numpy as np
import csv
import time
 
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])
 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	y = 0
	for x in range(length):
		print ('instance2')
		print (instance2 [0][1])
		print(instance1[x])
		print(instance2[x])
		#for y in range(0,17):
			#distance += pow((instance1[x] - instance2[x][y], 2)
			#print ('hello')	
	#return math.sqrt(distance)
	#return (distance)

def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	length = 10
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		print('DIST')
		print(dist)
		distances.append((trainingSet[x], dist))
		print(distances)
		time.sleep(1)
	distances.sort(key=operator.itemgetter(1))
	print(distances)
	neighbors = []
	#for x in range(k):
		#neighbors.append(distances[x][0])
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def readcsv(filename):
	ifile = open(filename, "rU")
	reader = csv.reader(ifile, delimiter=";")
	rownum = 0	
	a = []
	matix = []
	for row in reader:
		a.append (row)
		rownum += 1
	ifile.close()
	
	for x in range(len(a) -1):
		print (a[x][0])
		if a[x] == ',':
			print ('new line')
		else:
			print ('another num')
	return a
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.67
	filename = 'LetterA.csv'

	#Read the training file
	AtrainingSet = readcsv ('LetterA.csv')
	#BtrainingSet = readcsv ('LetterA.csv')
	#BtrainingSet = readcsv (filename)
	#CtrainingSet = readcsv (filename)
	
	#trainingSet = ([AtrainingSet],[BtrainingSet])
	
	#Read the test file
	testSet = readcsv ('TestA.csv')
	
	print(trainingSet)
	k = 3
	neighbors = getNeighbors(AtrainingSet, testSet, k)
	
	print('neighbors')
	print(neighbors)
	#loadDataset('LetterA.data', split, trainingSet, testSet)
	#print 'Train set:' + repr(len(trainingSet))
	#print 'Test set:' + repr(len(testSet))
	#generate predictions
	#predictions=[]
	
	#for x in range(len(testSet)):
	#	neighbors = getNeighbors(trainingSet, testSet[x], k)
	#	result = getResponse(neighbors)
		#predictions.append(result)
		#print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	#accuracy = getAccuracy(testSet, predictions)
	#print('Accuracy: ' + repr(accuracy) + '%')
	
main()