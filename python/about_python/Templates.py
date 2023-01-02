import os

##  Templates de strings so biuriful guys  ##
# Aceita objetos e operacoes desde que esteja dentro do {}
# lets bora


frutas = ["uva", "morango", "abacaxi", "pera"]
title = "Minha lista de frutas"
tp1 = "{title:^30} : {frutas[1]:^9}".format(
    title=title, frutas=frutas)  # > right ,  < left , ^ center
tp2 = "{title:^30} : {os.name:^9}".format(
    title="Meu Sistema operacional", os=os)  # aceita propriedades
print(tp1)
print(tp2)


# formatar numericos


cientific = "{0:^30e} = {1:^30.3e} = {2:^30g}".format(*([3.145677]*3))
bases = "{0:^30X} = {1:^30o} = {2:^30b} ".format(*([255]*3))

print(cientific)
print(bases)


# aplicando o template a um decorador basico


def tag(name):
    def tagDecorator(func):
        def wrapper(*args):
            return "<{0}>{1}</{0}>".format(name, func(*args))
        return wrapper
    return tagDecorator

@tag("div")
@tag("p")
def lpisum():
    return "Givele"


print(lpisum())



