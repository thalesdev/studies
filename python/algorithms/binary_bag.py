P = [2,3.1,1.98,5,3] # Pesos
V = [40,50,100,95,30] # Valores

# Conta o valor genericamente do peso ou do valor
def count(bag, target): 
    return sum([target[index] if value == 1 else 0 for index,value in enumerate(bag)])
best_bag = None
best_price = 0
# Mochila binaria recursiva
def binary_bag(bag, item = 0, max_weight=10):
    global best_bag
    global best_price
    temp_bag = list(bag)
    # Caso que a se torna inutil quando o peso ja e maior ou igual a capacidade...
    if count(bag, P) >= max_weight:
        pass
    # Quando chega nas folhas verifica se e a melhor solucao ate o momento...
    elif item == len(bag):
        price = count(bag, V)
        if price > best_price:
            best_price = count(bag, V)
            best_bag = bag
    else:
        # Chamadas recursiva adicionando o produto
        temp_bag[item] = 1
        binary_bag(temp_bag, item+1)
        binary_bag(bag, item+1) # backtraking 
# testes 

bag = [0,0,0,0,0] # Mochila vazia
binary_bag(bag)
print(best_bag, best_price)




