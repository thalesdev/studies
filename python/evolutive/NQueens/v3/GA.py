from Individual import Individual
import numpy as np
from tqdm import tqdm
import random

class NQueensGA:
    def __init__(self, n=4, pop_size=20, torn_size=80,
                 mut_prob=0.1, cross="two_point", epochs=100, selection="roulette"):
        self.n = n
        self.pop_size = pop_size
        self.torn_size = torn_size
        self.epochs = epochs
        self.mut_prob = mut_prob
        self.cross = cross
        self.selection_type = selection
        self.pop = np.array(list(Individual.random_population(
            self.pop_size, self.n, cross)), dtype=Individual)
        self.pop_score = np.vectorize(lambda ind: ind.score)(self.pop)
        self.S = sum(self.pop_score)

    @property
    def roulette(self):
        r = np.random.randint(0, self.S+1)
        s_ = 0
        for k in np.arange(self.pop.size):
            if s_ > r:
                return k
            s_ += self.pop[k].score
        return self.pop.size-1

    @property
    def classification(self):
        index = list(map(lambda e: e[0][0], sorted(
            np.ndenumerate(self.pop_score), key=lambda e:  e[1])))[::-1]
        scores = np.empty((self.pop.size,), dtype="uint32")
        scores[index] = np.arange(self.pop.size)
        S = sum(scores)
        r = np.random.randint(0, S+1)
        s_ = 0
        for k in np.random.choice(index, scores.size, False):
            if s_ > r:
                return k
            s_ += scores[k]
        return scores[-1]

    @property
    def random_selection(self):
        return self.pop[np.random.choice(self.pop.size, 2, replace=False)]

    @property
    def min(self):
        return np.argmin(self.pop_score)

    @property
    def max(self):
        return np.argmax(self.pop_score)

    @property
    def limits(self):
        return self.max, self.min

    def selection(self):
        parent = self.__getattribute__(self.selection_type)
        while(True):
            parent2 = self.__getattribute__(self.selection_type)
            if parent != parent2:
                break
        return self.pop[[parent, parent2]]

    def _tourn(self):
        sons = []
        for _ in range(self.torn_size):
            if self.selection_type == "random":
                p1, p2 = ga.random_selection
            else:
                p1, p2 = ga.selection()
            offspring = p1.cross(p2)
            if np.random.random() < self.mut_prob:
                offspring.mutate()
            sons += [offspring]
        #self.pop = np.concatenate((self.pop, sons))
        #self.pop_score = np.vectorize(lambda ind: ind.score)(self.pop)

    def _fit(self):
        pop = sorted(np.ndenumerate(self.pop_score),
                     key=lambda e: e[1], reverse=True)[:self.pop_size]
        pop = list(map(lambda e: self.pop[e[0][0]], pop))
        self.pop = np.array(pop, dtype=Individual)
        self.pop_score = np.vectorize(lambda ind: ind.score)(self.pop)
        self.S = sum(self.pop_score)

    def run(self):
        for _ in tqdm(range(self.epochs)):
            self._tourn()
        print("Terminou o algo genetico o score maximo foi {}".format(
            self.pop[self.max].score))


ga = NQueensGA(n=100, selection="random", cross="point")
ga.run()

"""
for k in range(100):
    id = ga.classification
    print(ga.pop_score[id], ga.pop_score[_max])
"""
