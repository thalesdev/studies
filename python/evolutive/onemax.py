import random
len_gens = 8
len_pop =  100
len_torn = 40 
generations = 500
population = [[random.randint(0,1) for k in range(len_gens)] for j in range(len_pop)]
mutation_prob = 0.2
crossover_prob = 0.7
stop = False


def score(a):
	c=0
	for k in range(len(a)):
		c+=a[k]
	return c
def best_score():
	best_Score,best_score_id = 0,0
	for k in range(len_pop):
		Score = score(population[k])
		if Score > best_Score:
			best_Score = Score
			best_score_id = k
	return best_score_id

def mutation(individual):
	gen = random.randint(0, len_gens-1)
	if individual[gen] == 0:
		individual[gen] = 1
	else:
		individual[gen] = 0
	return individual
def crossover(index_father_1, index_father_2):
	global population
	point = random.randint(0, len_gens-1)
	son = []
	for k in range(point):
		son.append(population[index_father_1][k])
	for k in range(point, len_gens):
		son.append(population[index_father_2][k])
	return son
for i in range(generations):
	print('\n\nGeracao ' + str(i+1) + '\n\n')
	for k in range(len_torn):
		mutation__prob = random.random()
		crossover__prob = random.random()
		if crossover__prob <= crossover_prob:
			father_1_id = random.randint(0, len_pop-1)
			father_2_id = random.randint(0, len_pop-1)
			while(father_1_id == father_2_id):
				father_2_id = random.randint(0, len_pop-1)
			son = crossover(father_1_id, father_2_id)
			if mutation__prob <= mutation_prob:
				son = mutation(son)
			score_father_1 = score(population[father_1_id])
			score_son = score(son)
			if score_son > score_father_1:
				population[father_1_id] = son
	best_score_id = best_score()
	print('Melhor cromossomo :', population[best_score_id])
	if score(population[best_score_id]) == len_gens:
			print('Tivemos o melhor cromossomo na geracao', i+1)
			break

print('Melhor pontucao :',score(population[best_score()]))
						