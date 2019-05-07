from knn import *

random.seed(12345)


def make_population(population_size, population, max_k):
	for x in range(population_size):
		random_k = random.randint(1, max_k)
		if random_k in population:
			x -= 1
			continue
		else:
			population[random_k] = 0

def calc_fitness(population):
	for k in population:
		predictions = []
		for x in range(len(testing_set)):
			neighbors = get_neighbors(training_set, testing_set[x], k)
			label = get_common(neighbors)
			predictions.append(label)
		population[k] = get_accuracy(testing_set, predictions)
	population_sorted = sorted(population.items(), key=lambda kv: kv[1], reverse = True)
	return population_sorted


def create_new_population(population, population_size,max_k):
	new_population = {}
	for x in range(1):
		new_population[population[x][0]] = population[x][1]

	for x in range(population_size-len(new_population)):
		random_k = random.randint(1, max_k)
		if random_k in new_population:
			x -= 1
			continue
		else:
			new_population[random_k] = 0

	return new_population
		

population_size = 3
population = {}

make_population(population_size, population, len(testing_set)-1)
population = calc_fitness(population)
epochs = 0
while(population[0][1] < 98 and epochs<50):
	tmp = population
	new_population = create_new_population(tmp, population_size, len(testing_set)-1)
	population = calc_fitness(new_population)
	
	print("#"+str(epochs)+" Best Acuuracy is: " + str(population[0][1]))
	epochs+=1

print("Training is done!!!")
print("# Best Acuuracy is: " + str(population[0][1]))
print("# Best K value is: " + str(population[0][0]))

