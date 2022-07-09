import math
from grafo import *
from matplotlib import pyplot as plt

partida = input("Insira o ponto de partida: ")
destino = input("Ïnsira o destino desejado: ")

#Definição das variáveis e listas
sentido_reto = grafo
melhor_caminho = {}
rota = []
path_no = {}

#Garante que o dijkstra não irá escolher o nó atual como menor caminho (evita voltas)
for no in sentido_reto:
    melhor_caminho[no] = math.inf
melhor_caminho[partida] = 0

# Garante que o algoritmo está sequencial, e adiciona os nós de menor peso
   while sentido_reto:
    menor_no = None
    for no_atual in sentido_reto:
        if menor_no is None:
            menor_no = no_atual
        elif melhor_caminho[menor_no] \
            > melhor_caminho[no_atual]:
            menor_no = no_atual
    for (no, valor) in sentido_reto[menor_no].items():
        if valor + melhor_caminho[menor_no] \
            < melhor_caminho[no]:
            melhor_caminho[no] = valor \
                + melhor_caminho[menor_no]
            path_no[no] = menor_no
    sentido_reto.pop(menor_no)
no = destino
while no != partida:
    try:
        rota.insert(0, no)
        no = path_no[no]
    except Exception:
        print('Rota inválida.')
        break
rota.insert(0, partida)

# Printa o melhor caminho até o destino, caso a lista seja diferente de infinito
if melhor_caminho[destino] != math.inf:
    print('O melhor caminho é ' + str(rota))

# Plota o gráfico com o melhor caminho e quantidade de paradas
x = rota
plt.plot(x)
plt.xlabel('Quantidade de paradas')
plt.title('Caminho a ser percorrido')
plt.show()
