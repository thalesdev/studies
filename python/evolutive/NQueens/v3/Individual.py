import json
import numpy as np
from itertools import count


class Individual:
    """Implementação do tabuleiro NxN."""

    def __init__(self, n=8, queens=[], cross="two_point"):
        self.n = n
        self.queens = np.random.randint(0, self.n, size=(
            self.n,)) if len(queens) == 0 else queens
        self.score = self.__score()
        self._cross_type = cross

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        if n > 0:
            self._n = n
        else:
            raise Exception("Erro o N deve ser maior que 0.")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if val > 0:
            self._score = val

    def conflict(self, i):
        error = False
        for k, queen in enumerate(self.queens[:i]):
            if any([queen == self.queens[i],
                    self.queens[k] == (self.queens[i]-(i-k)), self.queens[k] == (self.queens[i]+(i-k))]):
                error = True
                break
        return error

    def __score(self):
        # return 11
        score = 0
        for j in range(self.n):
            score += 1 if not self.conflict(j) else 0
        return score

    def cross_point(self, parent):
        point = np.random.randint(1, self.n-1)
        offspring = np.concatenate(
            (self.queens[:point], parent.queens[point:])).copy()
        return Individual(self.n, offspring)

    def cross_two_point(self, parent):
        fp = np.random.randint(1, self.n-2)
        sp = np.random.randint(fp+1, self.n)
        offspring = np.concatenate(
            (self.queens[:fp], parent.queens[fp:sp], self.queens[sp:])).copy()
        return Individual(self.n, offspring)

    def cross_uniform(self, parent):
        choices = np.random.randint(2, size=self.n)
        offspring = np.empty((0,)).astype('uint32')
        for (index, ), choice in np.ndenumerate(choices):
            if not choice:
                offspring = np.append(
                    offspring, self.queens[index])
            else:
                offspring = np.append(
                    offspring, parent.queens[index])
        return Individual(self.n, offspring)

    @property
    def cross(self):
        """
            :rtype: function
        """
        return self.__getattribute__("cross_{}".format(self._cross_type))

    def mutate(self):
        to_mutate_size = np.random.randint(1, self.n+1)
        index = np.random.choice(self.n, to_mutate_size, False)

        def permut_gen(queen):
            moves = np.random.randint(self.n-1)
            if np.random.randint(2):
                queen = queen + \
                    moves if (queen+moves) <= (self.n -
                                               1) else ((queen+moves) - self.n)
            else:
                queen = (queen-moves) if (queen -
                                          moves) >= 0 else (self.n-1) - (abs(queen-moves))

            return queen
        self.queens[index] = np.vectorize(permut_gen)(self.queens[index])
        self.score = self.__score()
        return self

    def __str__(self):
        return "Individual Score : {} , Queens :{} ".format(self.score, str(self.queens))

    @property
    def to_dict(self):
        return {
            "queens": self.queens,
            "score": self.score,
            "cross_type": self._cross_type
        }

    @staticmethod
    def random_population(k, n, cross):
        for _ in range(k):
            yield Individual(n, cross=cross)
