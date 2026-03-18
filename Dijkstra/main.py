import random

lista = []
random.seed(73)
for e in range(6):
    aux = []
    for c in range(6):
        if e == c:
            aux.append(-1)
        else:
            aux.append(random.randint(1,21))
    lista.append(aux)

#print(lista)
print('Matriz de Pesos:\n')
for i in lista:
    print(i)

inicio = random.randint(0,6)
