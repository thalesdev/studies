import random
import json


class Chromosome:
    def __init__(self, queens=[]):
        self.__size = len(queens)
        self.gens = []
        self.score = 0
        self.__queens = queens
        self.__score =  self.__calc_score()

    @property
    def score(self):
        return self.__score

    @property
    def gens(self):
        return self.__queens

    @score.setter
    def score(self, value):
        pass

    @gens.setter
    def gens(self, queens=[]):
        self.__queens = queens if isinstance(queens, list) else []
    
    def __conflict(self, i):
        error, queens = False, self.__queens
        for k,queen in enumerate(queens[:i]):
            if ( queen == queens[i]) or queens[k] == queens[i]-(i-k) or queens[k] == queens[i]+(i-k):
                error = True
                break
        return error

    def __calc_score(self):
        score = 0
        for j in range(len(self.gens)):
            score += 1 if  not self.__conflict(j) else 0
        return score

    def mutation(self, single_gen=False):
        """
            Aplica a mutacao do cromosomo.

            :param single_gen: Mutacao de 1 Gen ou N Gens
            :type single_gen: bool
            :return: Retorna o cromossomo modificado.
            :rtype: list

            :Example:

            >>> mutation(True)
            antes [1,2,3,5] depois [3,0,1,5]
        """
        amount = 1 if single_gen else random.randint(2, self.__size-1)
        gens = []
        for i in range(amount):
            gen = random.randint(0, self.__size-1)
            while gen in gens:
                gen = random.randint(0, self.__size-1)
            gens.append(gen)
            moves = random.randint(0, self.__size-1)
            direction = random.randint(0, 1)
            if direction == 1:
                if (self.__queens[gen]+moves) > self.__size-1:
                    self.__queens[gen] = (
                        self.__queens[gen]+moves) - self.__size
                else:
                    self.__queens[gen] += moves
            else:
                if (self.__queens[gen]-moves) < 0:
                    self.__queens[gen] = (self.__size-1) - \
                        abs(self.__queens[gen]-moves)
                else:
                    self.__queens[gen] -= moves
        self.__score = self.__calc_score()
        return list(self.__queens)

    def cross(self, point, parent):
        """
            Aplica o cruzamento de ponto ao cromossomo.

            :param point: Numero do gen que vai dividir quantos gens vem de cada pai.
            :type single_gen: int
            :param parent: Pai para o cruzamento.
            :type single_gen: Chromosome
            :return: Retorna o filho produzido pelo cruzamento de ponto.
            :rtype: Chromosome

            :Example:
            >>> parent = Chromosome([1,2,3,4])
            >>> parent2 = Chromosome([5,6,7,8])
            >>> parent.cross(2, parent2)
            Chromosome([5,6,3,4])
        """
        parent_gens = parent.gens
        L_1 = [ parent_gens[k] for k in range(point) ]
        L_2 = [ self.__queens[k] for k in range(point, self.__size)]
        son =  Chromosome( L_1 + L_2 ) if random.randint(0,1) else Chromosome( L_2 + L_1 ) 
        return son
    def __str__(self):
        return "Chromosome("+str(self.gens)+","+ str(self.score)+")"
    
    def dumps(self):
        queen = { 
            "gens" : {},
            "score" : self.score
        }
        
        for index,gen in enumerate(self.gens):
            queen['gens'][index] = gen
        return queen

if __name__ == "__main__":
    parent = Chromosome([2, 0, 3, 1])
    print(parent)

