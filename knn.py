import csv
import random
import math
import operator
training_set = []
testing_set = []

def get_data(file_name, split_prop, training, testing):
	"""This function reads the data from the csv file and splits it into testing and training sets"""
	with open(file_name, 'r') as file:
		lines = csv.reader(file)
		dataset = list(lines)
		for x in range(1,len(dataset)):
				for y in range(1, len(dataset[x])):
					dataset[x][y] = float(dataset[x][y])
				if random.random() < split_prop:
					training.append(dataset[x])
				else:
					testing.append(dataset[x])

def calc_dist(first, second):
	"""this function calculates the euclediean distance between two given points"""
	distance = 0
	for x in range(1,len(first)):
		distance += pow(first[x] - second[x], 2)
	return math.sqrt(distance)


def get_neighbors(training, testing_point, k):
	"""this function gets the closest K neighbors by calculating the distance between testing point and testing set and sorting the distances"""
	distances = []
	for x in range(len(training)):
		dist = calc_dist(testing_point, training[x])
		distances.append((training[x], dist))
	distances.sort(key = operator.itemgetter(1))

	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def get_common(neighbors):
	"""This function gets the most common class between the k neighbors"""
	votes = {}
	for x in range(len(neighbors)):
		vote = neighbors[x][0]
		if vote in votes:
			votes[vote] += 1;
		else:
			votes[vote] = 1;
	votes_sorted = sorted(votes.items(), key=lambda kv: kv[1], reverse = True)
	return votes_sorted[0][0]


def get_accuracy(test, predictions):
	"""This function calculates the accuracy"""
	correct = 0
	for x in range(len(test)):
		if test[x][0] == predictions[x]:
			correct+=1
	return (correct / float(len(test))) * 100
			

get_data("data.csv", 0.8, training_set, testing_set)