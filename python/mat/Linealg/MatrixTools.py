import numpy as np
import math
from scipy.linalg import lu

# Modulo criado para resolver operações com matrizes
def ComplexToReal(number):
	if(isinstance(number, complex)):
		if(number.imag == 0):
			return number.real
	return number

def ComplexToRealArray(array):
	aux = []
	for i in range(len(array)):
		aux.append(ComplexToReal(array[i]))
	return aux

def uniqueArray(array):
	aux = []
	for l in range(len(array)):
		if not array[l] in aux:
			aux.append(array[l])
	return aux

def Trace(A):

    """
        Traco da matriz A.
        Somatorio da sigma(A[i][j]) se i==j de i=1 ate n e j=1 ate n
    :param A:
    :return Real:
    """
    sum = 0
    for i in range(len(A)):
        for j in range(len(A)):
           if j==i:
               sum+= A[i][j]
    return sum

def Product(A, B):
    """
        Produto de matrizes.

    :param A:
    :param B:
    :return AB:
    """
    size_A = len(A)
    size_AC = len(A[0])
    if size_AC != len(B):
        raise Exception("O tamanho da matriz A deve ser o mesmo da matriz B")
    size_BC = len(B[0])
    R = []
    for i in range(size_A):
        R.append([])
        for j in range(size_BC):
            val = 0
            for k in range(size_AC):
                    val += A[i][k]*B[k][j]
            R[i].append(val)
    return R

def Pow(A, y):
    """
        Eleva a matriz a y-esima potencia. para todo n>=2.
    :param A:
    :param y:
    :return A^y:
    """
    if y >1:
        if y == 2:
            return Product(A,A)
        else:
            return Pow(A, y-1)

def RemoveLines(matriz, line = None, col = None):
    """
        Funcao para remover linha e colunas.
    :param matriz:
    :param line:
    :param col:
    :return:
    """
    mat = np.copy(matriz).tolist()
    if line is not None:
        mat = np.delete(mat, line, 0)
    if col is not None:
        mat = np.delete(mat, col, 1)
    return mat.tolist()

def EmptyLines(matriz):
    """
        Funcao para verificar se existem linhas todas composta por zeros.
    :param matriz:
    :return Boolean:
    """
    for i in range(len(matriz)):
        c=0
        for j in range(len(matriz)):
            if matriz[i][j] == 0.0:
                c+=1
        if c == len(matriz):
            return True
    return False

def EmptyCols(matriz):
    """
        Funcao para verificar se existe uma coluna composta toda por zerso.
    :param matriz:
    :return Boolean:
    """
    for j in range(len(matriz[0])):
        c=0
        for i in range(len(matriz)):
            if matriz[i][j] == 0.0:
                c+=1
        if c == len(matriz):
            return True
    return False

def Det(A):
    """
        Funcao para calcular o determinante da matriz de ordem n-esima.
    :param A:
    :return Real:
    """
    mat = np.copy(A).tolist()
    cols = len(mat[0])
    lines = len(mat)
    j = det = i=0
    if EmptyLines(mat) or EmptyCols(mat):
        return 0
    if lines==2 and cols == 2:
        a = mat[0][0]
        b = mat[0][1]
        c = mat[1][0]
        d = mat[1][1]
        factor = a*d - b*c
        return factor
    else:
        while i < lines:
            det += mat[i][j] * math.pow((-1), i + j) * Det(RemoveLines(mat, i, j))
            i += 1
    return det

def GaussJordan(A):
    mat = np.copy(A).tolist()

    def fullzeros(vector):
        size = len(vector)
        c=0
        for l in vector:
            if l == 0:
                c+=1
        if c==size:
            return True

        return False
    def numericError(A):
    	aux = []
    	for i in range(len(A)):
    		aux.append(np.round(A[i], decimals=4))
    	return aux


    def normalize(vector, pivotIndex=0):
        aux = list(vector)
        for j in range(len(vector)):
            if vector[pivotIndex] != 0.0:
                aux[j] = vector[j]/vector[pivotIndex]
        return aux
    def stepOne(A):
        """
            Acha a linha mais a esquerda composta não composta por zeros.
        :param A:
        :return:
        """
        r= np.copy(A)
        matAux= r[~np.all(r == 0, axis=1)].tolist()
 
        for j in range(len(matAux[0])):
            for i in range(len(matAux)):
                if A[i][j] != 0.0:
                    aux = A[i]
                    matAux[i] = A[0]
                    matAux[0] = aux
                    return (0,j, matAux)
        return 0,0,[]
    def stepTwo(A,line = 0, pivot = 1):
        """
            Cria um pivo na linha.
        :param A:
        :param line:
        :param pivot:
        :return:
        """
        aux = np.copy(A).tolist()
        for j in range(len(A[0])):
            if A[line][pivot] != 0.0:
                aux[line][j] = A[line][j]/A[line][pivot]
        return aux
    def stepThree(A, linePivot=0, colPivot=0):
        """
            Remove todos elementos abaixo do pivo.
        :param A:
        :param linePivot:
        :param colPivot:
        :return:
        """
        iP = linePivot
        jP = colPivot
        aux = np.copy(A).tolist()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i != linePivot:
                    item = -A[i][jP]
                    if item != 0.0:
                        aux[i][j] = A[i][j] + item*A[iP][j]
        return aux
    def stepFour(A, startLine =0):
        """
            Usa a recurssao para fazer a Eliminacao Gaussiana.
        :param A:
        :param startLine:
        :return:
        """
        size = len(A)
        if size == 1:
        	if(not fullzeros(A[0])):
        		apivot, bpivot, mat = stepOne(A)
        		A = [numericError(A[0])]
        		return [normalize(A[0],bpivot)]
        	else:
        		return []

        elif size==0:
            return []
        else:
            mat = np.copy(A).tolist()
            apivot,bpivot, mat = stepOne(mat)
            if len(mat) > 0:
            	mat = stepTwo(mat,apivot,bpivot)
            	mat = stepThree(mat,apivot,bpivot)
            	return list([mat[0]]+ stepFour(mat[1:]))
            else:
            	return []
                
    def stepFive(A):

        """
            Eliminacao gaussiana-para frente(Jordan).
        :param A:
        :return [[]]:
        """
        toJordan = np.copy(A[::-1]).tolist()
        size = len(toJordan)
        if size>1:
            b = 0
            for k in range(len(toJordan[0])):
                if abs(toJordan[0][k]) != 0.0:
                    b = k
                    break
            aux = np.copy(toJordan).tolist()
            for i in range(1,size):
                for j in range(len(toJordan[0])):
                    aux[i][j] = toJordan[i][j] +  -toJordan[i][b]*toJordan[0][j]
            return aux
    def stepSix(A):
        """
            Resolve recursivamente a etapa pra frente.
        :param A:
        :return:
        """
        aux = np.copy(A)
        if isinstance(aux[0],list):
            A = aux[~np.all(aux == 0, axis=1)].tolist()
        size = len(A)
        if size == 2:
            return stepFive(A)
        elif size ==1:
            return A[0][::-1]
        else:
            mat = np.copy(A).tolist()
            mat = stepFive(mat)
            return list([mat[0]] + stepSix(mat[1:]))

    r = stepSix(removeZeros(stepFour(mat)))[::-1]
    if isinstance(r[0], list):
    	return removeZeros(r)
    else:
    	return r

def removeZeros(A):
    a = np.copy(A)
    return a[~np.all(a == 0, axis=1)].tolist()

def errorNum(A):
    aux = []
    for k in A:
        aux.append(np.round(k, decimals=4))
    return aux

def EigenValue(A):
    """
        Funcao para achar autovalores
    :param A:
    :return:
    """
    size = len(A)
    mat = np.copy(A).tolist()
    if size == 2:
        a = mat[0][0]
        b = mat[0][1]
        d = mat[1][0]
        c = mat[1][1]
        delta = (-c-a)**2 -4*((-d*b) +(a*c))
        if delta>0:
            x1 = ((-(-c-a)+math.sqrt(delta))/2)
            x2 = ((-(-c-a)-math.sqrt(delta))/2)
            return uniqueArray([x1,x2])
        else:
            x1 = ((-(-c-a)+ ((delta)**0.5)/2))
            x2 = ((-(-c-a)-((delta)**0.5)/2))
            return uniqueArray([x1,x2])
    else:
        a1 = 1
        a2 = -(Trace(mat))
        a3 = (-1 / 2) * (Trace(Pow(mat, 2)) - (Trace(mat) ** 2))
        a4 = -Det(mat)
        x1, x2, x3 = np.roots([a1, a2, a3, a4])
        list_ = np.around([x1,x2,x3], decimals=4).tolist()
        return uniqueArray(ComplexToRealArray(list_))
    return None

def Unique_rows(a):
    a = np.ascontiguousarray(a)
    unique_a = np.unique(a.view([('', a.dtype)]*a.shape[1]))
    return unique_a.view(a.dtype).reshape((unique_a.shape[0], a.shape[1]))

def EigenVector_v3(A):
    size = len(A)
    if size == 2 or size == 3:
        eigenValues = EigenValue(A)
        eigenvectors = []
        for root in eigenValues:
            mat_aux = np.copy(A).tolist()
            for i in range(size):
                mat_aux[i][i] = mat_aux[i][i] - root
                mat_aux[i].append(0)
            mat_aux = Unique_rows(mat_aux).tolist()
            if len(mat_aux) > 1:
                auto_space = GaussJordan_v2(mat_aux)
            else:
                auto_space = mat_aux[0]
            #print(auto_space)
            if (isinstance(auto_space[0], list)):
                if len(auto_space) >1:
                    eigenvectors.append(SolveLinear(auto_space))
            else:
                if len(auto_space) == 3:
                    vet = []
                    vet.append(-auto_space[1])
                    vet.append(1)
                    eigenvectors.append(vet)
                elif len(auto_space) == 4:
                    vet1 = []
                    vet1.append(-auto_space[1])
                    vet1.append(1)
                    vet1.append(0)
                    vet2 = []
                    vet2.append(-auto_space[2])
                    vet2.append(0)
                    vet2.append(1)
                    eigenvectors.append([vet1, vet2])
        return eigenvectors
    return None

def LoadFromFile(file="mat.txt", splitDelimiter=" ", Set=1):
    """
        Abre uma matriz apartir de um arquivo.
        Set 1:Inteiros;2:Reais;3:Complexos;
    :param file:
    :param splitDelimiter:
    :param Set:
    :return:
    """
    pointer = open(file,"r")
    matriz = pointer.read().split("\n")
    chunks = []    
    for l in range(len(matriz)):
        if(len(matriz[l]) != 0):
            chunks.append(matriz[l].split(splitDelimiter))
    for i in range(len(chunks)):
        for j in range(len(chunks[i])):
            if Set ==1:
                chunks[i][j] = int(chunks[i][j])
            elif Set ==2:
                chunks[i][j] = float(chunks[i][j])
            else:
                chunks[i][j] = complex(''.join(chunks[i][j].split()))
    return chunks

def SolveLinear( VectorSpace ):
    """
		Função para achar uma solução particular de um espaco vetorial escalonado reduzido por linhas homogenio.
	"""
    #print( VectorSpace,"\n\n\n")
    def verityTrivialVar(col, matrix):
        lines = len(matrix)
        cols = len(matrix[0])
        c = 0
        for i in range(lines):
            c = 0
            for j in range(cols):
                if((matrix[i][j] == 0) and (matrix[i][col] != 0.0) and (col != j) and j<cols-1):
                    c+=1
                    if c== cols-2:
                        return True, i
        return False, 0
    size_x = len(VectorSpace)
    size_y = len(VectorSpace[0])
    variables_values = {}
    free_vars = {}
    A = np.copy(VectorSpace).tolist()
    for j in range(size_y-1):
        t_bol, t_line = verityTrivialVar(j, A)
        if(t_bol):
            variables_values[j] = A[t_line][size_y-1]/A[t_line][j]
        else:
            if(j>(size_x-1)):
                free_vars[j] = 1
    if len(free_vars) > 1:
        pass
		# fazer depois
    elif len(free_vars) == 1:
        vet = []
        for i in range(size_x):
            a = 0
            for j in range(size_y-1):
                if i != j:
                    if(j in free_vars):
                        a += -1*A[i][j]
                    elif j in variables_values:
                        a += variables_values[j]*A[i][j]
            vet.append(a)
        vet.append(1)
        return vet
    else:
        vet = []
        for i in range(size_x):
            a = 0
            for j in range(size_y):
                if i != j:
                    if(j in variables_values):
                        a+= variables_values[j]*A[i][j]
            vet.append(a)
        return vet
    return None

def pivotize(A):
    aux = []
    A = errorNum(A)
    pivot = 0
    for i in range(len(A)):
        if abs(A[i]) != 0.0:
            pivot = i
            break
    for k in A:
        if abs(A[pivot]) != 0.0:
            aux.append(k/A[pivot])
        else:
            #A[pivot] = np.round(A[pivot], decimals=4)
            return A
    aux = errorNum(aux)
    return aux

def pivotizeMatrix(A):
    aux = []
    for k in A:
        aux.append(pivotize(k))
    return removeZeros(aux)

def togglePiv(A):
    if A is not None:
        if(len(A[0])>1):
            if isinstance(A[0], list):
                aux = pivotizeMatrix(A)
        else:
            aux = pivotize(A)
        return aux
    return A

def GaussJordan_v2(A):
    pv, gauss_mat = lu(A, permute_l=True)
    gauss_mat = gauss_mat.tolist()
    def Jordan(Matrix):
        mat = np.copy(Matrix).tolist()[::-1]
        mat = removeZeros(mat)
        size = len(mat)
        if size>1:
            if(isinstance(mat[0], list)):
                if size == 2:
                    # passo base
                    for j in range(len(mat[0])):
                        if abs(mat[0][j]) != 0.0:
                            pivot = j
                            break
                    piv = mat[1][pivot]
                    for j in range(len(mat[0])):
                        mat[1][j] = mat[1][j] -  piv*mat[0][j]
                    return mat[::-1]
                else:
                    pivot = 0
                    for j in range(len(mat[0])):
                        if abs(mat[0][j]) != 0.0:
                            pivot = j
                            break
                    for i in range(1,len(mat)):
                        piv = mat[i][pivot]
                        for j in range(len(mat[0])):
                            mat[i][j] = mat[i][j] - piv * mat[0][j]
                    return list([mat[0]] + Jordan(mat[1::-1]))
            elif size == 0:
                return []
            else:
                return mat
    gauss_mat = togglePiv(gauss_mat)
    gauss_mat = togglePiv(Jordan(gauss_mat))
    return gauss_mat


b = (LoadFromFile("matriz.txt"))
print(EigenValue(b))
print(EigenVector_v3(b))