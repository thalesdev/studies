#conding : utf-8

import random
import math
import itertools
from Chromosome import Chromosome
from random import shuffle
from tqdm import tqdm


class NQueensGenetic:
    def __init__(self, N=4, pop_size=20, torn_size=80,
                 mut_prob=0.1, cross_prob=0.95,  generations=100, mult_threading=False):
        self.N = N
        self.pop_size = pop_size
        self.torn_size = torn_size
        self.generations = generations
        self.mult_threading = mult_threading
        self.mut_prob = mut_prob
        self.cross_prob = cross_prob
        self.__pop__()

    @property
    def pop_size(self):
        return self.__pop_size

    @pop_size.setter
    def pop_size(self, size):
        if size > 0:
            self.__pop_size = size
            self.__pop__()
        else:
            raise Exception("Tamanho de população invalida!!")

    def __pop__(self):
        self.__population = [Chromosome([random.randint(
            0, self.N-1) for k in range(self.N)]) for j in range(self.pop_size)]

    def __crossover(self, parent_1, parent_2):
        point = random.randint(0, self.N-1)
        return self.__population[parent_1].cross(point, self.__population[parent_2])

    def __best_score(self):
        best_score, best_score_id = 0, 0
        for k in range(self.pop_size):
            score = self.__population[k].score
            if score > best_score:
                best_score = score
                best_score_id = k
        return best_score_id

    def __unique_pop(self):
        individuals = []
        ids = []
        for id, individual in enumerate(self.__population):
            if individual.gens not in individuals:
                individuals.append(individual.gens)
                ids.append(id)
        pop = [self.__population[id] for id in ids]
        gap = self.__pop_size - len(pop)
        pop.extend([Chromosome([random.randint(0, self.N-1)
                                for k in range(self.N)]) for j in range(gap)])
        return pop

    def __fit__(self):
        self.__population = list(sorted(random.sample(self.__population, len(
            self.__population)), key=lambda e: e.score, reverse=True))[:self.pop_size]
        self.__population = self.__unique_pop()

    def __tornament(self):
        mutation__prob = random.random()
        crossover__prob = random.random()
        if crossover__prob <= self.cross_prob:
            parent_1_id = random.randint(0, self.pop_size-1)
            parent_2_id = random.randint(0, self.pop_size-1)
            while(parent_1_id == parent_2_id):
                parent_2_id = random.randint(0, self.pop_size-1)
            son = self.__crossover(parent_1_id, parent_2_id)
            if mutation__prob <= self.mut_prob:
                son.mutation(random.randint(0, 1))
            self.__population.append(son)
            #score_parent_1 = self.__population[parent_1_id].score
            #score_son = son.score
            # if score_son > score_parent_1:
            #    self.__population[parent_1_id] = son

    def run(self, logging=False, limit=True, logging_multply=100):
        generation = 0
        for _ in tqdm(range(self.generations)):
            for tourn_id in range(self.torn_size):
                self.__tornament()
            best_score_id = self.__best_score()
            score = self.__population[best_score_id].score
            if score == self.N:
               #pass
               #print('\nTivemos o melhor cromossomo na geracao {}'.format(generation+1))
               break
            if logging and generation % logging_multply == 0:
               #pass
                print("="*50)
                print('Melhor cromossomo :\n', self.__population[best_score_id])
                yield (self.__population[best_score_id], generation)
            if generation == self.generations and limit:
               print(generation)
            self.__fit__()
            generation += 1
        id = self.__best_score()
        print('\n\nMelhor pontucao :',self.__population[id].score, "\nMelhor individuo :", self.__population[id] )
        yield self.__population[id], generation


if __name__ == "__main__":
    nqueens = NQueensGenetic(N=100, mut_prob=0.15, cross_prob=0.99)
    nqueens.run(True, True)
