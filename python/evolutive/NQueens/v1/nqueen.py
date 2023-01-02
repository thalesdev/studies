import random
import math
from QueensChromosome import *


n = 20
len_gens = n
len_pop =  20
len_torn = 20*n 
generations = 100
population = [QueensChromosome([ random.randint(0,n-1)  for k in range(len_gens)]) for j in range(len_pop)]
mutation_prob = 0.1	
crossover_prob = 0.95
stop = False

def crossover(index_father_1, index_father_2):
	point = random.randint(0, len_gens-1)
	return population[index_father_1].cross(point,population[index_father_2])

def best_score():
	best_Score,best_score_id = 0,0
	for k in range(len_pop):
		Score = population[k].score()
		if Score > best_Score:
			best_Score = Score
			best_score_id = k
	return best_score_id

def init():
	global population
	i = 0
	while(True):
		print('='*50)
		print('\n\nGeracao ' + str(i+1) + '\n')
		print('='*50)
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
					son.mutate(random.randint(0,1))
				score_father_1 = population[father_1_id].score()
				score_son = son.score()
				if score_son > score_father_1:
					population[father_1_id] = son
		best_score_id = best_score()
		score = population[best_score_id].score()
		print("*"*50)
		print('Melhor cromossomo :\n', population[best_score_id])
		if score == len_gens:
				print('\nTivemos o melhor cromossomo na geracao {}'.format(i+1))
				break
		print("*"*50)
		i+=1
	id = best_score()
	print('\n\nMelhor pontucao :',population[id].score(), "\nMelhor individuo :", population[id] )


init()